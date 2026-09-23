# PR review follow-up — 2026-09-23

Live status refreshed at **2026-09-23 19:49:35 UTC**. The core tracker remains **17 open, 11 merged** client PRs. The companion QA fixture PR and draft specification are counted separately. [Snapshot](status.json) records immutable heads, review decisions, check summaries, nonpassing checks and workflow approval gates.

## Changes pushed

All pushes were fast-forward updates. The empty-selection branch received a normal merge of its prerequisite; no history was rewritten.

| PR | Pushed head | Focused validation |
| --- | --- | --- |
| [Nethermind #13665](https://github.com/NethermindEth/nethermind/pull/13665) | `064563fcee` | [86 tracer](review-output-final.log) + [25 TraceStore](review-output.log) |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666) | `d743282fd4` | [379 RPC/service/socket + 104 HTTP](review-stream-final.log) + [35 log](review-stream-logs.log) |
| [Nethermind #13667](https://github.com/NethermindEth/nethermind/pull/13667) | `261883f2b7` | [86 trace RPC + 29 TraceStore](review-empty.log) |
| [Nethermind #13676](https://github.com/NethermindEth/nethermind/pull/13676) | `2b1eba31c6` | [41 RPC/helper](review-get.log) + [4 TraceStore](review-get-names.log) |
| [Nethermind #13677](https://github.com/NethermindEth/nethermind/pull/13677) | `f8c4ecfc6a` | [64 filter/helper](review-filter-final.log); [33 filter cases rerun after allocation change](review-filter-allocation.log) |
| [Erigon #24255](https://github.com/erigontech/erigon/pull/24255) | `b804487ea4` | [Focused trace_filter tests](review-erigon-filter.log), [lint and erigon/integration builds](review-erigon-exact.log) |
| [rpc-tests #604](https://github.com/erigontech/rpc-tests/pull/604) | `8a4ef8afce` | Three fixtures: only mode=union added; responses unchanged |
| [execution-apis #895](https://github.com/ethereum/execution-apis/pull/895) | `89b54f807c` | CI spellcheck container passed |

The spec validation used `docker run --rm -v <checkout>:/github/workspace -w /github/workspace jonasbn/github-action-spellcheck:0.29.0`: spelling passed. Only `MLOAD`, `Erigon's`, `idx` and `mem` were added to the wordlist. The new fixture PR preserves the original expected JSON and makes the existing union intent explicit.

Nethermind tests ran on Fedora with .NET SDK 10.0.300, using `dotnet test --project <project> -c release -- --filter <fixture>`. The logs retain exact test counts; build warnings concern missing source-link metadata in transferred checkouts. Changed-file formatting checks pass for the get/output/streaming follow-ups. Filter formatting identified and corrected the two new initializer lines; pre-existing unrelated whitespace findings in the same test file were left intact.

## What was addressed

- **#13677:** one request timeout begins before range/state preflight, is checked between lookups, and survives into buffered/deferred execution. A single block/parent list removes the temporary reference array. Tests share state-availability setup and group independent assertions.
- **#13666:** internal write outcomes drive HTTP 503 and final call reports. Streamed success/error metrics wait for execution. Fully buffered HTTP stages the current response in a recyclable stream and preserves prior batch items and their byte count. Serialization exceptions cannot become appended request-parse errors, and failed batches are not completed. Public stream and sink interfaces are unchanged.
- **Socket policy:** early failures produce valid errors and keep the connection usable. Already-committed partial messages cannot be repaired; late failures end the connection, including WebSocket subscriptions. Real WebSocket single/batch tests exercise both outcomes. The PR release note documents this behavior.
- **#13665/#13667:** move tracer-only tests, share response serialization, make receipt tracing invariant explicit, and propagate changes into the stacked PR. Pre-EIP-658 receipt callback state-root work is disclosed.
- **#13676:** share timeout test setup with Eth tests and consolidate position coverage. Non-generic `Result` has no `IsError` on this base, so the existing boolean conversion is used. The public extraction helper keeps its signature.
- **Erigon:** correct the MCP default description. [rpc-tests #604](https://github.com/erigontech/rpc-tests/pull/604) fixes the three legacy union requests behind nine QA mismatches.

22 additional implemented-fix review threads were verified and resolved. Rationale threads remain for reviewer confirmation; thread resolution is not maintainer approval.

## Remaining external gates

- Sixteen core PR heads need maintainer workflow approval; labels/DCO alone are not test results. #13677 still has a changes-requested review until the reviewer rechecks the fixes.
- **Nethermind #13668:** current debug EthereumTests build stalled for 900 seconds; ARM TxPool failed `OverflowStorage_ReusesBoundedCapacityAcrossRepeatedBursts(8192,6)`. Reruns of runs 35768284413 and 35768284699 were rejected with `Must have admin rights to Repository`. The preceding #13665 head's Trie failure (run 35769533162) received the same rejection. No unrelated test was changed or declared flaky.
- **Erigon QA:** merge/release #604 and advance the current v2.28.0 corpus pin before a maintainer reruns mainnet integration. The separate networking CI failure `TestRequestContextCancelClosesEstablishedStream` passed [ten local repetitions under -race](review-erigon-race.log); that does not replace upstream CI.
- The spec's new-head workflows also require approval. The new QA PR awaits review.
- Watched third-party work is unchanged: Nethermind #13622 retains its no-intrinsics failure; #13551's test checks pass (the snapshot also retains a failed workflow-dispatch benchmark); Besu #10953 awaits CI approval. Reth #27217 retains its previously identified setup-mold failures. Silkworm #2885 remains draft with external CircleCI resource-class failures and its full native-build gate.

## Dependency refresh

Reth `main@58a51b3ee3f6714ded9207b244a273c8afb592fd` now locks `alloy-rpc-types-trace 2.5.0`. GitHub ancestry comparisons confirm the v2.5.0 tag contains both Alloy #4216 and #4218. Filter-default and reward-field behavior can now be retested on that Reth head.

`revm-inspectors 0.43.0` and `alloy-evm 0.39.0` are still locked. The inspector fixes still need uptake, and the system-call error chain still needs Alloy EVM #411 plus Reth #27378.

This pass ran native regressions and refreshed PR state. It did not rerun the cross-client matrix or replace any frozen captures.
