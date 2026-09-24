# Simulation review: trace_call / trace_callMany / trace_rawTransaction

Scope: H11, H12, H13, H14, H15 (request/fee side), H16 (request side), H25, H31, H32 (simulation block selection).
Spec read from the pinned execution-apis b979aefe; eth/debug siblings from execution-apis e38fc96c.
Geth upstream semantics from the go-ethereum `feat/trace` fork fa8ecb92 (upstream files only: `internal/ethapi/*`, `eth/tracers/api.go`,
`core/state_transition.go`; the draft trace impl is `eth/tracers/trace_namespace.go`, `trace_types.go`).

Legend: confidence H/M/L; severity **spec** (would change the spec), **verdict** (would change a client verdict),
**cosmetic**.

---

## Ranked summary

| Rank | § | Finding | Kind | Conf | Severity |
|---|---|---|---|---|---|
| 1 | §1 | H15 leaves omitted/incomplete fee defaults "open", but all 9 tested `eth_call` builds agree on omitted → zero-fee (GASPRICE 0, BASEFEE 0), and eth_simulateV1's spec already states fee defaults = 0. The harness masks Besu/Erigon trace_call≠eth_call divergence as "observation". | A + B | H | spec + verdict |
| 2 | §12 | **Erigon trace_call silently drops `input`** (TraceCallParam has only `data`), plus `nonce`, `chainId`, `type`, `blobVersionedHashes`, `authorizationList`. No corpus case ever sends `input` or any of those fields, so this is invisible. | C | H | verdict (new case) |
| 3 | §2 | `first_invalid` treats `maxFeePerGas=0, maxPriorityFeePerGas>0` as only a priority violation; it is also a base-fee violation. Reth is marked "Differs" for a correct rejection (24 case pages × 2 Reth builds = 48 false checks). | B | H | verdict |
| 4 | §3 | Error codes: execution-apis already has two conventions for exactly these failures — eth_simulateV1 `-38010..-38025` (implemented by Geth, Erigon, Nethermind, Reth) and the #650 error-group catalog (`1/2/800/804/806/809/-32003`) that eth_sendRawTransaction uses. The draft invents a single `-32003` for raw and specifies **no** code at all for unsigned-call fee/funding rejections. | A | H | spec |
| 5 | §13 | "Unknown fields MUST be ignored" + "standard fields when supported" lets a client that lacks a *known* field (7702 auths, blob hashes, `input`) silently execute a different transaction. Known schema fields must be honoured or rejected (-32602). | A | H | spec |
| 6 | §4 | trace_callMany validation failure semantics are unspecified (whole-request error vs per-item), yet the harness asserts whole-request rejection. Parity and eth_simulateV1 both fail the whole request; spec should say so and require the item index. No batch gas budget / item limit is specified. | A | H | spec |
| 7 | §14 | Overrides are already accepted by 3/4 clients on trace_call but in incompatible positions/shapes (Reth p4 StateOverride + p5 BlockOverrides; Nethermind p4 StateOverride; Erigon p4 geth-style `{stateOverrides, blockOverrides}` config). A Reth-style request to Erigon is silently ignored. "Outside profile" is not neutral; reserve positions. | A | H | spec |
| 8 | §5 | Block selector for trace_call/callMany is `BlockNumberOrTag`; Parity accepted EIP-1898 hash objects, and eth_call/eth_simulateV1 use `BlockNumberOrTagOrHash`. | A | H | spec |
| 9 | §15 | Besu trace_call strictly validates a supplied nonce (rejects ≠ state nonce) while Besu eth_call allows future nonces; Geth/Reth/Nethermind/Erigon/Parity ignore the nonce. | C | H | verdict (new case) |
| 10 | §7 | H15 recommendation omits Parity's balance top-up (`transact_virtual`) as a compatibility cost of "enforce funding"; also omits the BLOBBASEFEE half of geth's rule. | A | H | spec (wording) |
| 11 | §8 | TraceCall schema drift from GenericTransaction/GenericCallTransaction: `gas` is uint256 (should be uint64), `nonce` semantics under-specified (supplied nonce is ignored by eth_call/Parity/Reth/Geth draft), stale "without rewriting BASEFEE" text in trace_call description. | A | H | spec |
| 12 | §16 | Erigon trace_callMany at a historical block reads state at txIndex 0 of block N+1 while trace_call reads at −1 (post-N); likely exposes N+1's pre-block system-call writes (EIP-4788/2935) to callMany only. | C | M-L | verdict (probe needed) |
| 13 | §9 | Missed H13 coverage: unprotected pre-EIP-155 legacy tx (consensus-valid, RPC-policy-rejected by geth send), type-3 network vs canonical encoding, type-4 tx with empty/invalid auths, EIP-7825 gas cap at Osaka. | C | M | spec + coverage |
| 14 | §10 | Missed H16 callMany isolation probes: transient storage reset, EIP-6780 "same-tx" selfdestruct across items, warm-set reset. | C | M | coverage |
| 15 | §6 | H31 ledger claim stale: Reth main now defaults omitted trace_callMany to latest (`d8d704cf`, #27410, 2026-09-24). | D | H | cosmetic (ledger text / migration note) |
| 16 | §11 | Minor harness: `assess()` rejection classifier lacks Besu's "Upfront cost exceeds account balance" wording that `assess_compatibility()` recognises; code whitelist `[-32000,-32003,-32602]` would block clients that adopt simulate/error-group codes. | B | M | verdict (latent) |

Checked and found correct (brief): H15 oracle arithmetic and BASEFEE rule for all scored families (§B1);
H11 (accept `[]`); H14 (-32602 for malformed); H32 rejecting pending for simulations (matches Parity and
upstream debug_traceCall); H12 two-argument baseline.

---
## 1. H15 fee defaults are not actually open; the harness hides a real trace_call≠eth_call divergence (A+B, H, spec+verdict)

**What geth does (the rule H15 claims to align with).** `TransactionArgs.CallDefaults`
(`geth-trace/internal/ethapi/transaction_args.go:401-461`) defaults a missing `maxFeePerGas` and a missing
`maxPriorityFeePerGas` to **zero** whenever the block has a base fee (lines 447-455); `ToMessage` (467-495) then
computes `gasPrice = min(tip + header.BaseFee, cap)` unless both are zero (486-493). `applyMessage` zeroes
`blockContext.BaseFee` iff `msg.GasPrice.Sign()==0` (`internal/ethapi/api.go:798-803`); debug_traceCall does the
same (`eth/tracers/api.go:948-960`). So in geth, "omitted" is not a separate category: omitted ≡ zero.

**execution-apis already specifies this for the sibling simulation method.** `GenericCallTransaction`
(`execution-apis/src/schemas/execute.yaml:241-300`, used by eth_simulateV1) documents `gasPrice`,
`maxPriorityFeePerGas`, `maxFeePerGas` each "Default: 0".

**Our own paired capture shows eth_call is unanimous.** From
`evidence/2026-09-24/h15-call-compat/fee-compat/observations.json` (words GASPRICE/BASEFEE decoded):

| Family | eth_call, 9/9 builds | trace_call (none selection) |
|---|---|---|
| defaults-omitted | GP 0, BF 0, no debit — **all 9** | Besu GP=B BF=B **debit**; Erigon dev GP=B BF=B; Geth draft/Neth dev GP 0 BF B; Reth GP 0 BF 0 |
| defaults-cap-only-zero | GP 0, BF 0 — **all 9** | Besu -32603; Erigon dev GP=B; Geth/Neth BF=B; Reth 0/0 |
| defaults-cap-only-positive (cap 2B) | GP=B BF=B — all 9 (Reth no debit) | same as eth_call except Erigon dev no debit |
| defaults-tip-only-zero | GP 0 BF 0 — 7/9; Reth prices at B | Besu -32603; Erigon GP=B; Reth GP=B |
| defaults-tip-only-positive | 7/9 reject (Geth/Erigon: tip>cap; Besu/Neth: base fee); Reth executes at B+1 | similar |

So for the first three families the eth_call answer is unanimous and matches geth's documented rule; only
`tip-only-*` shows a Reth outlier. H15's own rationale — "adding tracing should not change the execution of the
same call" — therefore already decides the defaults. Keeping them "Policy open" lets Besu (which *charges*
B·gas on an omitted-fee trace_call while its eth_call is free) and Erigon escape both the policy check and
the method-consistency check.

**Harness defect.** `fee_policy.assess_compatibility` sets `status='observation'` whenever
`fee_policy.admission == 'observe'` (`trace_interop/fee_policy.py:236-238`), **even when the same client's
eth_call and trace_call outputs differ**. The paired check is policy-neutral ("same observable output or
same rejection class"), so it should still produce `matches`/`change_needed` for defaults families; only
the independent-policy check (`assess`, line 132-134) needs the "open" carve-out. As written, H15's
consistency principle is not measured exactly where Besu/Erigon violate it.

**Recommendation.** Spec: "Omitted fee fields default as eth_call/eth_simulateV1: missing gasPrice,
maxFeePerGas, maxPriorityFeePerGas are 0; the zero-fee rule applies to the *effective* price after defaulting
(GASPRICE 0 ⇒ BASEFEE 0)." Promote defaults-omitted, cap-only-zero, cap-only-positive, tip-only-zero to
`accept` families (expected: free, free, price B, free) and tip-only-positive to `reject: priority`
(Reth's eth_call outlier can be noted). At minimum, let `assess_compatibility` score defaults families.

## 2. `first_invalid` misses the base-fee violation when maxFeePerGas = 0 and tip > 0 (B, H, verdict)

`trace_interop/fee_policy.py:98-103`:
```python
if tip>cap:            return index, 'priority'
if 0<cap<base:         return index, 'base_fee'
```
For `typed-zero-cap-positive-tip` (cap 0, tip 1) the request violates **both** constraints: the zero-fee
exemption requires cap **and** tip to be zero (geth `core/state_transition.go:576`, `skipCheck := NoBaseFee &&
GasFeeCap==0 && GasTipCap==0`), so the cap-vs-base check applies and 0 < B fails too. The oracle encodes
geth's *check order* rather than the *set of violated constraints*; the spec does not (and should not) mandate an
order. Result: Reth (`"max fee per gas less than block base fee"`) gets "Differs … Expected call 0: priority;
observed base_fee" on all 24 case pages (16 fee-policy + 8 fee-compat) × 2 Reth builds = 48 false
`change_needed` checks (`grep -rh "Expected call 0: priority; observed" reports/cases` → 48 base_fee).
Nethermind (`maxFeePerGas (0) < maxPriorityFeePerGas (1)`), Erigon and Geth happen to report tip-first and pass.

Fix: return the set of violated reasons, `{'priority'} ∪ ({'base_fee'} if cap<base and not (cap==0 and tip==0))`,
and accept any member. The same applies to `first_invalid` being reused for fee-compat.

(Other rejection families checked: `typed-tip-over-cap` cap=B, tip=B+1 → only priority; `typed-below-base-positive-tip`
cap=B−1, tip=1 → only base_fee; funding families → only funds. These are single-violation and fine.)

## 3. Error codes: reuse an existing execution-apis convention instead of a bespoke single -32003 (A, H, spec)

State of execution-apis (working tree e38fc96c):
- **eth_simulateV1** (`src/eth/execute.yaml:127-166`): `-38010` nonce too low, `-38011` nonce too high,
  `-38012` base fee too low, `-38013` intrinsic gas, `-38014` insufficient funds, `-38015` block gas limit,
  `-38024` sender not EOA, `-38025` init-code size, `-38026` client limit; `-32602` invalid params.
  Conformance vectors (`tests/eth_simulateV1/ethSimulate-gas-fees-and-value-error-38014.io`, `…-38012.io`,
  `…-instrict-gas-38013.io`, `…-transaction-too-low-nonce-38010.io`) pin them. Implemented by Geth
  (`internal/ethapi/errors.go:103-160`, `txValidationError`), Erigon (`rpc/errors.go:39-43`), Nethermind
  (`Nethermind.JsonRpc/ErrorCodes.cs:137-157`), Reth (`rpc-eth-types/src/simulate.rs:131-136`). Besu has no
  -380xx codes (it uses its own -32004/-32006/-32009, `RpcErrorType.java:160-175`).
- **Error-group catalog** (#650, `46ef7174`, 2026-03-23; `src/error-groups/*.yaml`): ExecutionErrors `1` nonce
  too low, `2` nonce too high; GasErrors `800` intrinsic, `804` tip>cap, `806` fee cap < base fee, `809`
  insufficient funds; NonStandard `-32003` Transaction rejected; TxPool `1001` invalid sender. Currently
  attached only to eth_sendTransaction / eth_sendRawTransaction (`src/eth/submit.yaml:8-13,54-59`).

The draft (`src/trace/methods.yaml:134-168`) lists only `-32003` for trace_rawTransaction and,
for trace_call/trace_callMany (lines 29-37, 80-88), **no code at all** for fee/funding/intrinsic rejections even
though H15 now requires those rejections. H14's own rationale ("distinguish … without text matching") is
undercut: the harness itself has to regex messages to recover the reason (`fee_policy.py:123-126, 199-205`).

Recommendation:
- trace_rawTransaction takes the same bytes as eth_sendRawTransaction → reference the same error groups
  (`JSONRPCStandardErrors`, `JSONRPCNonStandardErrors`, `GasErrors`, `ExecutionErrors`), keeping `-32003` as the
  generic fallback (it is already in that catalog, so the draft is a compatible subset, just less useful).
- trace_call/trace_callMany are unsigned sequential simulations → reuse eth_simulateV1's `-38010..-38026` (four
  of five clients already emit them from shared code paths). Note geth maps tip>cap to `-32602` there
  (`errors.go:131-132`); decide explicitly.
- Whichever is chosen, list it in `errors:` for all three methods. Do not score `-32003` vs a specific code as a
  failure until agreed (harness `rules.py:352-355` currently requires exactly -32003).

## 4. trace_callMany: specify item-validation failure, index reporting and batch limits (A, H, spec)

The spec (`methods.yaml:58-65`) says "Reverted writes roll back; subsequent calls continue" but says nothing about
an item that fails *validation* (fee below base, insufficient funds after earlier items, tip>cap). The harness
nonetheless asserts whole-request rejection and optionally checks the reported index
(`fee_policy.py:115-129`, fixtures `mixed-*-then-invalid`, `sequential-funding`). Precedent is unanimous and
should be written down:
- Parity: `call_many` returns `Result<Vec<_>>`; any item error fails the call (`parity-ethereum/rpc/src/v1/impls/traces.rs:119-145`).
- eth_simulateV1: item validation error fails the whole request even in non-validation mode
  (`geth internal/ethapi/simulate.go:347-352`; vector `ethSimulate-simple-no-funds.io` returns -38014 for call 0).
- Geth draft: `call %d: …` prefix (`trace_namespace.go:84-92`).

Add: "If any item fails validation, return a single error for the request, identify the zero-based item index
(e.g. in `data`), and return no partial results." Putting the index in `error.data` rather than message text
lets the harness drop the `call |txindex ` regex (`fee_policy.py:128`).

Limits: the geth draft caps the item count at `traceFilterResultLimit` (`trace_namespace.go:69-71`) and uses a
batch timeout, while eth_simulateV1 enforces a cumulative RPC-gas budget across calls (`simulate.go:169-196, 365,
452-455`). The spec is silent. Recommend allowing a server total-gas/item limit reported as `-32005` Limit
exceeded (or simulate's `-38026`) and forbidding silent truncation (same rule the draft already uses for filters).
Client behaviour (source, §17): all four fail the whole request on an item error; only Erigon names the
index (`first run for txIndex %d error`, `trace_adhoc.go:1482`); Nethermind builds an index message but the
RPC layer drops it (-32000, `JsonRpcService.cs:621-622`); Besu returns -32603 with no index; Reth propagates
without index. Only Nethermind caps items (1024, `TraceCallManyRequest.cs:12,40-42`). All reuse one header
for every item (no NUMBER/TIMESTAMP increment), matching Parity; H15's per-item reset is consistent.

## 5. Block selector should be BlockNumberOrTagOrHash (A, H, spec)

`trace_call`/`trace_callMany` declare `BlockNumberOrTag` (`methods.yaml:20-24, 73`). But:
- Parity's `BlockNumber` includes `Hash { hash, require_canonical }` parsed from the EIP-1898 object
  (`parity-ethereum/rpc/src/v1/types/block_number.rs:24-31, 96-…`), and `call`/`call_many`/`raw_transaction` map it
  to `BlockId::Hash` (`impls/traces.rs:103, 128, 155`). Dropping it removes an original capability.
- eth_call and eth_simulateV1 use `BlockNumberOrTagOrHash` (`execution-apis/src/eth/execute.yaml:9-12, 117-121`).
  Hash selection is also the only reorg-safe way to pin a simulation (relevant to H32's "one consistent chain view").
Client acceptance (source, see §17): Erigon (`BlockNumberOrHash`), Nethermind (EIP-1898 object,
`Nethermind.Blockchain/Find/BlockParameter.cs:189-205`) and Reth (`BlockId`) accept a hash; Besu rejects it
(`BlockParameter.java:41-73`, `Long.decode`). 3/4 + Parity + eth_call → adopt `BlockNumberOrTagOrHash`.

## 6. H31 Reth claim is stale (D, H, ledger text)

Ledger H31 background: "Pinned Reth code deliberately defaults omitted trace_callMany to BlockId::pending() …
Choosing latest intentionally changes that established Reth default." Current Reth main has
`let at = block_id.unwrap_or_default();` (`crates/rpc/rpc/src/trace.rs:157`) plus test
`trace_call_many_defaults_to_latest` (same file, ~905-942), from commit `d8d704cf7d` "fix(rpc): default
trace_callMany to latest (#27410)", 2026-09-24 (on Reth main). The
recommendation stands; the migration note should say Reth main already converged and only released builds
(≤2.6.0) differ.

## 7. H15 wording gaps vs geth's actual rule and vs Parity (A, H, spec wording)

(a) **Is the oracle exactly geth's rule?** For every family it scores, yes (see §B1): BASEFEE word is
`0 if price == 0 else base` with `price = min(cap, B+tip)` (`fee_policy.py:58-67`), identical to
`msg.GasPrice.Sign()==0` when B>0. The *recommendation text* is narrower than geth in three ways:
- geth's condition is on the effective price **after defaulting** (see §1), not "explicit zero";
- the fee-*validation* skip is a different predicate (`cap==0 && tip==0`, `state_transition.go:576`) from the
  BASEFEE-zeroing predicate (`gasPrice==0`); they differ only for cap=0/tip>0, which is rejected anyway — worth one
  sentence so implementers don't zero BASEFEE and then skip validation;
- **BLOBBASEFEE**: geth independently zeroes it iff `msg.BlobGasFeeCap != nil && == 0`
  (`api.go:804-806`, `tracers/api.go:961-963`), and `CallDefaults` sets the blob cap to 0 when `blobVersionedHashes`
  are present without `maxFeePerBlobGas` (`transaction_args.go:456-458`); the blob-fee check is skipped iff the
  blob cap is zero (`state_transition.go:618-631`). A non-blob call keeps the real BLOBBASEFEE. H15 says
  "Preserve the selected block's other fields", which is right for non-blob calls but wrong for zero-cap blob
  calls. State the blob rule explicitly.

(b) **Parity compatibility cost not recorded in H15.** Parity's unsigned path went through `transact_virtual`,
which *adds* missing balance for `value + gas*gasPrice` (`parity-ethereum/ethcore/machine/src/executive.rs:821-833`).
H13 records this for raw transactions, but H15's "Enforce applicable funding" also removes it for trace_call and
trace_callMany; the H15 Parity paragraph only mentions nonce checks and gas-limit replacement. Add a
"Recommendation risk" line like H13's. (I agree with the direction: eth_call in all tested clients enforces
funding.)

## 8. TraceCall schema issues (A, H, spec)

`src/schemas/trace.yaml:16-62`:
- `gas: uint256` — GenericTransaction uses `uint`, GenericCallTransaction `uint64`
  (`execute.yaml:264-268`); gas is a uint64 everywhere in execution. Use uint64.
- `nonce`: description says "nonce from selected state" but not what a *supplied* mismatching nonce does. Every
  reference ignores it: geth eth_call `SkipNonceChecks: true` (`transaction_args.go:516`, `api.go:798`), Reth
  `request.take_nonce()` (`rpc-eth-api/src/helpers/call.rs:~897`), Parity `check_nonce=false` with CREATE address
  from state nonce (`executive.rs:845, 899`), geth draft passes skip=true (`trace_namespace.go:379`). Spec: "A
  supplied nonce is accepted but neither validated nor used; CREATE addresses derive from the state nonce."
- `trace_call` description (`methods.yaml:3-4`) still says "Explicit zero fees are permitted without rewriting
  BASEFEE" — contradicts revised H15 (ledger acknowledges; listing for completeness).
- `data`/`input` MUST agree: stricter than eth_call (geth `data()` silently prefers `input`,
  `transaction_args.go:84-92`; only the send path errors, line 121-122). Parity accepted only `data`
  (`call_request.rs:20-42`, `deny_unknown_fields`). Strictness is defensible; note it as a deliberate divergence
  from eth_call.
- Consider `$ref`-ing GenericTransaction/GenericCallTransaction plus the `data` alias instead of re-declaring
  fields, to prevent further drift (the draft re-declares 17 fields).
- Overrides: the draft excludes state/block overrides. That matches the eth_call spec, which also lists only two
  params (`execute.yaml:1-12`) even though clients implement overrides; eth_simulateV1 has the schemas
  (`StateOverrides`, `BlockOverrides`, `execute.yaml:52-147`). I agree with deferring, but suggest reserving
  positions (param 4 = StateOverrides, 5 = BlockOverrides, like Reth's `TraceCallRequest`) so implementations
  don't diverge; see §14.

## 9. Missed H13 cases (C, M, spec + coverage)

- **Unprotected (pre-EIP-155) legacy transactions** are consensus-valid; geth rejects them on
  eth_sendRawTransaction only as RPC policy (`--rpc.allow-unprotected-txs`). H13 says "chain identity" but the
  corpus (`fixtures/corpora/raw-validation.json`: probes listed in §B3) only has a *wrong* chain ID. Spec should say
  unprotected txs are valid for tracing (it is a pool/RPC policy like minimum tip) and add a probe.
- **Type-3**: which encoding (canonical vs network form with sidecar) trace_rawTransaction accepts; blob fee cap
  vs BLOBBASEFEE; max blobs per tx (`state_transition.go:595-631`). Unspecified and untested.
- **Type-4**: empty authorization list is tx-invalid (`state_transition.go:640-642`) while individual invalid
  authorizations are skipped, not tx-invalid. The raw corpus has a delegated *sender* but no type-4 transaction.
- **EIP-7825 (Osaka)** tx gas cap: a validity rule for signed txs (`state_transition.go:561-565`), skipped for
  unsigned calls (geth `SkipTransactionChecks: true`, `transaction_args.go:517`; Reth `tx_gas_limit_cap =
  u64::MAX`, `call.rs:888`). Fixtures are Prague, so neither side is exercised. Also: the geth draft rejects a
  signed tx with gas > RPC gas cap as `-32602` (`trace_namespace.go:111-113`) — that is a server limit, not
  invalid params (should be `-32005`), and could reject a consensus-valid tx.

## 10. Missed callMany isolation probes (C, M, coverage)

Each item is a separate transaction; the corpus covers storage carry and revert rollback
(`fixtures/corpora/callmany-isolation.json`) but not: transient storage (EIP-1153) must reset between items;
warm address/slot sets and refund counter must reset (H16 next_step mentions warm access only); EIP-6780: a
contract created in item 0 and SELFDESTRUCTed in item 1 must **not** be deleted (different tx). All three are
cheap to probe with the existing output-word technique and are classic places where an implementation that
runs items inside one EVM/tx context goes wrong.

## 11. Minor harness inconsistencies (B, M, latent verdict)

- `assess()` funding classifier (`fee_policy.py:123`) lacks `'upfront cost exceeds account balance'` /
  `'upfront gas cost exceeds account balance'`, which `assess_compatibility()` recognises (lines 199-202). Besu's
  native trace-path reason is `UPFRONT_COST_EXCEEDS_BALANCE`; today Besu returns -32603 so it is moot, but a Besu
  fix that surfaced its real message would be `blocked` in fee-policy and `matches` in fee-compat.
- Code whitelist `[-32000,-32003,-32602]` (`fee_policy.py:124, 206`) would mark any client that adopts the
  simulate codes (§3) as `blocked`.

---

## B. Oracle verification by hand (checked, correct)

**B1. H15 expected values.** Recomputed with independent arithmetic:
- Environment program (35 bytes, 2 zero bytes): intrinsic = 53000 + 2·4 + 33·16 + 2·1 = 53540; execution = 5·2
  (GASPRICE/BASEFEE/NUMBER/TIMESTAMP/GASLIMIT) + 2·(2+100) (CALLER/COINBASE + warm BALANCE; sender warm per
  EIP-2929, coinbase warm per EIP-3651) + 7·(3+3) + 21 (7-word memory) + 6 + 224·200 = 45083; total **98623** ✓.
- Refund program: intrinsic 53182; 22100 + 100 + 18 → 75400 spent; refund min(19900, 75400//5=15080) → **60320** ✓.
- Revert 53138 + 18 = **53156** ✓; out-of-gas = limit ✓; transfer 21000 ✓. EIP-7623 floor never binds.
- Legacy B+1, gas 200000, value 7: CALLER BALANCE word = 10^18 − 200000·765625001 − 7 = **999846874999799993** ✓.
- `funding-legacy-exact` value `0xde02b6f7625c0c0` = 10^18 − 200000·(B+1) ✓; `funding-typed-exact`
  `0xddfa02b44ed9c00` = 10^18 − 200000·2B ✓ (cap-based funding check, geth `buyGas`); `funding-typed-effective-only`
  reuses the legacy-exact value with cap 2B → funds violation ✓.
- `sequential-funding`: after call 0 (21000·(B+1) paid) call 1 needs exactly 10^18 → funds at index 1 ✓.
- Accounting identity `Σ balance deltas = −used·min(price,B)` (burn) and tip = used·max(price−B,0) ✓; zero-fee
  → no burn/tip ✓; nonce +1 per item including zero-fee and failed items ✓.
- BASEFEE/GASPRICE words match geth `ToMessage` + `applyMessage` for all `accept` families ✓. Omitted fields in
  the oracle default to 0 (`call.get(..., '0x0')`), which is geth's rule, but only matters for `observe` families.

**B2. Paired eth_call evidence corroborates the oracle**: all 9 eth_call builds return BF 0 for legacy-zero and
typed-zero; the documented table in H15 matches `observations.json`.

**B3. H13.** Corpus probes: below-basefee, code-sender, create-nonce-high/low, create-valid, delegated-sender-valid,
execution-oog-valid, funds-gas, funds-value, intrinsic-gas, nonce-high/low, valid, wrong-chain. The rejection rule
(`rules.py:345-355`) only checks "is rpc_error" + "code == -32003"; it does not check the *reason* (a nonce-high
tx rejected for "insufficient funds" would pass). Low risk because each probe violates exactly one constraint,
but a reason check (as the H15 oracle does) would be consistent.

## 12. Erigon trace_call ignores `input` and every post-Berlin call field (C, H, verdict — new cases needed)

`erigon/rpc/jsonrpc/trace_adhoc.go:66-79` (`TraceCallParam`) declares only from/to/gas/gasPrice/
maxPriorityFeePerGas/maxFeePerGas/maxFeePerBlobGas/value/**data**/accessList; there is no custom UnmarshalJSON
(only `ToMessage`/`ToTransaction`, lines 152, 303), so Go's decoder silently drops `input`, `nonce`, `chainId`,
`type`, `blobVersionedHashes`, `authorizationList`. Calldata comes only from `args.Data` (lines 219-220).
Consequences: a trace_call/callMany using the canonical execution-apis field name `input` (GenericTransaction has
**only** `input`, `execution-apis/src/schemas/transaction.yaml:546-548`) executes with **empty calldata** and returns a
success-shaped trace of the wrong execution; an `authorizationList` call executes without delegation; blob hashes
are dropped. The draft already says `data` is an alias for `input` (`schemas/trace.yaml:55-61`), so this is a
conformance failure the harness cannot see: across all corpora, trace_call/callMany call objects use
`from`(1308) `gas`(1308) `data`(1303) `value` `maxFeePerGas` `maxPriorityFeePerGas` `gasPrice` `to` `nonce`(8)
and one `unknownDiagnosticFlag` — **never `input`, `chainId`, `type`, `accessList`, blob or authorization fields,
and never an omitted `from`/`gas`**. Add a small field corpus: `input`-only, `data`+`input` equal, `data`≠`input`
(expect -32602 per draft), `accessList` (observable via warm-SLOAD gas), `authorizationList` (observable via
delegated code), omitted `from`/`gas` (observable via CALLER/GAS), `chainId` mismatch (geth eth_call rejects,
`transaction_args.go:417-423`).

Other clients: Nethermind maps `data` into `Input` so the last one wins with no error
(`Nethermind.Facade/Eth/RpcTransaction/LegacyTransactionForRpc.cs:40-44`); Besu rejects a mismatch
(`CallParameter.java:105-110`); Reth rejects a mismatch (`alloy-evm-0.39.0/src/rpc/transaction.rs:105`).

## 13. "Ignore unknown fields" must not cover schema-defined fields a client does not implement (A, H, spec)

`schemas/trace.yaml:55-61`: "Standard eth_call transaction fields retain their eth_call meaning, including blob
context and authorization lists when supported by the selected fork. Unknown fields MUST be ignored." Read
together, a client that has not implemented `authorizationList` (Erigon today, §12) may treat it as unknown and
run a *different transaction* with a success result. The "ignore" rule is justified for forward-compatible
extensions (H14), but every property listed in the TraceCall schema must be either honoured or rejected with
-32602; "when supported by the selected fork" should mean a fork-level validity error (e.g. authorizationList
before Prague → geth `ErrTxTypeNotSupported`, `state_transition.go:633-636`), not permission to drop the field.

## 14. Overrides: already implemented, mutually incompatible, and silently ignorable (A, H, spec)

Current signatures (source):
- Reth: `trace_call(call, types, block, state_overrides, block_overrides)` (`rpc-api/src/trace.rs:17-23`).
- Nethermind: `trace_call(call, types, block, stateOverride)` (`Modules/Trace/ITraceRpcModule.cs:20-22`); no block overrides.
- Erigon: `trace_call(call, types, block, traceConfig)` where the 4th is a geth `TraceCallConfig`-style object with
  `stateOverrides`/`blockOverrides` fields (`trace_adhoc.go:1068`; `execution/tracing/tracers/config/api.go:31-39`);
  callMany takes a 3rd config with block overrides only (`trace_adhoc.go:1326, 1401`).
- Besu: none (`AbstractTraceByBlock.java:134`, `Map.of()`).

A Reth/Nethermind-style `{address: {...}}` map sent to Erigon decodes as a config with no known keys and is
silently ignored (Go JSON), so the caller gets a non-overridden simulation that looks successful — exactly the
"acceptance ≠ support" hazard H12/H14 warn about. Declaring overrides "outside this profile" leaves that
ambiguity in place. Recommend reserving: param 4 = `StateOverrides`, param 5 = `BlockOverrides`, using the
existing eth_simulateV1 schemas (`execution-apis/src/schemas/execute.yaml:52-147`) — this matches Reth and
Nethermind's p4 — and requiring clients that do not implement them to reject a non-null value with -32602.
If overrides are adopted, H15's zero-fee rule must use the *overridden* base fee (geth: `blockOverrides.MakeHeader`,
`api.go:759-767`, then `ToMessage(header.BaseFee)`).

## 15. Besu trace_call rejects a supplied non-state nonce; its eth_call does not (C, H, verdict)

Besu trace paths validate with `TransactionValidationParams.transactionSimulator()`
(`AbstractTraceByBlock.java:122`), i.e. `allowFutureNonce=false` (`TransactionValidationParams.java:36-38`), so
`MainnetTransactionValidator.java:334-348` returns NONCE_TOO_LOW/NONCE_TOO_HIGH for a supplied nonce ≠ state nonce.
Besu's eth_call uses `transactionSimulatorAllowFutureNonce()` / `…AllowExceedingBalanceAndFutureNonce()`
(`EthCall.java:178-179`). Every other reference ignores a supplied nonce for unsigned calls: geth
(`SkipNonceChecks`, `transaction_args.go:516`), Reth (`take_nonce`, `call.rs:~897`), Nethermind (state nonce,
`TransactionProcessorAdapterExtensions.cs:20-23`), Erigon (field not parsed), Parity (`check_nonce=false`). This is a
trace_call≠eth_call divergence within Besu under H15's own principle; no probe sends a mismatching nonce (the
only 8 nonce-bearing calls are in `precompile-values.json` and use the state nonce). Spec per §8: supplied nonce
ignored for unsigned simulation.

## 16. Erigon trace_callMany (historical block) may see block N+1's pre-block system writes (C, M-L, probe)

`trace_adhoc.go:1112` (trace_call) builds its state reader with txIndex **−1**; `trace_adhoc.go:1347`
(trace_callMany) uses **0**. For non-latest blocks `rpchelper.CreateHistoryStateReader(block+1, txnIndex)` reads at
`minTxNum(N+1) + txnIndex + 1`, commented "1 system txNum in beginning of block" (`rpc/rpchelper/helper.go:175-190`).
So call reads before N+1's begin-system txNum (= post-N), callMany reads after it. If Erigon records the
EIP-4788/EIP-2935 pre-block system calls at that txNum, trace_callMany at historical N sees N+1's beacon root and
history-hash writes that trace_call does not. (Erigon's own eth_call also uses 0, `eth_call.go:218`, while
eth_getBalance uses −1, so this may be a shared off-by-one.) Discriminating probe: at historical block N (not
latest), call the EIP-4788 beacon-roots contract with calldata = timestamp(N+1); post-N state must revert, a
state including N+1's system write returns the root. Compare trace_call vs one-item trace_callMany vs
eth_getStorageAt. Not verified at runtime.

## 17. Client request-semantics matrix (source, for reference)

Paths: E=`erigontech/erigon`, N=`NethermindEth/nethermind/src/Nethermind`, B=`besu-eth/besu`, R=`paradigmxyz/reth` 861a5616 `crates`.
(Collected by a sub-agent reading source; the load-bearing rows §12, §14, §15, §16 were re-verified by me.)

| | Erigon | Nethermind | Besu | Reth |
|---|---|---|---|---|
| trace_call params | 4 (config w/ overrides) | 4 (stateOverride) | 3 | 5 (state + block overrides) |
| block hash accepted | yes | yes (EIP-1898) | no | yes |
| trace_callMany params | 3 (config, block overrides only) | 2, ≤1024 items | exactly 2 (else INVALID_PARAM_COUNT) | 2 |
| trace_rawTransaction params | 2, latest | 2, latest | 2, head | 3 (block_id) |
| default `from` | zero | zero | zero | zero |
| default gas | RPC cap (E trace_adhoc.go:160-163) | GasCap 100M | min(rpcGasCap, block limit) | 50M cap; if priced & omitted: min(allowance, block limit) (call.rs:915-923) |
| GASLIMIT opcode | **max** in call/raw, unchanged in callMany (1159-1160, 1768-1769 vs 1400) | header | header | header |
| supplied nonce | not parsed | replaced by state | **validated** | ignored |
| `input` | **dropped** | last-wins alias | mismatch → error | mismatch → error |
| chainId | not parsed | not checked | typed only | validated |
| blob / 7702 fields | ignored | applied | applied | applied |
| EIP-3607 on unsigned | skipped | skipped | skipped | skipped |
| omitted fees (trace path) | price = base fee (205-207) | zero | price = base fee (TransactionSimulator 609-612) | zero |
| callMany item failure | whole request, index in message (1482) | whole, index lost (-32000) | whole, -32603 | whole, no index |
| callMany env per item | same header | same header (+system calls replayed) | same header | same header |
| pending (call/callMany) | rejected (tracing.go:48-60) | pending header | treated as latest | pending env |

Parity reference: 3 params for call (`block` optional, hash accepted), default gas min(request, 500M)
(`helpers/fake_sign.rs:24-37`), `from` default zero, `data` only, unknown fields denied, pending rejected with
invalid params, balance topped up (`executive.rs:821-833`), nonce unchecked, CREATE address from state nonce.

## Agreement notes (checked, no change)

- **H11** accept `[]`: consistent with Parity source and the useful output-only case.
- **H12** two-argument baseline + observed extension: correct; only Reth (and Parity) take a 3rd arg. Note Parity's
  3rd arg also accepted a block hash.
- **H13 direction**: strict validation matches what Reth already does via unmodified revm env (`trace.rs:132-138`)
  and what the geth draft does (`TransactionToMessage` + `NoBaseFee:false`). Nethermind (SkipValidation, state nonce),
  Erigon (nonce/EIP-3607 off, gas bailout) and Besu (re-simulates as an unsigned call with fake signature,
  `CallParameter.fromTransaction`, `TraceRawTransaction.java:112-132` never checks an invalid result) are the
  migrations. Besu's "empty success-shaped result" in the H13 doc is consistent with that unchecked invalid result.
- **H25**: agree; §4's "index in `error.data`" also helps the post-commit/abort rule since no partial array is sent.
- **H31**: agree with latest default (stale Reth text only, §6).
- **H32**: agree that simulations should reject pending until specified — precedent is Parity (invalid params,
  `impls/traces.rs:109, 134, 161`), upstream `debug_traceCall` ("tracing on top of pending is not supported",
  `eth/tracers/api.go:895-902`) and Erigon (same message). Besu silently maps pending→latest and Reth/Nethermind
  build a pending env; those are the migrations.
