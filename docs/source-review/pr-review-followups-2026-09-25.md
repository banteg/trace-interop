# Tracked PR review follow-ups, 2026-09-25

Reviewed all 60 PRs tracked at the start of this pass, including merged and closed entries. The live GitHub snapshot at 09:59 UTC contained 28 open, 30 merged, and 2 closed PRs. Three follow-up PRs were subsequently added to the ledger. Attached bug documents supplied evidence and context, not authorization to perform unrelated work.

## Actionable reviews

| Parent | Resolution | Published follow-up |
| --- | --- | --- |
| [Nethermind #13551](https://github.com/NethermindEth/nethermind/pull/13551) | Remove the VM's concrete cancellation-tracer lookup and completion-time cancellation polling. Keep the emitted-start flag; the outer cancellation wrapper owns deferral across all observers. Add implicit STOP/filter, canceled-start VM reuse, CALL/CREATE result-push, and implicit-STOP fan-out regressions. Consolidate completion helpers and clarify callback documentation. | [#13835](https://github.com/NethermindEth/nethermind/pull/13835), targeting `trace-callback-ownership` |
| [Nethermind #13622](https://github.com/NethermindEth/nethermind/pull/13622) | Cover a child REVERT with bytes before root STOP/RETURN; remove requested comments and document the action-revert collection. The contract concerns custom tracer callbacks, not a new built-in RPC output change. | [#13834](https://github.com/NethermindEth/nethermind/pull/13834), targeting `correct-top-level-action-output` |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666) | Restrict recovery to deferred execution, consolidate state into one internal context, use a bounded pooled array, preserve the first socket failure, terminate idle notification receivers, and document rewind invariants. | Updated existing branch at `e774a5039b`; see the [performance comparison](engine-streaming-performance-2026-09-25/README.md). |
| [Erigon #24032](https://github.com/erigontech/erigon/pull/24032) | Move same-canonical-head validation and durable marker updates out of `unwindIfNeeded`; remove the marker-update flag; use `sameExecutedBlockNum`; trim comments without changing finality or write-lock behavior. | [#24322](https://github.com/erigontech/erigon/pull/24322), targeting `test/unwind-catchup-crash-recovery` |

The three parent branches belong to upstream repositories, so follow-ups target those branches from the user's forks. No force pushes or history replacement.

## Design decisions

### Cancellation and instruction pairing

The VM tracks whether it emitted an instruction start and closes that instruction exactly once. Cancellation policy belongs to `CancellationTxTracer`, placed around the complete observer graph. A new public interface or VM knowledge of a concrete wrapper is unnecessary. Checking cancellation after each implicit-STOP observer completion breaks fan-out: the first observer can cancel before the second observer receives its completion. The new regression fails on submitted head `430c33df1f` and passes after the redesign.

The gas-update callback remains separate from instruction completion: it updates a resumed CALL/CREATE operation and reports failure gas when no instruction is open. Filtering must not create a completion for an omitted start. The CALL/CREATE result push is checked for both collected and streaming Parity traces.

### Deferred execution versus direct serialization

`IStreamableResult` is shared by deferred trace execution and efficient serialization of already-computed Engine results. Recovery is now an internal opt-in marker for the former. The public streamable and transport-sink interfaces remain unchanged. The public streaming base class carries the internal marker for derived trace implementations; unrelated third-party streamables do not automatically gain recovery.

A single optional internal context retains the service/request mapping information and owns final metric reporting. The original response retains module-rental ownership. The processor enables reporting; the writer records exactly one completed outcome. Request cancellation is excluded, while a non-request-cancelled failure after commitment counts as an error.

Deferred unbuffered responses stage at most 16 KiB in one rented array. Fully buffered HTTP rewinds the existing append-only buffer. Engine payloads/blobs/bodies and logs receive the original transport writer, eliminating the extra staging object, rental, prefix copy and forwarding on those paths. Reserving destination memory without advancing would require stronger lifetime and rollback guarantees than the general PipeWriter contract; it is unnecessary once the recovery policy is scoped correctly.

After commitment, a failure aborts the response rather than appending an error. A failed socket notification faults the shared send lock before releasing it, retains the first cause, then cancels the receive loop after release. The receive loop surfaces an IOException with the original cause even when the underlying WebSocket stream converts cancellation into a closed result. A missing notification response is rejected before acquiring/faulting the lock.

## Validation

- #13551: full normal EVM suite 12,606 passed / 8 skipped; checked `TRACE;DEBUG` configuration 12,604 passed / 8 skipped; no failures. The implicit-STOP fan-out regression fails on the submitted VM.
- #13622: full EVM suite 12,628 passed / 8 skipped; both added child-REVERT cases fail when the old return-data-buffer argument is restored.
- #13666: full JSON-RPC suite 2,428 passed / 22 skipped; 120 HTTP Startup tests, 436 Engine direct-response serialization tests, and 634 Core JSON tests passed. The final socket/response-writer follow-up passes all 63 selected cases; both notification-shutdown variants fail without the diagnostic fix and pass with it.
- #24032: `make lint` reports zero issues; `make erigon integration` succeeds; repeated-forkchoice, catch-up/crash-recovery and unwind tests pass in execution/execmodule and execution/engineapi. The engineapitester package builds but contains no tests matching that selection. A larger local build exhausted temporary disk space; final builds and recovery validation completed on Fedora.
- Nethermind validation used .NET SDK 10.0.300 on Fedora. Changed-file whitespace checks and `git diff --check` were run. Erigon used Go 1.27.1 on Fedora.

Claude Code / Claude Opus 5.5 at high effort supplied two read-only design/review iterations for #13551 and #13666, plus a final review of #13622. It did not run tests; the test results above came from Codex-run validation. The final reviews found no correctness blockers. Small helper/docs findings and the receive-loop diagnostic issue were addressed.

## Other tracked activity

The initial sweep found no additional unaddressed review requests requiring code changes in the remaining tracked PRs. Complete refreshes of all 63 entries at 10:55 and 11:09 UTC found no further actionable code-review changes; comment, review, thread and nested-comment pagination was checked for truncation. #13800 is approved. #13801's genesis parser-validation/TraceStore concerns and #24291's nonce-overflow feedback were already addressed on their current heads. Newly merged work includes Erigon #24255/#24290/#24294/#24295, Nethermind #13779, revm-inspectors #528 and Reth #27429. Erigon #24032 is now draft. The maintainer also converted follow-up #24322 to draft pending #24032 merging; that status is preserved. The ledger previously still marked Nethermind #13779 and Reth #27429 open.

Claude also raised a pre-existing possible top-level failing-precompile null dereference in Parity vmTrace. That was a static lead, not demonstrated by this review; it was not folded into the cancellation follow-up or reported as a confirmed new regression.

## Publication and proof limits

Follow-up commits: Nethermind #13835 `0bdca3b4fc`, #13834 `288d4656cd`, #13666 `e774a5039b`; Erigon #24322 `ec859cb36ad`. The follow-ups address review feedback; they do not imply upstream approval or merge. #13666 still requires maintainer re-review. Erigon CI was still running at publication; the Nethermind follow-up branches only triggered metadata workflows, so the Fedora suite results are the available execution evidence. No full cross-client matrix or full Nethermind solution run was performed.

## Engine performance result

The [three-revision comparison](engine-streaming-performance-2026-09-25/README.md) covers 28 real-HTTP Engine direct-response cases, twice in opposite arm orders. Revised versus base median case ratios: allocation +0.040%, throughput +0.117%, p50 latency +0.022%, p95 latency −1.256%. Small-response extra allocation falls from roughly 432–456 B/request to typically about 24 B/request. The direct-writer identity test confirms Engine avoids the recovery wrapper. Individual timing cases remain noisy on the shared host, so these results do not certify a strict per-case zero-regression merge gate. Raw measurements and exact reproduction patches are retained with the report.
