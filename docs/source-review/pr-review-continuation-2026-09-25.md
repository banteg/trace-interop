# Tracked PR continuation, 2026-09-25

Final complete snapshot: **2026-09-25T14:48:15.481125+00:00**, **65 PRs** (28 open, 35 merged, 2 closed). All comment, review, thread and nested-comment pagination checks were complete. See the [machine-readable snapshot](pr-review-continuation-2026-09-25.json).

This pass continued the [earlier review](pr-review-followups-2026-09-25.md), refreshed every tracked PR (including merged and closed entries), investigated failed checks, and reproduced the remaining precompile lead. Claude Code / Claude Opus 5.5 at high effort supplied a socket-lifecycle review and two precompile design/review iterations. Those were read-only source reviews; the test results below came from Codex-run validation on Fedora with .NET SDK 10.0.300.

## Published fixes

### Nethermind #13666: reconcile upstream socket disposal

[The PR](https://github.com/NethermindEth/nethermind/pull/13666) failed its CI merge build with `CS0102`: upstream added an integer `_disposed` flag for idempotent subscription disconnects while the PR already had a boolean flag protecting cancellation-source disposal. Three inspected jobs reported the same duplicate-field error.

Commit `90d920312028f72364b7a6c9ef96fc492504d68e` merges master `0ba8d5faeea054234f5dab8239c2dd39d8dbd18f` into PR head `3c2f67004e4a3e6a2fdae2e0c6f6c0a80999cbe1`. It uses one atomic idempotency flag and retains the lock that serializes `CancellationTokenSource.Cancel` against `Dispose`. A regression disposes the client concurrently while a notification has written only a prefix, checking one `Closed` event and no message extension or terminator. Existing maintainer changes, including return of the staging rental before pre-commit cancellation, are preserved. No history was rewritten.

Validation: full JSON-RPC suite **2,613 passed / 22 skipped**; after adding the concurrent-disposal test, **38 socket tests passed**; **120 HTTP Startup tests passed**. Changed-file whitespace validation passes. Claude found no race introduced by this merge. Its separate observations about pre-existing semaphore teardown and WebSocket disposal were not reproduced here and are not claimed as confirmed defects or as fixed.

### Erigon #24291: update seven obsolete SELFDESTRUCT fixture values

[The mainnet integration run](https://github.com/erigontech/erigon/actions/runs/36113793384) failed two fixtures across HTTP, compressed HTTP, and WebSocket, in both attempts. The differences were exactly seven SELFDESTRUCT `sub` values that still expected an empty child frame.

[Companion rpc-tests #605](https://github.com/erigontech/rpc-tests/pull/605), commit `2f5592235b01b6ece57d7027df876ae8a720469e`, changes these to `null`: one operation in block 10,000,000 (`test_22`) and six in block 7,345,007 (`test_29`). Both complete revised response objects equal the actual CI responses. Every other JSON byte is preserved; the archives retain their member metadata and bzip2 format and were reopened to verify the payload. Requests, action traces, gas accounting and state diffs do not change. The [validation manifest](pr-review-continuation-2026-09-25-fixtures.json) records paths and transaction hashes.

The fixture PR remains draft until [Erigon #24291](https://github.com/erigontech/erigon/pull/24291) lands. Updating the expectations before that would make old client behavior fail. The client PR description now links the companion and corrects its earlier statement that no fixture covered the case. No fresh full mainnet replay was run locally; the complete CI response comparison is the validation evidence.

### Nethermind: failed top-level precompile vmTrace

The previous static lead is now a confirmed bug. A serialized `trace_call` to Blake2F with empty input and `vmTrace` selected fails in the buffered tracer because the precompile has no opcode and `_currentOperation` is null. On master `0ba8d5faee`, both buffered cases (`vmTrace` alone and with `trace`) fail at `ReportOperationRemainingGas`; both streaming controls pass.

[Nethermind #13847](https://github.com/NethermindEth/nethermind/pull/13847), commit `ade7a659cb26daf069070ef13b5146f53d0b39cc`, ignores gas updates when there is no operation, matching the streaming tracer. It guards both `ReportOperationRemainingGas` and `ReportGasUpdateForVmTrace`, without changing VM callback order or adding tracer interfaces. The second guard matters for #13551's callback redesign: on `ec0ff7df4256f9a3ef60b9f3efb686e9a838b434`, the same two buffered cases instead fail at `ReportGasUpdateForVmTrace`. This establishes why a guard in only the old callback would be incomplete.

Validation on master: full JSON-RPC suite **2,508 passed / 22 skipped**, full EVM suite **13,608 passed / 20 skipped**. After the final test cleanup, all **143 trace RPC tests passed** and changed-file whitespace validation passed. On the #13551 compatibility tree, the two previously failing buffered cases plus both streaming controls pass (**4/4**). Its later merge `70da9f546b9f8511c1c94dbd889e2afbea09963f` leaves the gas callbacks unchanged; that newer whole tree was not retested. The tested [compatibility patch](pr-review-continuation-2026-09-25-evidence/precompile-13551-compat.patch), based on `ec0ff7df42`, preserves #13551's additional push/finalization logic. The PR description explicitly calls out retaining the guard when the branches merge.

## Other tracked activity

- Nethermind #13622, #13834 and #13835 merged; #13551 is approved. Its maintainer subsequently simplified cancellation deferral to a stateless rule in the wrapper. The retained no-instruction gas update is required by its existing failing-precompile gas regression.
- Nethermind #13800 merged during this pass.
- New review feedback on #13801 asked to move trace-type validation to the live fallback. Maintainer commit `bf3ba1396cf4ce284838b57c8818469452cf8920` does this before receipt/header/state lookup and restores TraceStore delegation, with tests for an unknown hash and delegation. Source review found the change addresses the request; it was not independently retested here. The PR is now approved.
- Erigon #24322 remains draft pending #24032. No new code action was identified there.
- Silkworm #2885's three failed CircleCI jobs (72299, 72300, 72301) date to September 13 and each exposes only `Error: Task information unavailable`, a canceled step, and no exit code. The available API output cannot establish a source failure; the output endpoint returned 404. They were not treated as demonstrated code regressions.

No full cross-client matrix or full Nethermind solution run was performed. CI and merge state remain separate from the local validation results.

Read-only Claude reviews are retained in the [evidence directory](pr-review-continuation-2026-09-25-evidence/). Their conclusions remain source-review judgments, separate from the executable validation above.

At publication, #13666 is mergeable at `90d9203120` and still has the stale formal changes-requested review. Its new head has only two successful metadata checks; no full CI rerun has completed for that head. Local test passes must not be read as a green upstream CI result. The two new PRs remain open; rpc-tests #605 intentionally remains draft.

The trace-interop repository check passed: 239 tests, schema checks and deterministic report regeneration. The ledger and generated client/decision reports were refreshed together.
