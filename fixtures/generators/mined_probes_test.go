package main

// Copy into cmd/hivechain at the pinned Hive revision and run TestMinedProbes.
// All keys below are intentionally public fixture keys, never wallet keys.
//
// Each block holds one probe family, so block traces and filters stay small:
//
//	1  type-3 transfer with one blob to an absent recipient
//	2  EIP-4788 read at the block's own TIMESTAMP; EIP-2935 read of the parent hash
//	3  top-level CREATE whose initcode reverts; factory CREATE of the same initcode
//	4  SELFDESTRUCT to self of a funded contract with storage; factory create-then-
//	   destroy-to-self at an absent and at a prefunded address
//	5  SSTORE clears: one uncapped refund, one capped at a fifth of the gas used
//	6  type-4 transaction: replaced, stale, absent-authority and restoring tuples
//
// Expectations are derived separately by scripts/build_mined_probes_fixtures.py;
// this generator only records which transaction plays which role.
import (
	"math/big"
	"os"
	"path/filepath"
	"reflect"
	"strings"
	"testing"
	"unsafe"

	"github.com/ethereum/go-ethereum/common"
	"github.com/ethereum/go-ethereum/common/hexutil"
	"github.com/ethereum/go-ethereum/core"
	"github.com/ethereum/go-ethereum/core/state"
	"github.com/ethereum/go-ethereum/core/types"
	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/crypto/kzg4844"
	"github.com/ethereum/go-ethereum/params"
	"github.com/holiman/uint256"
)

var (
	minedBeaconReader  = common.HexToAddress("0x4788")
	minedHistoryReader = common.HexToAddress("0x2935")
	minedFactory       = common.HexToAddress("0xfac0")
	minedDestruct      = common.HexToAddress("0xde57")
	minedRefund        = common.HexToAddress("0x5501")
	minedRefundCapped  = common.HexToAddress("0x5502")
	minedDelegateA     = common.HexToAddress("0x7702a")
	minedDelegateB     = common.HexToAddress("0x7702b")
	minedBlobRecipient = common.HexToAddress("0xb10b")
)

// readerCode stores STATICCALL(target, word) success in slot 1 and the returned word
// in slot 0, then returns that word. prefix leaves the input word on the stack.
func readerCode(prefix string, target common.Address) []byte {
	return common.FromHex(prefix + "5f52" + "60205f60205f73" + strings.ToLower(target.Hex()[2:]) + "5afa" +
		"600155" + "5f515f55" + "60205ff3")
}

// preApplyBeaconRoot performs the block's EIP-4788 storage writes before its transactions.
// The pinned chain maker runs that system call after the block callback, whereas block
// import (like every client) runs it before the first transaction. The later system call
// rewrites the same two slots, and the import in g.run validates the resulting block.
func preApplyBeaconRoot(gen *core.BlockGen) {
	fields := reflect.ValueOf(gen).Elem()
	field := func(name string) any {
		f := fields.FieldByName(name)
		return reflect.NewAt(f.Type(), unsafe.Pointer(f.UnsafeAddr())).Elem().Interface()
	}
	statedb, header := field("statedb").(*state.StateDB), field("header").(*types.Header)
	const ring = 8191 // EIP-4788 HISTORY_BUFFER_LENGTH
	slot := header.Time % ring
	statedb.SetState(params.BeaconRootsAddress, common.BigToHash(new(big.Int).SetUint64(slot)), common.BigToHash(new(big.Int).SetUint64(header.Time)))
	statedb.SetState(params.BeaconRootsAddress, common.BigToHash(new(big.Int).SetUint64(slot+ring)), *header.ParentBeaconRoot)
}

type minedProbes struct {
	keys  []string
	info  map[string]any
	plans map[uint64]func(*genBlockContext, *minedProbes)
	done  map[uint64]bool
}

func (m *minedProbes) apply(ctx *genBlockContext) bool {
	plan, ok := m.plans[ctx.NumberU64()]
	if !ok || m.done[ctx.NumberU64()] {
		return false
	}
	plan(ctx, m)
	m.done[ctx.NumberU64()] = true
	return true
}

func (m *minedProbes) txInfo() any { return m.info }

func (m *minedProbes) account(i int) *genAccount {
	key := mustParseKey(m.keys[i])
	return &genAccount{key: key, addr: crypto.PubkeyToAddress(key.PublicKey)}
}

// send signs a dynamic-fee transaction from key 1 with a 2 gwei tip and records its role.
func (m *minedProbes) send(ctx *genBlockContext, role string, to *common.Address, value int64, gas uint64, data []byte) {
	sender := m.account(0)
	tip := big.NewInt(2 * params.GWei)
	tx := ctx.AddNewTx(sender, &types.DynamicFeeTx{
		ChainID: ctx.ChainConfig().ChainID, Nonce: ctx.AccountNonce(sender.addr), GasTipCap: tip,
		GasFeeCap: new(big.Int).Add(new(big.Int).Mul(ctx.block.BaseFee(), big.NewInt(2)), tip),
		Gas:       gas, To: to, Value: big.NewInt(value), Data: data,
	})
	m.record(ctx, role, tx)
}

func (m *minedProbes) record(ctx *genBlockContext, role string, tx *types.Transaction) {
	m.info[role] = map[string]any{"txhash": tx.Hash(), "block": hexutil.Uint64(ctx.NumberU64()), "indexInBlock": ctx.TxCount() - 1}
}

func (m *minedProbes) authorize(ctx *genBlockContext, key int, target common.Address, nonce uint64) types.SetCodeAuthorization {
	auth, err := types.SignSetCode(m.account(key).key, types.SetCodeAuthorization{
		ChainID: *uint256.MustFromBig(ctx.ChainConfig().ChainID), Address: target, Nonce: nonce,
	})
	if err != nil {
		panic(err)
	}
	return auth
}

var minedPlans = map[uint64]func(*genBlockContext, *minedProbes){
	1: func(ctx *genBlockContext, m *minedProbes) {
		blob := kzg4844.Blob{0x01}
		commitment, _ := kzg4844.BlobToCommitment(&blob)
		proof, _ := kzg4844.ComputeBlobProof(&blob, commitment)
		sidecar := &types.BlobTxSidecar{Blobs: []kzg4844.Blob{blob}, Commitments: []kzg4844.Commitment{commitment}, Proofs: []kzg4844.Proof{proof}}
		sender := m.account(0)
		tip := uint256.NewInt(2 * params.GWei)
		tx := ctx.AddNewTx(sender, &types.BlobTx{
			ChainID: uint256.MustFromBig(ctx.ChainConfig().ChainID), Nonce: ctx.AccountNonce(sender.addr), GasTipCap: tip,
			GasFeeCap: new(uint256.Int).Add(new(uint256.Int).Mul(uint256.MustFromBig(ctx.block.BaseFee()), uint256.NewInt(2)), tip),
			Gas:       21000, To: minedBlobRecipient, Value: uint256.NewInt(7),
			BlobFeeCap: uint256.NewInt(params.BlobTxBlobGasPerBlob), BlobHashes: sidecar.BlobHashes(), Sidecar: sidecar,
		})
		m.record(ctx, "blob-transfer", tx)
	},
	2: func(ctx *genBlockContext, m *minedProbes) {
		preApplyBeaconRoot(ctx.block)
		m.send(ctx, "beacon-root-read", &minedBeaconReader, 0, 200000, nil)
		m.send(ctx, "history-read", &minedHistoryReader, 0, 200000, nil)
	},
	3: func(ctx *genBlockContext, m *minedProbes) {
		revert := common.FromHex("0x63deadbeef5f526004601cfd") // REVERT with 0xdeadbeef.
		m.send(ctx, "create-revert", nil, 0, 200000, revert)
		m.send(ctx, "factory-create-revert", &minedFactory, 0, 200000, revert)
	},
	4: func(ctx *genBlockContext, m *minedProbes) {
		destroySelf := common.FromHex("0x30ff") // SELFDESTRUCT(ADDRESS).
		m.send(ctx, "selfdestruct-self", &minedDestruct, 0, 200000, nil)
		m.send(ctx, "create-destroy-absent", &minedFactory, 0x100, 200000, destroySelf)
		m.send(ctx, "create-destroy-prefunded", &minedFactory, 0x100, 200000, destroySelf)
	},
	5: func(ctx *genBlockContext, m *minedProbes) {
		m.send(ctx, "refund-clear", &minedRefund, 0, 200000, nil)
		m.send(ctx, "refund-capped", &minedRefundCapped, 0, 200000, nil)
	},
	6: func(ctx *genBlockContext, m *minedProbes) {
		existing, absent, restoring := m.account(1).addr, m.account(2).addr, m.account(3).addr
		auths := []types.SetCodeAuthorization{
			m.authorize(ctx, 1, minedDelegateA, 5), // applied
			m.authorize(ctx, 1, minedDelegateB, 6), // applied, replaces A
			m.authorize(ctx, 1, minedDelegateA, 5), // stale nonce: skipped
			m.authorize(ctx, 2, minedDelegateA, 0), // absent authority: applied, born
			m.authorize(ctx, 3, minedDelegateB, 3), // applied, delegated A -> B
			m.authorize(ctx, 3, minedDelegateA, 4), // applied, back to A: no net code change
		}
		sender := m.account(0)
		tip := uint256.NewInt(2 * params.GWei)
		tx := ctx.AddNewTx(sender, &types.SetCodeTx{
			ChainID: uint256.MustFromBig(ctx.ChainConfig().ChainID), Nonce: ctx.AccountNonce(sender.addr), GasTipCap: tip,
			GasFeeCap: new(uint256.Int).Add(new(uint256.Int).Mul(uint256.MustFromBig(ctx.block.BaseFee()), uint256.NewInt(2)), tip),
			Gas:       400000, To: existing, AuthList: auths,
		})
		m.record(ctx, "authorizations", tx)
		m.info["authorities"] = map[string]any{"existing": existing, "absent": absent, "restoring": restoring}
	},
}

func TestMinedProbes(t *testing.T) {
	output := os.Getenv("TRACE_MINED_OUTPUT")
	if output == "" {
		t.Fatal("set TRACE_MINED_OUTPUT to a fresh output directory")
	}
	if err := os.Mkdir(output, 0755); err != nil {
		t.Fatal(err)
	}
	const name = "trace-mined-probes"
	disabled := []string{}
	for mod := range modRegistry {
		disabled = append(disabled, mod)
	}
	keys := []string{strings.Repeat("0", 63) + "1", strings.Repeat("0", 63) + "2", strings.Repeat("0", 63) + "3", strings.Repeat("0", 63) + "4"}
	probes := &minedProbes{keys: keys, info: map[string]any{}, plans: minedPlans, done: map[uint64]bool{}}
	modRegistry[name] = func() blockModifier { return probes }
	defer delete(modRegistry, name)
	cfg, err := (generatorConfig{chainLength: len(minedPlans), txCount: 1, merged: true, lastFork: "prague", disabledMods: disabled,
		outputDir: output, outputs: []string{"genesis", "chain", "headblock", "headstate", "forkenv", "headfcu", "txinfo"}}).withDefaults()
	if err != nil {
		t.Fatal(err)
	}
	g := newGenerator(cfg)
	eth := new(big.Int).Exp(big.NewInt(10), big.NewInt(18), nil)
	hash := common.HexToHash
	delegation := func(target common.Address) []byte { return append(common.FromHex("0xef0100"), target.Bytes()...) }
	g.genesis.Alloc[probes.account(0).addr] = types.Account{Balance: new(big.Int).Mul(eth, big.NewInt(10))}
	g.genesis.Alloc[probes.account(1).addr] = types.Account{Balance: eth, Nonce: 5}
	g.genesis.Alloc[probes.account(3).addr] = types.Account{Balance: eth, Nonce: 3, Code: delegation(minedDelegateA)}
	g.genesis.Alloc[minedBeaconReader] = types.Account{Nonce: 1, Balance: new(big.Int), Code: readerCode("42", params.BeaconRootsAddress)}
	// NUMBER - 1: the parent hash the block's pre-transaction EIP-2935 call stores.
	g.genesis.Alloc[minedHistoryReader] = types.Account{Nonce: 1, Balance: new(big.Int), Code: readerCode("60014303", params.HistoryStorageAddress)}
	// CREATE(CALLVALUE, calldata) and return the created address word.
	g.genesis.Alloc[minedFactory] = types.Account{Nonce: 1, Balance: new(big.Int), Code: common.FromHex("0x365f5f37365f34f05f5260205ff3")}
	g.genesis.Alloc[minedDestruct] = types.Account{Nonce: 1, Balance: big.NewInt(1000), Code: common.FromHex("0x30ff"),
		Storage: map[common.Hash]common.Hash{hash("0x1"): hash("0x2a")}}
	g.genesis.Alloc[minedRefund] = types.Account{Nonce: 1, Balance: new(big.Int), Code: common.FromHex("0x5f5f5500"),
		Storage: map[common.Hash]common.Hash{hash("0x0"): hash("0x2a")}}
	g.genesis.Alloc[minedRefundCapped] = types.Account{Nonce: 1, Balance: new(big.Int), Code: common.FromHex("0x5f5f555f60015500"),
		Storage: map[common.Hash]common.Hash{hash("0x0"): hash("0x2a"), hash("0x1"): hash("0x2b")}}
	g.genesis.Alloc[minedDelegateA] = types.Account{Nonce: 1, Balance: new(big.Int), Code: []byte{0}}
	g.genesis.Alloc[minedDelegateB] = types.Account{Nonce: 1, Balance: new(big.Int), Code: []byte{0}}
	// The factory's third CREATE (nonce 3) lands on an address that already holds wei.
	g.genesis.Alloc[crypto.CreateAddress(minedFactory, 3)] = types.Account{Balance: big.NewInt(5000)}
	if err := g.run(); err != nil {
		t.Fatal(err)
	}
	for block := range minedPlans {
		if !probes.done[block] {
			t.Fatalf("block %d probes did not run", block)
		}
	}
	if _, err := os.Stat(filepath.Join(output, "chain.rlp")); err != nil {
		t.Fatal(err)
	}
}
