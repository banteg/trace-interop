# H13: signed transaction validation

The proposal is to validate the supplied signed transaction for execution against the
selected state and fork. This includes both nonce directions, chain identity, signature,
funds for value and upfront gas, intrinsic gas, fee validity and sender-code restrictions
with the EIP-7702 exception. Local pool replacement, already-known and minimum-tip rules
are outside this contract. A valid transaction that REVERTs or exhausts execution gas
still returns a trace. The proposed `-32003` validation code is scored separately from
rejection itself; malformed bytes/parameters use `-32602`.

This tightens legacy diagnostic behavior. Signed pre-broadcast inspection, pool-transaction
inspection and experimentation against another state are all legitimate uses; we have
no usage evidence establishing which dominates. Permissive execution needs explicit
semantics for nonce, balances and CREATE, rather than a successful-looking result whose
relation to the selected state is unclear. An ordinary block selector identifies block
post-state; it does not reconstruct the pre-state of a transaction inside that block.
Use transaction replay for that purpose. H12's portable two-argument/latest baseline is
separate from this policy.

## What the reproducers establish

The [capture](../evidence/2026-09-23/raw-validation-native/summary.json) has 560 responses:
56 signed requests and 14 controls per build, across eight digest-pinned native builds.
Every launch, head/state and independent setup check passed. This uses the existing
September 21 client lock, not clients rebuilt with the September 22 PR fixes. Release
and development builds show the same validation categories below for the all-tracers
selection; individual selections are also retained, including unrelated output-field
bugs. These results concern trace RPC simulation, not block consensus validation.

| Probe | Besu | Erigon | Nethermind | Reth |
|---|---|---|---|---|
| Valid EOA | Executes | Executes | Executes | Executes |
| Valid delegated sender | Executes | Executes | Executes | Executes |
| Valid transaction, execution OOG | Trace halt | Trace halt | Trace halt | Trace halt |
| Nonce low / high | Empty result | Executes | Executes | Rejects `-32000` |
| Wrong chain ID | Executes | Rejects `-32000` | Malformed JSON | Rejects `-32000` |
| Value exceeds balance | Empty result | Executes | Malformed JSON | Rejects `-32003` |
| Value affordable, upfront gas unaffordable | Empty result | Executes | Malformed JSON | Rejects `-32003` |
| Intrinsic gas short by one | Empty result | Rejects `-32000` | Malformed JSON | Rejects `-32000` |
| Gas price below base fee | Empty result | Rejects `-32000` | Malformed JSON | Rejects `-32000` |
| Ordinary code at sender (EIP-3607) | Executes | Executes | Executes | Rejects `-32003` |
| CREATE with low / high nonce | Empty result | State-nonce address | State-nonce address | Rejects `-32000` |

“Executes” means the target returns word `42`, records the expected slot-0 write and
has VM operations in the all-tracers response. Merely receiving a `result` envelope
does not meet that standard. Besu's empty results have output `0x`, zero gas used,
null stateDiff and no VM operations despite a successful-looking root frame. They
show missing validation error reporting, not successful execution or proof that all
validation was skipped. Nethermind's malformed responses do not establish execution.

The CREATE constructor returns its own ADDRESS. For signed nonces 9 and 11, Erigon and
Nethermind both execute at `0x00de48310d77a4d56aa400248b0b1613508f5b73`, derived from state
nonce 10. Output bytes, the returned root address and newly created code in stateDiff
agree. The independently computed signed-nonce addresses differ. This establishes the
observable execution semantics; it does not claim either client mutated signed bytes.
Besu's empty CREATE envelopes name the signed-nonce address without executing initcode.

Erigon executes a value transfer of `1000000000000000001` wei from a sender independently
verified to have `1000000000000000000` wei. The target balance and marker storage change,
while sender balance is reported unchanged. It also executes when value alone consumes
the balance, leaving nothing for upfront gas. This directly demonstrates simulation
beyond the selected balance. The wire evidence does not identify the internal mechanism.
Even the valid control's Erigon sender delta excludes gas while the beneficiary gains
a tip; gas-accounting fidelity needs a separate follow-up, not an inference about pool
admission.

## Reproduction and controls

The [corpus](../fixtures/corpora/raw-validation.json) stores the exact signed bytes,
expected sender, nonce, signed fields and both CREATE addresses. A transaction-free,
two-block Prague chain fixes each sender nonce at 10 and balance at one ETH. Public
fixture keys 1, 2 and 3 control an EOA, an ordinary-code sender (`0x00`) and a valid
EIP-7702 delegation sender. Target `0x0000000000000000000000000000000000001002`
has code `0x602a600055602a60005260206000f3`: store 42, return 42. Each probe runs
independently against unchanged latest state with all tracers, trace-only, stateDiff-only
and vmTrace-only selections.

Independent RPC controls check chain ID, sender nonces/balances/code, positive base fee,
and target code/zero storage. The 21,000-gas control is intrinsically valid but halts on
its first opcode; the 20,999-gas negative must fail before execution. The delegated
sender protects against incorrectly rejecting every code-bearing sender.

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --corpus raw-validation --output evidence/local/raw-validation
```

To regenerate the chain, copy `fixtures/generators/h13_test.go` into `cmd/hivechain/`
in ethereum/hive at `43ea47bef5761351e3da7b726050ea80ab362c52`, then run:

```sh
TRACE_H13_OUTPUT=/fresh/output GOTOOLCHAIN=go1.26.1 \
  go test ./cmd/hivechain -run '^TestH13Fixtures$' -count=1 -v
```

The output directory must not already exist. Frozen artifacts and checksums are the
reproduction inputs. This corpus does not exhaust typed-transaction fee relationships,
blob rules, every signature constraint, fork transitions or local pool policies. The
corpus does not cover the experimental Geth fork; its evidence is evaluated separately.

## Client agreement

[Erigon supports strict execution validation](https://github.com/ethereum/execution-apis/issues/890#issuecomment-5784143408),
including balance and EIP-3607 checks. The converged status records agreement on that
direction. Error-code mapping and compatibility migration remain open, and the measured
implementations are not harmonized. Erigon describes OpenEthereum's permissive nonce
and balance behavior; OpenEthereum was not independently measured in this corpus.
