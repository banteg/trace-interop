# stateDiff review (H16, H17, H18, H26, H28 and stateDiff content)

Sources read: Parity `55c90d40`; Besu main `07f0a4b2f8`; Erigon main `3b4861d1038` (the captured dev build is e26d9bd4); Nethermind master `ac02224f25` (from 09-22, so it predates #13668); revm-inspectors 0.43.0 (the version Reth locks, read from the cargo registry) and a fresh-main export; Geth draft `fa8ecb92`; pinned spec `b979aefe`.

Evidence used: the active snapshot `evidence/2026-09-24/h15-call-compat/*/observations.json`.

Reproduce with `scripts/compare_responses.py`: `show <run dir> <case>` prints one case's stateDiff for every build, and `groups <evidence dir>` groups builds that return identical stateDiffs.

Severity legend: **spec** = would change the spec, **verdict** = would change a client verdict, **cosmetic**.

---

## 0. Reference model: what Parity did, compared with the clients and the draft

### Parity's algorithm

- **Post-state.** Built from every cached account that still exists (`account-state/src/state.rs:790-798`). Each account's storage is its dirty `storage_changes`.
- **Pre-state.** `orig.to_pod_diff(post)` (`state.rs:868-919`). The storage keys are the union of the dirty keys held by the pre-state cache and the post-state cache.
- **Classification.** `pod/src/account.rs:106-146`:
  - `(None,Some)` gives Born for balance, nonce, code and every post storage entry.
  - `(Some,None)` gives Died.
  - `(Some,Some)` gives `Diff::new` per field. That returns only Same or Changed (`types/src/account_diff.rs:38-44`), never Born or Died.
  - Storage: only keys with pre ≠ post are kept, and they are always Changed (`*`). This holds even for 0→x or x→0.
  - An account with nothing changed is dropped (returns None).
  - The storage type comment says "values are not allowed to be `Diff::Same`" (`account_diff.rs:64`).
- **Existence** means presence in the state cache/trie. Two cases follow:
  - A touched empty account is removed by `kill_garbage` (`state.rs:762-778`, called at `machine/executive.rs:1180-1181`). If it existed before, the result is Died. If it was absent before, there is no diff.
  - SELFDESTRUCT runs `kill_account` (`machine/executive.rs:1176-1178`), which also gives Died.
- **SSTORE of an unchanged value** is not recorded (`state.rs:684`).

### Behaviour matrix

"Existing-empty" means present in the trie but EIP-161-empty. "main" means revm-inspectors fresh main.

| Behaviour | Parity | Besu | Erigon | Nethermind (master) | Reth 0.43 / main | Geth draft | Draft |
|---|---|---|---|---|---|---|---|
| Unchanged touched/read account | omitted | omitted | omitted | omitted | omitted (0.43: all-`=` entry for zero-balance pre-Cancun destruct) | omitted | **unstated** |
| Birth of an absent account | `+` for all fields | `+` | `+` | `+`, but empty code gave `=` until #13668 | 0.43: `*` unless is_created; main: `+` | `+` | `+` (stated) |
| Existing-empty account touched then EIP-161-removed | `-` with zeros | `-` with zeros | `-` with zeros | `*` to `null` (invalid) | omitted | omitted (no hook fires) | **unstated** |
| Storage 0→x / x→0 on a surviving account | `*` from/to zero word | `*` | `*` | `*` | `*` | **`+` / `-`** | **unstated** |
| Net-zero slot write | omitted | omitted | omitted | omitted | omitted | omitted | unstated; schema allows `=` |
| Storage of a born account | `+` for dirty keys (a zero value is possible) | `+` nonzero only | `+` nonzero only | `+`, decided by whether the balance was born | `+` changed slots | `+` nonzero only | unstated |
| Storage of a deleted account | effectively `{}` (see A4) | `{}` | `{}` | written slots as `*` to 0 | main: accessed nonzero slots as `-` | written slots as `-` | "open question" |
| callMany timeline | sequential | sequential | sequential | sequential | sequential | sequential | sequential |
| Pre-block system writes / withdrawals / 7002 dequeue in tx diffs | n/a | none (**not executed**, see B3) | none | none | none | none | **unstated** |
| Blob fee in the sender's debit (replay) | n/a | yes | yes | yes | yes | yes | **unstated** |

Sources for the client columns:
- Besu: `StateTraceGenerator.java:87-102,130-143`
- Erigon: `trace_adhoc.go:730-742,756-881`
- Nethermind: `ParityAccountStateChangeJsonConverter.cs:35-102`, `StateProvider.cs:1150-1206`
- Reth 0.43: `parity.rs:509-575`
- revm-inspectors main: `parity.rs:447-522`
- Geth: `trace_capture.go:220-262`

The replay-fee rows were verified from evidence: all 9 builds agree byte-for-byte on `forks/replay-55/56/59/60` account sets and balances.

---

## Ranked findings

### 1. [B/C, verdict] Besu `trace_callMany` does not start each call at a transaction boundary, so SSTORE uses the wrong original value

Confidence: **high**, from evidence plus source.

**Evidence.** Case `a/many-storage-write-revert-read`, call 1: SSTORE `0x2b` to slot 0, which holds 42 after call 0, then REVERT. Charged gas per client:
- Besu: 23 535 (sender debit `47070000000000` at 2 gwei)
- Geth, Nethermind and Erigon: 26 335. Nethermind debits `52670000000000`. Erigon's coinbase tip is `52625824880950` = 26 335 × 1 998 322 570.

**Independent derivation of 26 335.** The code is `…6000556020351561001957 60006000fd`.
- Non-SSTORE opcodes cost 55.
- SSTORE is cold, with original = current = 42 ≠ new, so it costs 2100 + 2900.
- Execution total is 5 055, which matches Geth/Erigon/Reth's root `gasUsed` of `0x13bf`.
- Intrinsic cost is 21 000 + 2×16 + 62×4 = 21 280.
- Total: 21 280 + 5 055 = 26 335.

**Besu's shortfall.** Besu is exactly 2 800 lower (2900 → 100). That is what you get if it treated the slot's *original* value as 0, the pre-bundle value.

**Cause.** In `TraceCallMany.java:128-140` each call runs in `updater.updater()` and commits into the shared `updater`. It never calls `markTransactionBoundary()`. `UpdateTrackingAccount.getOriginalStorageValue` (`evm/.../UpdateTrackingAccount.java:285-293`) therefore falls through to the pre-bundle value. Besu's own block replay does it correctly (`TraceBlock.java:206-215`, `ChainUpdater.getNextUpdater` → `markTransactionBoundary`).

**Harness miss.** The failing call is exactly the one where Besu and Nethermind omit the reverted root's `gasUsed`. `execution_models.assess` therefore reports H16 as **blocked** ("No receipt gas or execution-gas witness"). An independent oracle is trivial here: this program is fully modelled.

**Lineage.** Parity itself did not commit between calls (`client.rs:1532-1536`, and `original_storage_at` reads the committed root at `account-state/src/state.rs:609-616`). It likely had the same quirk, which is a Parity wart the spec should fix.

**Spec change.** The callMany text should say: *each call is a separate transaction for EIP-2200/3529 original values, EIP-2929 access sets, EIP-1153 transient storage and refund counters.*

**Harness fix.** Add a derived-gas oracle for the storage program, or add a refund/original-value probe: write X, then in the next call restore the original value.

### 2. [A+B, spec + verdict] Storage markers are unspecified; the Geth draft diverges from Parity and all four clients, and the harness accepts it

Confidence: **high**.

- The Geth draft computes storage with `traceChange(old,new, old!=0, new!=0, …)` (`trace_capture.go:245-251`). A 0→x slot on an existing account comes out as `{"+":x}`, and x→0 as `{"-":x}`.
- Parity and Besu, Erigon, Nethermind and Reth all emit `{"*":{"from":0x00…,"to":x}}`. Evidence: `a/many-storage-write-read` call 0.
- `rules.py:319-321` explicitly accepts both forms ("marker style is a separate compatibility decision"). No decision covers that choice, so the Geth draft is shown as "✅ Checked cases agree".
- The same code also affects nonzero→zero slots (`-`), which no case tests.

**Spec:** in TraceStorageChange, `+` and `-` appear only when the whole account is born or dies. Slots on a surviving account are always `*` with 32-byte from/to words, including zero words.

**Harness:** reject `+` and `-` storage entries on accounts that exist at both endpoints.

### 3. [B/C/D, verdict] H28 is marked "Converged", but Besu replay never executes the block's pre-block system calls

Confidence: high on source, medium on impact because no probe exists.

**Source.**
- `Tracer.processTracing` opens the *parent* world state (`processor/Tracer.java:42-53`).
- `TraceReplayBlockTransactions` then only calls `processTransaction` (`ExecuteTransactionStep.java:88-111`).
- `BlockTracer`, `BlockReplay` and `DebugTraceBlockStreamer` do the same.
- Only the plugin `TraceServiceImpl.java:209,263` runs `PreExecutionProcessor.process`.

**Consequence.** A mined transaction that reads EIP-4788 at its own `block.timestamp`, or reads the EIP-2935 slot for the parent, sees stale storage in Besu replay. Its trace, output and stateDiff then diverge from the chain. BLOCKHASH is unaffected, because it uses a blockchain-backed lookup.

**Ledger inconsistency.** `docs/client-fixes.md` already lists the open **Besu #10953** "Replay block pre-execution before tracing transactions". Yet H28 shows Besu "✅ Checked cases agree", because the only H28 probes are `trace_call` and `eth_getStorageAt`.

**Fix.** Add a mined fixture transaction that STATICCALLs `0x000F3d…Beac02` with TIMESTAMP and SSTOREs the result, and replay it with stateDiff. Until then, H28 should not claim replay convergence.

### 4. [A/B/D, spec + verdict] Erigon `trace_callMany` at a historical block reads block N+1's system writes; the ledger accepts the maintainer's rationale without checking it

Confidence: medium-high.

**What the code does.**
- `trace_adhoc.go:1347` uses txnIndex **0**, which means `Min(N+1)+0+1` (`rpchelper/helper.go:180-186`). That is state *after* N+1's EIP-4788/2935 system transaction; commit 66571d04390 says so itself.
- The same method executes with block **N's** header as the EVM context (`doCallBlock(... parentHeader ...)` → `NewEVMBlockContext(header)`, `trace_adhoc.go:1359,1400`) and with N's base fee (`:1323`).

**Why the "parent block" rationale does not hold.** The environment is N's, but the state includes N+1's system writes, so the result is internally inconsistent. Parity's `call_many` used the same `state_at(block)` and header as `call` (`client.rs:1518-1538`). Erigon's own `debug_traceCallMany` default was moved to −1.

**Spec gap.** The draft `trace_callMany` description never says what state the first call starts from.

**Spec:** "The first call executes against the same state and environment as `trace_call` at the selected block."

**Harness:** add a callMany twin of `fork-followup/beacon-call-55`.

### 5. [A, spec] The draft does not define "existence", account inclusion, or storage-diff rules; some parts of the schema are too permissive

Confidence: high on the text, low on mainnet impact.

- **(a) Account inclusion.** An account appears only if balance, nonce, code or any storage slot changed, or its existence changed. Accounts that were touched, read or warmed without net change are omitted. Every client already does this; Reth 0.43 has an all-`=` edge case that is fixed in main. The draft never says so.
- **(b) Existence.** Existence should mean presence in the state trie, as in Parity, Besu and Erigon.
  - An EIP-161-empty account present before and removed by touch-clearing is a deletion (`-` with zeros).
  - This currently splits clients three ways: Besu/Erigon emit `-`, Nethermind emits a schema-invalid `*`→`null`, and Reth and the Geth draft omit it.
  - No fixture has an empty account in genesis; I checked `a`, `initial`, `forks`, `b` and `raw-validation`.
  - Such accounts cannot be created after Spurious Dragon, so impact is legacy-only. The spec should still say it, and the ledger should stop using "existing-but-empty" for prefunded accounts that merely have empty code.
- **(c) Storage `=`.** `TraceStorageChange` allows `'='`. Parity forbids it, and `rules.py:321` accepts `{slot:'='}`. Remove `=` from the storage schema and from the harness.
- **(d) Born-account storage.** A born account's storage should list only nonzero post values as `+`. That is what Besu, Erigon, Reth and Geth do; Parity could leak a `+0x00…` for a slot written and then zeroed.

### 6. [A/B, spec, H26] Storage of deleted accounts: Parity actually emitted `{}`, which settles the "open policy question"

Confidence: medium-high, from source.

**Why Parity emitted `{}`.**
- For a killed account the post cache entry is `None`.
- `to_pod_diff` takes storage keys from the *pre* clone's dirty `storage_changes`, plus the query account's changes. The query account is `None`, so `opt.account.as_ref()?` short-circuits (`state.rs:879-892`).
- For `trace_call`, and for the first transaction of a replay, the pre clone is clean. So Parity's Died entries had `storage: {}`.
- The only exception is keys dirtied by earlier uncommitted calls or transactions in the same bundle or block, which is a quirk.

**Clients today.**
- Besu `{}` (`StateTraceGenerator.java:142`)
- Erigon `{}`
- Nethermind: written slots as `*`→0
- Geth draft: written slots as `-`
- revm-inspectors main: *accessed* nonzero-original slots as `-`

**Proposal.** A deleted account's `storage` is `{}`, and consumers treat account `-` as wiping all storage. This is deterministic, cheap, and matches Parity, Besu and Erigon. The H26 page's statement that each prior slot is "supplied to that helper" should note that in practice none were.

**Coverage gap.** The current H26 fixture account has no storage, so it cannot discriminate between these behaviours.

### 7. [B, latent false positives] The H18 oracle mis-models multiple authorizations and absent authorities

Confidence: **high**, demonstrated.

**The problem.** `execution_models.py` (H18 block) compares *each* authorization tuple against the transaction's *net* diff, and assumes the authority existed before, expecting `{"*":{from:'0x',…}}`.

**Demonstration** (synthetic case run through `assess`):
- Two tuples from one authority: a correct net diff `0x`→`ef0100‖T2` fails **both** checks.
- An absent authority with correct `+` markers fails H18 and simultaneously passes H17, so the two oracles contradict each other.
- The oracle also treats every tuple as applied, so it has no model for skipped invalid tuples (wrong nonce or chain id).

**Why it matters now.** The ledger's own "Decision needed" asks for exactly these probes. Fix the oracle first:
- fold tuples per authority
- validate each tuple's nonce and chain id
- use `+` when the authority is absent
- also check that the nonce equals the pre-state nonce plus the number of applied tuples

### 8. [A/B, spec + latent] Fee wording and the H16 conservation oracle ignore blob fees, fee collectors and SELFDESTRUCT burns

Confidence: high.

**Evidence.** In `forks/replay-56` tx 0 (type 3, 1 blob, excessBlobGas 0), all 9 builds report the same totals:
- sum of balance deltas = −3 603 562 989 668
- which is 51 868 × base fee 69 475 647 (= 3 603 562 858 596) + 131 072 (= 1 blob × 131 072 blob gas at blob base fee 1 wei)

So every client puts the blob fee in the sender's debit.

**Recommendation wording.** H16 says "sender pays value plus gas, fee recipient gets the tip, base fee is burned". It should say:
- the sender also pays `blobGasUsed × blobBaseFee`
- the base fee and blob fee are removed from supply, or credited to a chain-defined collector (Erigon `txn_executor.go:766-778` and Nethermind `TransactionProcessor.cs:1730-1737` do this on Gnosis-type chains)

**Oracle.** `execution_models.py` uses `burn=min(price,base)*gas`. That would false-flag every client if a blob replay (e.g. replay-56 or replay-59) were ever assigned to H16. It also ignores:
- SELFDESTRUCT burns: pre-Cancun, and post-Cancun same-transaction create-then-destroy-to-self
- refunds on the root-gas path (`gas = intrinsic + root.gasUsed`)

Model these before adding the "refunds and blob-fee accounting probes" the ledger plans.

### 9. [A, spec wording] Block-level operations are excluded from every transaction diff; all clients agree, but the draft never says so

Confidence: high.

**Evidence.** `forks/replay-55` and `replay-59` (withdrawals), `replay-56` (4788) and `replay-60` (Prague, EIP-7002 request): no tx diff on any of the 9 builds contains the 4788 or 2935 contracts, the withdrawal recipients, or the post-block 7002 dequeue. The 7002 entry in tx 3 is the user's own enqueue.

**Source.**
- Geth draft runs `core.PreExecution` before the first capture (`trace_namespace.go:438-460`).
- Reth runs `apply_pre_execution_changes`.
- Nethermind uses `NullStateTracer` for system writes.
- Erigon runs `InitializeBlockExecution` and commits into the cache.

**Spec text:**

> "A transaction's stateDiff covers only that transaction. Block-level system operations (EIP-4788/2935 pre-block calls, withdrawals, EIP-7002/7251 post-block calls, rewards) are applied in protocol order to the replay state but are attributed to no transaction's stateDiff; concatenated diffs therefore do not reconstruct the block post-state."

Erigon's opt-in `includeWithdrawals` extra element (`trace_adhoc.go:1017-1062`) should be declared outside the baseline.

### 10. [B, latent] The H17 existence model does not follow state created by earlier calls in a callMany bundle

Confidence: medium.

For earlier calls, `assess` adds only `prior['to']` (when value is sent) and the miner. It does not add:
- the earlier call's sender (its nonce becomes ≥1, so it now exists)
- CREATE addresses
- internal value recipients

The current fixtures always use funded senders, so nothing is misreported today. A callMany starting from an unfunded or default `from` would report the second call's correct `* nonce` as "new account lacks creation markers".

### 11. [D, cosmetic/ledger accuracy] Reth rows understate upstream status; one Nethermind description is understated

Confidence: medium.

**Reth.**
- Locked revm-inspectors 0.43.0 has the old logic: `is_created() && balance==0`, code compared only when created, and no `Removed` (`parity.rs:509-575`).
- The fresh-main export already contains:
  - the #509 fix: 7702 code-hash comparison (`parity.rs:497-503`)
  - the #510 fix: `-` deletion (`:462-481`)
  - the #526 existence logic: `existed = db_acc.is_some()` (`:466-486`), with the test `tests/it/parity/state_diff_birth.rs:86`
- There is no git metadata in the export, so the #526 merge status is unconfirmed; `client-fixes.md` still lists #526 as open.
- The H18 and H26 Reth rows should say "fixed upstream in revm-inspectors (unreleased; needs >0.43.0 and a Reth bump)". H17 should be updated if #526 has merged.

**Nethermind.** Release 2.0.0's pre-Cancun destroy emits `{"*":{"from":"0x64","to":null}}` for **balance**, nonce and code. That is schema-invalid, not merely "loses code/nonce markers". H26 never checks the balance marker (`rules.py:452-457`).

---

## Checked and found correct

- **H16 Parity cloning claim.** Correct: the clone happens right before each virtual call (`client.rs:1228`), on one shared uncommitted state (`client.rs:1532-1536`), so each diff is relative to the previous call's post-state. All six implementations are sequential, verified in source and in `many-storage-write-read`, whose second diff has no storage on any build.
- **H17 oracle against revm-inspectors main.** The rule "new account needs all `+`, existing account has no `+`" matches main's rule `!existed && (is_created() || !is_empty())`. Main omits a touched-then-cleared account that was absent at both endpoints, and the oracle agrees.
- **H26 expected values.** Correct: genesis `0x…1007` has `balance 0x64`, `code 0x611008ff`, no storage. Block 55 is before Cancun (timestamp 550 < 560) and block 56 is after.
- **Hex handling.** `balance_delta` parses integers, so it tolerates any representation. Exact string compares on nonce, code and storage are appropriate because the schema mandates minimal or 32-byte lowercase forms. `_alloc` and `_codes` keys are normalised to lowercase `0x`.
- **Precompile touches.** A zero-value touch produces no entry on any client, which matches Parity.
- **Erigon `trace_call`/`trace_callMany`.** Crediting the coinbase tip without debiting the sender (gasBailout, `trace_adhoc.go:1198,1360`) is already recorded under H15.
- **Nethermind** re-runs block N's own pre-block system calls on the post-state of N for `trace_call` and `trace_callMany`. This is idempotent (same header), so it has no observable effect today.
