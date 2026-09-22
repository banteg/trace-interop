package main

// Copy into cmd/hivechain at the pinned Hive revision and run TestH13Fixtures.
// All keys below are intentionally public fixture keys, never wallet keys.
import (
	"encoding/json"
	"math/big"
	"os"
	"path/filepath"
	"strings"
	"testing"

	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/common/hexutil"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
)

func TestH13Fixtures(t *testing.T) {
	output := os.Getenv("TRACE_H13_OUTPUT")
	if output == "" {
		t.Fatal("set TRACE_H13_OUTPUT to a fresh output directory")
	}
	if err := os.Mkdir(output, 0755); err != nil {
		t.Fatal(err)
	}
	chainDir := filepath.Join(output, "chain")
	if err := os.Mkdir(chainDir, 0755); err != nil {
		t.Fatal(err)
	}
	cfg, err := (generatorConfig{chainLength: 2, txCount: 0, merged: true, lastFork: "prague",
		outputDir: chainDir, outputs: []string{"genesis", "chain", "headblock", "headstate", "forkenv", "headfcu"}}).withDefaults()
	if err != nil {
		t.Fatal(err)
	}
	g := newGenerator(cfg)
	target := common.HexToAddress("0x1002")
	marker := common.FromHex("0x602a600055602a60005260206000f3") // Store and return 42.
	balance := new(big.Int).Exp(big.NewInt(10), big.NewInt(18), nil)
	keys := []string{strings.Repeat("0", 63) + "1", strings.Repeat("0", 63) + "2", strings.Repeat("0", 63) + "3"}
	senders := []common.Address{}
	codes := [][]byte{nil, {0}, append(common.FromHex("0xef0100"), target.Bytes()...)}
	for i, keyText := range keys {
		key := mustParseKey(keyText)
		address := crypto.PubkeyToAddress(key.PublicKey)
		senders = append(senders, address)
		g.genesis.Alloc[address] = types.Account{Nonce: 10, Balance: new(big.Int).Set(balance), Code: codes[i]}
	}
	g.genesis.Alloc[target] = types.Account{Balance: new(big.Int), Code: marker}
	if err := g.run(); err != nil {
		t.Fatal(err)
	}
	headBytes, err := os.ReadFile(filepath.Join(chainDir, "headblock.json"))
	if err != nil {
		t.Fatal(err)
	}
	var head map[string]any
	if err := json.Unmarshal(headBytes, &head); err != nil {
		t.Fatal(err)
	}
	baseFee, err := hexutil.DecodeBig(head["baseFeePerGas"].(string))
	if err != nil || baseFee.Sign() <= 0 {
		t.Fatal("positive base fee required", err)
	}
	price := new(big.Int).Add(baseFee, big.NewInt(1))
	chainID := g.genesis.Config.ChainID
	cases := []map[string]any{}
	controls := map[string]any{}
	add := func(name, method string, params []any, fields map[string]any) {
		c := map[string]any{"name": name, "request": map[string]any{"jsonrpc": "2.0", "id": 1, "method": method, "params": params}}
		for k, v := range fields {
			c[k] = v
		}
		cases = append(cases, c)
	}
	control := func(name, method string, params []any, expected any) {
		name = "_control/" + name
		add(name, method, params, nil)
		controls[name] = expected
	}
	control("chain-id", "eth_chainId", []any{}, hexutil.EncodeBig(chainID))
	for i, sender := range senders {
		label := []string{"sender", "code-sender", "delegated-sender"}[i]
		params := []any{sender.Hex(), "latest"}
		control(label+"-nonce", "eth_getTransactionCount", params, "0xa")
		control(label+"-balance", "eth_getBalance", params, hexutil.EncodeBig(balance))
		control(label+"-code", "eth_getCode", params, hexutil.Encode(codes[i]))
	}
	control("marker-code", "eth_getCode", []any{target.Hex(), "latest"}, hexutil.Encode(marker))
	control("marker-storage", "eth_getStorageAt", []any{target.Hex(), "0x0", "latest"}, "0x"+strings.Repeat("0", 64))
	type probe struct {
		name, reason        string
		key                 int
		nonce, gas          uint64
		value, price, chain *big.Int
		create              bool
		reject              bool
	}
	probes := []probe{
		{name: "valid", nonce: 10, gas: 100000},
		{name: "execution-oog-valid", nonce: 10, gas: 21000},
		{name: "delegated-sender-valid", key: 2, nonce: 10, gas: 100000},
		{name: "nonce-low", nonce: 9, gas: 100000, reject: true, reason: "nonce below selected state"},
		{name: "nonce-high", nonce: 11, gas: 100000, reject: true, reason: "nonce above selected state"},
		{name: "wrong-chain", nonce: 10, gas: 100000, chain: new(big.Int).Add(chainID, big.NewInt(1)), reject: true, reason: "wrong chain identity"},
		{name: "funds-value", nonce: 10, gas: 100000, value: new(big.Int).Add(balance, big.NewInt(1)), reject: true, reason: "insufficient balance for value alone"},
		{name: "funds-gas", nonce: 10, gas: 100000, value: balance, reject: true, reason: "value is affordable but upfront gas plus value is not"},
		{name: "intrinsic-gas", nonce: 10, gas: 20999, reject: true, reason: "gas limit below 21000 intrinsic gas"},
		{name: "below-basefee", nonce: 10, gas: 100000, price: new(big.Int).Sub(baseFee, big.NewInt(1)), reject: true, reason: "gas price below selected block base fee"},
		{name: "code-sender", key: 1, nonce: 10, gas: 100000, reject: true, reason: "EIP-3607 ordinary-code sender (not delegation)"},
		{name: "create-valid", nonce: 10, gas: 100000, create: true},
		{name: "create-nonce-low", nonce: 9, gas: 100000, create: true, reject: true, reason: "creation nonce below selected state"},
		{name: "create-nonce-high", nonce: 11, gas: 100000, create: true, reject: true, reason: "creation nonce above selected state"},
	}
	for _, p := range probes {
		to := &target
		var data []byte
		if p.create {
			to = nil
			data = common.FromHex("0x3060005260206000f3")
		} // Return ADDRESS as deployed bytes.
		if p.price == nil {
			p.price = price
		}
		if p.value == nil {
			p.value = big.NewInt(1)
		}
		if p.chain == nil {
			p.chain = chainID
		}
		tx := types.NewTx(&types.LegacyTx{Nonce: p.nonce, Gas: p.gas, GasPrice: p.price, To: to, Value: p.value, Data: data})
		tx, err = types.SignTx(tx, types.NewEIP155Signer(p.chain), mustParseKey(keys[p.key]))
		if err != nil {
			t.Fatal(err)
		}
		recovered, err := types.Sender(types.NewEIP155Signer(p.chain), tx)
		if err != nil || recovered != senders[p.key] {
			t.Fatal("signature check failed", err)
		}
		raw, err := tx.MarshalBinary()
		if err != nil {
			t.Fatal(err)
		}
		for _, selection := range [][]string{{"trace", "stateDiff", "vmTrace"}, {"trace"}, {"stateDiff"}, {"vmTrace"}} {
			suffix := selection[0]
			if len(selection) == 3 {
				suffix = "all"
			}
			validation := "execute"
			if p.reject {
				validation = "reject"
			}
			fields := map[string]any{"validation": validation, "reason": p.reason, "sender": senders[p.key].Hex(), "signed_nonce": p.nonce, "state_nonce": 10,
				"signed_fields":   map[string]any{"chainId": hexutil.EncodeBig(p.chain), "gas": hexutil.EncodeUint64(p.gas), "gasPrice": hexutil.EncodeBig(p.price), "value": hexutil.EncodeBig(p.value)},
				"expected_output": "0x" + strings.Repeat("0", 62) + "2a", "marker": target.Hex()}
			if p.name == "execution-oog-valid" {
				fields["expected_output"] = "0x"
				fields["expected_execution_error"] = true
			}
			if p.create {
				fields["signed_create_address"] = crypto.CreateAddress(senders[p.key], p.nonce).Hex()
				fields["state_create_address"] = crypto.CreateAddress(senders[p.key], 10).Hex()
				fields["expected_output"] = "0x" + strings.Repeat("0", 24) + strings.ToLower(crypto.CreateAddress(senders[p.key], p.nonce).Hex()[2:])
			}
			add("raw-validation-"+p.name+"-"+suffix, "trace_rawTransaction", []any{hexutil.Encode(raw), selection}, fields)
		}
	}
	corpus := map[string]any{"description": "One-invalid-condition signed transactions on a Prague chain; valid marker and delegation controls; CREATE returns ADDRESS. Public test keys 1, 2 and 3.", "controls": controls, "base_fee": hexutil.EncodeBig(baseFee), "cases": cases}
	encoded, err := json.MarshalIndent(corpus, "", "  ")
	if err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(output, "corpus.json"), append(encoded, '\n'), 0644); err != nil {
		t.Fatal(err)
	}
}
