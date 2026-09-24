# Source review, 2026-09-24

A review of the draft against the original Parity implementation, current client source, the sibling
`eth_*`/`debug_*` specifications and this harness's own oracles. It asks three questions:

1. Where is the current recommendation wrong, underspecified, or inconsistent with the sibling methods?
   Where does it keep a Parity wart that a specification should fix, or "fix" something at an
   unjustified compatibility cost?
2. Where do our assertions, oracles or fixtures measure clients wrongly (false positives, false
   negatives, cases that don't discriminate what they claim)?
3. Which client behaviours are genuine bugs or divergences that no case covers?

**Status: unreviewed proposals.** Nothing here has been applied to the [ledger](../../decisions/README.md),
the pinned specification or the harness. The ledger remains the source of truth. Each finding needs
review before it changes a recommendation or a verdict.

## Reports

| Area | Decisions | Report |
| --- | --- | --- |
| Filters and lookup | H01–H06, H23, H27, H30, H32; pagination, rewards, tags | [filter-selection.md](filter-selection.md) |
| Simulation requests | H11–H16, H25, H31, H32 | [simulation.md](simulation.md) |
| Call-trace frames | H07–H10, H22, H24, H29 | [call-trace.md](call-trace.md) |
| stateDiff | H16–H18, H26, H28 | [statediff.md](statediff.md) |
| vmTrace | H19–H21, `sub` | [vmtrace.md](vmtrace.md) |

Each report ranks its findings and marks each with its kind (disagreement, harness bug, missed issue,
stale ledger claim), confidence, and whether it would change the specification or a verdict. Each
report ends with the items checked and found correct.

## Reviewed revisions

| Source | Revision |
| --- | --- |
| Parity/OpenEthereum | [`55c90d40`](https://github.com/openethereum/parity-ethereum/tree/55c90d4016505317034e3e98f699af07f5404b63) |
| Besu main | [`07f0a4b2`](https://github.com/besu-eth/besu/tree/07f0a4b2f832257842db71eacf4bca584f87fafe) (2026-09-22) |
| Erigon main | [`3b4861d1`](https://github.com/erigontech/erigon/tree/3b4861d10387ca3e19f7b16d1b8c0ec1fcd616cd) (2026-09-22) |
| Nethermind master | [`ac02224f`](https://github.com/NethermindEth/nethermind/tree/ac02224f25fd4901116ebf2643d522ec4a0e60a1) (2026-09-22) |
| Reth main | [`861a5616`](https://github.com/paradigmxyz/reth/tree/861a56167cd4eee8ed66e2bfb5d54a6b0620b40d) (2026-09-24); locks revm-inspectors 0.43.0 and alloy-evm 0.39.0 |
| revm-inspectors main | [`aac35449`](https://github.com/paradigmxyz/revm-inspectors/tree/aac35449a4cacfe4c71477211a383c719acbf904) (2026-09-24, unreleased after 0.43.0) |
| Geth draft fork | [`fa8ecb92`](https://github.com/banteg/go-ethereum/tree/fa8ecb9242dda61858c44cf43c70d00548fbd7cd); upstream files serve as the `eth_call`/`eth_getLogs` reference |
| Draft specification | [execution-apis `b979aefe`](https://github.com/banteg/execution-apis/tree/b979aefe57e4f63af0397b5a068237c04a9d6e3b) (pinned); sibling eth/debug specs at `e38fc96c` |

Line citations refer to these revisions, except where a report names another revision (for example a
released build or a cargo registry crate). Evidence comes from `evidence/2026-09-24/h15-call-compat`,
the active report set. The call-trace review also reads `evidence/2026-09-24/current-matrix`.
[`scripts/compare_responses.py`](../../scripts/compare_responses.py) prints one case's output for
every build (`show`) or groups builds whose output differs (`groups`).

## Independently re-checked

These claims were re-read in source or recomputed from evidence after the reports were written. The
remaining claims rest on the reports' own citations.

| Claim | Check |
| --- | --- |
| `eth_getLogs` requires -32602 for beyond-head and reversed ranges, not the draft's -32001 | `src/eth/filter.yaml:153-160` at b979aefe |
| Nethermind `trace_filter` breaks out of the block loop and returns partial success when a block or parent lacks state | `TraceRpcModule.cs:299-346` |
| Erigon `trace_call` drops `input` | `TraceCallParam` (`trace_adhoc.go:66-79`) has only `data`; Go JSON ignores unknown keys |
| The fee oracle requires one specific violation when a request violates two | `fee_policy.py:98-103` and the `kind == violation` check in `assess` |
| Erigon, Reth and the Geth draft already emit `result` on REVERT frames | revm-inspectors `types.rs:331-336`; frame `[1]` of `initial/call-many-priced` |
| Besu `trace_callMany` second call is 5,600 gas cheaper than on every other build | `initial/call-many-priced`: Besu root 124,547 vs 130,147 |
| Besu `TraceCallMany` never marks transaction boundaries | `markTransactionBoundary()` appears only in `TraceBlock`, `TransactionTracer` and `BlockTracer` |
| The Geth draft emits `+`/`-` for zero-to-value storage slots, and the harness accepts it | `trace_capture.go:245-251`; `rules.py:319-321`; `a/many-storage-write-read` |
| Erigon's vmTrace includes MLOAD in `mem` | `trace_adhoc.go:595` |
| Nethermind traces DUPn before moving the stack head | `EvmStack.cs:2085-2100` |

## Highest-impact findings

These are proposals, grouped by the question they answer. Details and citations are in the reports.

**Recommendations to reconsider**

- `trace_filter` range errors should follow `eth_getLogs` (-32602, no clamping), and range bounds should
  use `BlockNumberOrTagForRange`. [filter-selection §1](filter-selection.md)
- H20's written-bytes `mem` rule departs from Parity and from every established client for MLOAD.
  Define `mem` as the post-operation contents of the operand-designated range. [vmtrace A1](vmtrace.md)
- H09: `result` on REVERT frames already matches Erigon and Reth. The new part is failed CREATE, and an
  explicit null for other failures adds nothing. [call-trace A2](call-trace.md)
- H15 fee defaults are settled by unanimous `eth_call` behaviour and `eth_simulateV1`.
  [simulation §1](simulation.md)
- Reuse `eth_simulateV1` codes and the execution-apis error groups instead of a single -32003.
  [simulation §3](simulation.md)
- Schema-defined call fields must be honoured or rejected, never silently ignored.
  [simulation §12–13](simulation.md)
- Reserve parameter positions for state and block overrides, and accept block hashes.
  [simulation §5, §14](simulation.md)

**Unspecified behaviour where clients split**

- Frame gas numbers and `from`/`to`/`value` per call type. [call-trace A1](call-trace.md)
- Frames for calls that fail their precheck. [call-trace A4](call-trace.md)
- `creationMethod` and error labels. [call-trace A3, A5](call-trace.md)
- Implicit STOP, failing-op `ex`, `push` arity and order, and a non-null vmTrace for EOAs. [vmtrace A2–A6, B6](vmtrace.md)
- stateDiff existence, account inclusion and storage markers; `{}` for deleted accounts; blob fees;
  exclusion of block-level operations. [statediff §2, §5, §6, §8, §9](statediff.md)
- callMany transaction boundaries and first-call state. [statediff §1, §4](statediff.md)
- Genesis, `pending` block selectors, reward ordering and `earliest`. [filter-selection §4, §6, §9, §10](filter-selection.md)

**Harness bugs**

- Fee-oracle multiple-violation false positives. [simulation §2](simulation.md)
- Storage `+`/`-` and `=` accepted. [statediff §2, §5](statediff.md)
- H21 checks only `push`. [vmtrace B1](vmtrace.md)
- vmTrace `null` for EOAs accepted. [vmtrace B2](vmtrace.md)
- Failed CREATE `result.address` used as a filter recipient. [call-trace B2](call-trace.md)
- Latent issues in the H18 multi-authorization, H17 bundle-existence and H16 blob-fee oracles.
  [statediff §7, §8, §10](statediff.md)
- `anchored_reference` hides field mismatches. [call-trace B3](call-trace.md)

**Client issues without coverage**

- Besu:
  - `trace_callMany` original storage values. [statediff §1](statediff.md), [call-trace C1](call-trace.md)
  - Block replay skips pre-block system calls. [statediff §3](statediff.md)
  - Fabricated CALL `mem`. [vmtrace C4](vmtrace.md)
- Nethermind:
  - Filter truncation. [filter-selection §3](filter-selection.md)
  - DUPn arity and `store` gated on stateDiff. [vmtrace C1–C3](vmtrace.md)
- Rewards unreachable through `toAddress` in Besu and Nethermind. [filter-selection §2](filter-selection.md)
- Reth genesis reward. [filter-selection §4](filter-selection.md)
- Erigon historical callMany state. [statediff §4](statediff.md), [simulation §16](simulation.md)
- Revm-inspectors `store` regressions on main. [vmtrace C8](vmtrace.md)

## Reviewing these findings

Re-read the cited lines at the listed revision before relying on a claim. Line numbers drift, and some
citations come from source reading alone, without runtime evidence. Where a report proposes a fixture,
the prediction is untested until a capture runs. When a finding is accepted, rejected or superseded,
record the disposition in the relevant decision rather than editing these reports, which describe the
state on 2026-09-24.
