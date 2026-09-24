# Filter / selection review (H01–H06, H23, H27, H30, H32; pagination, rewards, tags, limits)

Scope: which records `trace_filter`, `trace_block`, `trace_transaction`, `trace_get` and the replay
methods select, not the content of those records. Spec text is read from pinned `b979aefe`
(`git show b979aefe:src/...` in execution-apis).
Paths are relative to each client checkout listed in [the index](README.md#reviewed-revisions). "Fresh Reth" means
Reth main at 861a5616 (2026-09-24).

Legend: **Kind** A = disagreement with the recommendation or draft, B = harness bug or gap,
C = missed client issue, D = stale or incorrect ledger claim. **Sev** spec = would change the
spec, verdict = would change a client verdict, cosmetic = neither.

---

## 1. Range-endpoint and reversed-range errors contradict the sibling eth_getLogs spec (A, spec + verdict, high)

The draft says an unknown selected block **or range endpoint** returns `-32001`
(`methods.yaml` trace_filter description; trace-profile.md "Explicit choices"). Case
`a/missing-block-filter` (`toBlock: 0xffff`, head 0x30) asserts `-32001` under H06
(`rules.py:396-398`).

The same execution-apis tree now fixes this for `eth_getLogs`. execution-apis #875 (0a4179bc,
2026-09-07; present in b979aefe) says in `src/eth/filter.yaml:153-160`: *"If either bound
resolves to a block number greater than the current head block, or if `fromBlock` resolves to
a block number greater than `toBlock`, clients MUST return the `-32602: Invalid params` error.
Clients MUST NOT clamp the range…"*. Upstream geth follows it: `eth/filters/api.go:39-40` defines
`errInvalidBlockRange` and `errBlockRangeIntoFuture` as `invalidParamsErr` (-32602), and
`api.go:481-483` and `filter.go:229-234` use them. The trace draft describes itself as mirroring
getLogs (OR/AND composition, latest/latest defaults), but it diverges on exactly the range-error
contract that getLogs has just pinned down.

Observed for `missing-block-filter` (evidence/2026-09-24/h15-call-compat/a/observations.json):
- Besu returns -32602. Its `FilterParameter.validateBlockRange` (FilterParameter.java:193-209)
  is shared with eth_getLogs, and it is exactly the #875 behaviour, yet the harness flags Besu
  as ⚠️ Differs.
- Reth and the Geth draft return -32001 (✅).
- Erigon returns `[]`, Nethermind returns -32000.

Reversed explicit ranges (`fromBlock > toBlock`, both explicit) are **not specified at all** in
the draft. Only the H30 case of an omitted fromBlock with an earlier toBlock gets a "range error",
and its code is "left for review". Current code gives:
- -32602: Besu (FilterParameter.java:195-198; the `fromBlock > toBlock → []` branch at
  TraceFilter.java:127-129 is dead), Reth (trace.rs:402-406), Geth draft
  (trace_namespace.go:223-225).
- -32000: Erigon (`errors.New`, trace_filtering.go:370-372) and Nethermind
  (`ErrorCodes.InvalidInput`, BlockFinderExtensions.cs:116-119).
- Parity had no check (client.rs:2057-2064 feeds `start..end` to the bloom iterator); a
  reversed range most likely produced `[]`.

No harness case covers an explicit reversed range.

Recommendation:
- For trace_filter, copy the #875 sentence: beyond-head or reversed resolved bounds → -32602,
  with no clamping. That also settles H30's open code for `toBlock` before an implicit latest
  start.
- Keep -32001 for single-block selectors (`trace_block`, `trace_replayBlockTransactions`,
  `trace_call` Block). That matches the newer eth/debug getters (`src/eth/block.yaml:253`,
  `src/debug/getters.yaml:102`).
- Type `TraceFilter.fromBlock`/`toBlock` as `BlockNumberOrTagForRange` (block.yaml:142-148, the
  getLogs type, which excludes `pending`) rather than `BlockNumberOrTag`. That answers H32 for
  trace_filter by construction, since `pending` becomes -32602, matching geth's
  `errPendingLogsUnsupported` (api.go:42).
- Verdict impact: `missing-block-filter` flips for Besu (to agree), Reth and the Geth draft (to
  differ). Add `filter-reversed` (`{fromBlock: 0x3, toBlock: 0x2}`).

## 2. Reward records are not matched by author in Besu and Nethermind; Erigon ignores mode for rewards (C, verdict, high on code)

The draft (and Parity `ethcore/trace/src/types/filter.rs:117-119`) says a reward matches
`toAddress` by `author`, has no from side, and fails any populated `fromAddress`.

- **Besu:** `TraceFlatTransactionStep.java:61-80` filters every flat trace, rewards included (the
  reward "transaction" is appended per block by `TraceFilterSource.java:53` and generated at
  `TraceFlatTransactionStep.java:54-55`). The filter uses the generic `action.getFrom()` and
  `action.getTo()`. A reward action carries only `author` (RewardTraceGenerator.java:67-94), so
  `toAddress: [miner]` never returns block or uncle rewards.
- **Nethermind:** `TxTraceFilter.cs:41,56-57` matches on `action.From` and `action.To`. The reward
  action sets only `Author` (ParityLikeBlockTracer.cs:52-60). Same loss.
- **Erigon:** `trace_filtering.go:597` and `:608` emit the block or uncle reward whenever the
  coinbase is in `toAddresses` (or no addresses are given). This ignores `mode` and
  `fromAddress`, so with explicit `mode: "intersection"`, `fromAddress: [X]` and
  `toAddress: [coinbase]`, Erigon returns rewards that the spec (and Alloy's matcher,
  filter.rs `Action::Reward => (from_addresses.is_empty(), …)`) excludes. Erigon does index the
  coinbase and uncle coinbases at block end (`execution/exec/txtask.go:543-552`), so to-only
  lookups do reach the reward.
- **Reth** (Alloy matcher) and the **Geth draft** (`trace_namespace.go:597-598`) match the draft.

No harness case exercises this. The `forks` chain already has PoW blocks 1–47, each with a block
and an uncle reward. The coinbase is `0x000…0`, and block-35/47 evidence shows all nine builds
emit identical reward records, so a fixture is cheap. Add:
- `filter-47-reward-to`: `{fromBlock: 0x2f, toBlock: 0x2f, toAddress: [<coinbase>]}`, expecting
  exactly the block and uncle reward records (plus any call to that address).
- `filter-47-reward-intersection`: `{…, fromAddress: [<tx sender>], toAddress: [<coinbase>],
  mode: "intersection"}`, expecting no reward records.
- Uncle-coinbase variants if the uncle miner differs.

Predicted verdicts: Besu and Nethermind differ on the first case, Erigon on the second.
Severity: verdict change under H23. It matters for mainnet pre-Merge and ETC-style chains,
where "all payments to a miner" is a standard trace_filter use.

## 3. Nethermind trace_filter silently truncates to a partial success, including every range that starts at genesis (C, verdict, high)

`TraceRpcModule.cs:299-318` (streaming and buffered paths) runs
`if (!TryResolveParentForTracing(block, out …)) break;`. `TryResolveParentForTracing`
(`:321-346`) logs `"trace_filter stream truncated: missing state …"` and returns false when the
block or its parent has no state, or the parent header lookup fails. The request then completes
**successfully with the records gathered so far**. That is exactly the silent narrowing the
draft forbids ("Return an error rather than silently truncate … return 4444").

Block 0 has no parent, so any range starting at genesis yields `[]`. This is the root cause of
the "Nethermind returns [] for both … separately tracked history issue" note in H32 (`h30/filter-earliest`
and `h30/filter-0-to-2`), and it should be recorded as a filter-truncation defect, not as a tag
observation. The pruned fixture is Reth-only (H06 next step), so no case exercises the
mid-range state gap. A Nethermind retention run of `pruned/old-filter` should expect 4444, and
would currently get a truncated success.

## 4. Genesis block handling is undefined, and Reth fabricates a genesis reward on PoW-genesis chains (C, spec, high for Reth and Nethermind, medium for Erigon)

- **Reth:** `trace_block` (trace.rs:523-560) appends rewards whenever
  `calculate_base_block_reward` returns `Some`. That function (`:307-318`) checks only
  `is_paris_active_at_block` and has no genesis guard. For block 0 on a PoW-genesis chain
  (mainnet, or the `forks` fixture with difficulty 0x20000), `trace_block(0)` returns a
  5-ETH `block` reward for the genesis coinbase that never happened. `trace_filter` from block
  0 includes it too (`:445-462`).
- **Nethermind:** `trace_block(0)` errors, because the parent lookup fails (TraceRpcModule.cs:367-371).
- **Erigon:** `trace_block(0)` returns `[]` (trace_filtering.go:198-200). Its `filterV3` has no
  block-0 guard for the final-txn reward branch (`:582-617`; only `isPos` short-circuits), so an
  address-less filter from 0 on a PoW genesis can emit a genesis reward that `trace_block(0)`
  omits. Medium confidence; it depends on the block-0 final txnum being iterated.
- **Besu** (`TraceBlock.java:97-100`; its filter skips genesis at TraceFilter.java:145-150) and
  the **Geth draft** (`trace_namespace.go:557`) return `[]`.

The spec should state that genesis has no transaction or reward records, so `trace_block(0)`
returns `[]`. Add `forks/block-0` and `forks/filter-0-1` cases.

## 5. Failed-CREATE filter semantics are asserted by the draft but never tested, and Nethermind diverges (B + C, verdict, medium-high)

The draft and H23 say a failed CREATE has no created-address match. Parity
(`filter.rs:103-110`: `_ => to_address.matches_all()`), Alloy/Reth (`matches_all` only when
`to_addresses` is empty), Erigon (`trace_filtering.go:679-684`: only a `*CreateTraceResult` with
an address) and the Geth draft (`trace_namespace.go:590-593`: requires `frame.Error == ""`) all
implement this.

Nethermind does not. `ParityLikeTxTracer.cs:413-421` sets `action.To = to` (the would-be
contract address) in `ReportAction`. `HandleActionError` (`:470-475`) clears only the result,
and `TxTraceFilter.cs:56-57` matches `action.To`. So `toAddress: [would-be address]` returns the
failed CREATE. Besu never matches CREATE by recipient at all (already H23).

All `a` chain CREATE fixtures succeed (the oracle's CHILD_INIT creates and self-destructs), so the
harness cannot see this. Add a mined CREATE whose initcode reverts, then query
`toAddress: [derived address]`, expecting `[]`, and `fromAddress: [creator]`, expecting the
failed frame.

## 6. `pending` for block-selector methods has four behaviours, and Reth localizes records to a block that is not on the chain (C + A, spec, medium-high)

The draft types `trace_block` and `trace_replayBlockTransactions` Block as `BlockNumberOrTag`,
which admits `pending`, with no semantics. Current code:
- **Reth:** `trace_block` calls `recovered_block(BlockId::pending)`, which returns the locally
  built pending block (helpers/block.rs:268-285). `PendingBlockKind` defaults to `Full`, meaning
  mempool transactions (rpc-eth-types/src/builder/config.rs:24-31). It then traces that block and
  localizes records with the pending block's hash and number (trace.rs:523-560).
- **Besu:** silently uses latest (`AbstractBlockParameterMethod.java:53-56`).
- **Nethermind:** uses `FindPendingBlock()` (IBlockFinder.cs:64, 97).
- **Erigon** (`rejectPendingNumber`, tracing.go:48-53) and the **Geth draft**
  (`trace_namespace.go:287-289`) return an error.
- **Parity** returned `null` for `trace_block` (impls/traces.rs:67-71) and rejected pending for
  replay.

H32 has only `filter-pending` and call/many pending cases. Add `trace_block("pending")` and
`trace_replayBlockTransactions("pending", ["trace"])`.

Spec suggestion:
- Until a pending contract exists, use a tag type without `pending` for these historical selectors
  (a `BlockNumberOrTagForRange`-like type), which makes it -32602.
- Localized records must never carry a hash that is not in the canonical chain.

## 7. H27's root cause in Besu is broader than fork rules: range execution skips every inter-block state transition (A + D, spec wording + verdict, high on code)

H27 cites Besu's single `protocolSpec` from the first header, and that is still true on current
main (TraceFilter.java:155-184). Beyond that:

- `TraceFilterSource` (TraceFilterSource.java:40-55) streams every block's transactions into one
  `ChainUpdater` (TraceBlock.java:192-216). `ExecuteTransactionStep` (ExecuteTransactionStep.java:84-111)
  processes transactions only. Between blocks, **no** block reward, withdrawal (EIP-4895),
  beacon-root (EIP-4788), history (EIP-2935) or request (EIP-7002/7251) processing is applied.
  Block N+1 executes on block N's post-transaction state, not its post-block state.
- Besu's `trace_block` (TraceBlock.java:111-178) and `trace_filter` never call
  `getPreExecutionProcessor()` system calls; they use only `createBlockHashLookup`. Besu's
  `debug_traceBlock` does call them (DebugTraceBlockStreamer.java:179,250;
  processor/BlockTracer.java:80). A transaction that reads the 4788 or 2935 contracts is
  therefore traced against stale system storage, even in a single-block query.

The current H27 recommendation ("use each block's own fork rules and state") covers this in
spirit. The client-facing "Proposed" text says only "use each block's own execution rules",
though, which invites a fix that swaps the protocolSpec per block and leaves the state skew.
Reword it to: "each block is traced from its parent's post-block state, with that block's
pre-transaction system operations applied". Consider a `forks/filter-across-52` variant whose
block-52 transaction spends a withdrawal credited in block 51, which would expose the skew
independently of fork rules.

## 8. H05 ledger omits Erigon's opt-in withdrawal records; system operations need one explicit sentence (A + D, spec, high on code)

The ledger says "neither Parity's reward encoding nor that EIP defines a trace_* withdrawal
action". True, but Erigon already ships an opt-in representation (PR #21592, 2026-06-28):
- With the extra `traceConfig.includeWithdrawals` argument, `trace_block` appends `reward`
  records with `rewardType: "withdrawal"` and the value in wei (trace_filtering.go:252-256,
  811-832).
- `trace_replayBlockTransactions` appends an extra **hashless** envelope carrying the withdrawal
  stateDiff (trace_adhoc.go:1015-1062).
- It is off by default and absent from `trace_filter` (filterV3 has no withdrawal branch).

The draft schema's `TraceRewardAction.rewardType` enum is `[block, uncle]`, so Erigon's extension
output is schema-invalid under this profile. That is fine, but the spec should say explicitly
whether extensions may reuse `reward`. It should also state that the replay array contains
exactly one envelope per transaction, which the Erigon extension breaks.

System calls: no client emits records for EIP-4788, 2935, 7002 or 7251 operations in `trace_block`,
`trace_filter` or replay. Reth runs `apply_pre_execution_changes` untraced
(rpc-eth-api/helpers/trace.rs:302,424-436). Nethermind uses `NullTxTracer` and no tracer for
requests (BlockProcessor.cs:162-163,205-211). Erigon runs `InitializeBlockExecution` untraced
(trace_filtering.go:746-752) and skips `txIndex == -1` in filters (`:623`). The Geth draft replays
transactions only. The draft states this only for withdrawals. Add "system operations are
applied to state but are not trace records", so that nobody later adds them to `trace_block` as
`call` frames with null localization, which would shift pagination.

## 9. Pagination: the draft stance is right, but harness probes do not discriminate it and "reward ordering" can be closed (B, cosmetic → verdict, high)

Code check (all agree with the draft's "filter, then skip `after`, then take `count`, in block →
transaction → preorder → rewards order"):
- Parity: client.rs:2066-2071 over db.rs:349-365, with rewards as the trailing pseudo-transaction
  at db.rs:189-193.
- Erigon: `nSeen` counts only matched records, trace_filtering.go:450-477.
- Reth: `apply_trace_filter_pagination` after `matcher.retain`, trace.rs:476-482 and 675-702.
- Besu: `ArrayNodeWrapper.addPOJO` after `TraceFlatTransactionStep` filtering.
- Nethermind: `TxTraceFilter.ShouldUseTxTrace` decrements `_after` only on a match.
- Geth draft: trace_namespace.go:262-280.

Reward order is uniform: block reward first, then uncles in ommer order. Code: Parity engine;
Erigon `:597-617`; Reth `extract_reward_traces`; Besu RewardTraceGenerator.java:95-102 (the
block reward is inserted at index 0); the Geth draft. The block-47 evidence agrees on all nine
builds. The trace-profile "Open details" item "protocol reward ordering" can become a normative
sentence.

Harness gaps:
- `a/filter-page-{0,1,2}` and `filter-past-end-page` (coverage.py:143-167) have no address
  filter, so "skip after matching" versus "skip before matching" is not discriminated.
- All page probes sit inside block 2 of the PoS chain, so neither block boundaries nor rewards
  are crossed.

Add:
- `a/filter-page-filtered`: `{0x2, 0x2, toAddress: [TREE], after: 1, count: 2}`.
- `forks/filter-page-rewards`: `{0x2f, 0x30, after: <#txframes in 47>, count: 3}`. This must
  return block-47 block reward, uncle reward, then block 48's first frame, and would also
  expose Besu and Nethermind's zero PoS reward shifting the page.

Also note in the spec that offsets are only stable for a fixed, numerically resolved range, and
depend on H05 (reward presence) and H29 (precompile emission) being agreed.

## 10. `earliest` resolution: the draft plus the Geth draft conflict with the shared tag definition (A, spec, medium)

`BlockNumberTag.earliest` is defined as "the lowest numbered block the client has available"
(src/schemas/block.yaml:125). Upstream geth `eth_getLogs` resolves it to
`HistoryPruningCutoff()` (eth/filters/filter.go:124-129). The Geth draft trace namespace maps it
to block 0 (trace_namespace.go:202-204 and 292-294, with the comment "uses genesis even when eth_*
resolves earliest to the node's history retention boundary"). Combined with "never replace an
explicit endpoint with a retention boundary; return 4444", a pruned node then fails
`fromBlock: "earliest"`, which is the opposite of what the tag promises.

H32 ("accept resolvable earliest") does not say which. Recommendation: `earliest` follows the
shared tag definition (lowest available); the 4444 rule applies to explicit numbers. The current
fixtures cannot see the difference because they are archive nodes. The pruned fixture could add
`filter-earliest` expecting success from the retention boundary.

## 11. Smaller items

- **D, cosmetic.** Nethermind master has no `Mode` property at all (TraceFilterForRpc.cs:10-24;
  TxTraceFilter.cs is intersection-only). That explains both H03 observations (union behaves as
  intersection; "garbage" is accepted). The proposal should say "add a validated `mode` field",
  not "implement union".
- **D, cosmetic.** Fresh Reth main already has the path `trace_get` (trace.rs:220-242, plus a
  separate `trace_get_index`), latest/latest filter defaults (trace.rs:381-388, with test
  `trace_filter_defaults_to_latest`), and null for a missing replay. The H02, H30 and H06 Reth
  rows describe 2.6.0 correctly but could note that upstream main has converged. The H30
  paragraph citing "pinned Reth … omitted start resolves to block 0" is now historical.
- **A, cosmetic.** Unknown-field policy is inconsistent inside the draft. `TraceFilter` is
  `additionalProperties: false` (reject), while `TraceCall` says unknown fields MUST be ignored.
  Parity (`deny_unknown_fields`, trace_filter.rs:27) and Alloy reject, while Erigon and
  Nethermind accept. Besu shares `FilterParameter` with eth_getLogs, so it accepts `address`,
  `topics` and `blockHash` in a trace_filter and silently ignores them. `{blockHash: X}` becomes
  latest..latest (FilterParameter.java:50-76; TraceFilter never checks `isValid()`).
- **cosmetic.** `after`/`count` are JSON integers (matching Parity `usize`), but Besu (`Integer`)
  and Nethermind (`int`) cap at 2³¹−1, while the schema has no maximum. Bound the schema at
  uint64 or state the minimum supported maximum.
- **B, cosmetic.** `rules.py:133` rebinds the local name `reference` (the helper function) to a
  list inside the `trace_get` branch. It is harmless today, because no later branch for the same
  case calls `reference(...)`, but a latent TypeError.
- **A, cosmetic.** H23's wording "destroyed account" for SELFDESTRUCT is inaccurate after
  EIP-6780, when the account usually survives. "Executing (self-destructing) account" is better.

## Checked and found correct

- **H23 mapping (CREATE creator/result address, SELFDESTRUCT address/refund, reward author on the
  to side only) matches Parity.** `filter.rs:96-121` (including failed CREATE →
  `to_address.matches_all()`) and the harness matcher (rules.py:262-272, coverage.py:148-156)
  encode it faithfully.
- **H02 path semantics match Parity.** db.rs:266-272 compares the full `trace_address`, so `[]` is
  the root. Integer entries were rejected by Parity's `Index` deserializer, so -32602 is
  compatible. Erigon (trace_filtering.go:135-147), fresh Reth and the Geth draft all do full-path
  equality.
- **H04 null/omitted/empty = unrestricted matches Parity** (trace_filter.rs:59-60,
  filter.rs:39-47).
- **count 0 returns `[]` everywhere.** Mempool (unmined) transactions return null from
  `trace_transaction` and `trace_get` (Reth transaction.rs:896-899 returns None for non-hash
  `at`; Erigon uses `txnLookup` on canonical transactions only). Spec wording could say "not in
  a canonical block" rather than "unknown".
- **Reward localization (null transactionHash/transactionPosition, non-null block fields) is
  correct.** Reth (trace.rs:876-893; Alloy serializes nulls), Besu (`@JsonInclude(ALWAYS)`,
  RewardTrace.java:57-71) and Erigon (`newRewardTrace`) all produce it.
- **H30 latest/latest matches upstream geth `eth_getLogs`** (api.go:470-478) and Parity
  (trace_filter.rs:55-56).
