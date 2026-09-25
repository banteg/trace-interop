# Tracked PR review refresh, 2026-09-25

Final snapshot: 2026-09-25T16:40:46.973974+00:00.

This pass follows the [14:48 UTC review](pr-review-continuation-2026-09-25.md). It checked all 65 tracked PRs for new comments, reviews, branch changes and failing checks. Review/comment pagination was complete. For open PRs with more than 100 check contexts, the remaining check runs were fetched through the paginated API; Nethermind #13666 had 606 checks and #13801 had 605.

## Actions

- **[Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666):** the new lint failure was `IDE0005` for the unused `Nethermind.Core.Extensions` import. Commit `91b0dcec85` removes it and addresses the reviewer-requested field-order cleanup. The JsonRpc project and dependencies build with CI's analyzer settings with **zero warnings and zero errors**; changed-file formatting passes. No behavior changed, so the existing socket regressions were not rerun for the import/field-placement cleanup.
- **[Nethermind #13847](https://github.com/NethermindEth/nethermind/pull/13847):** the maintainer suggested replacing the early return plus assignment with `_currentOperation?.Used = gasAvailable`. On merged head `d6d6a4351e`, applying that exact suggestion makes both buffered precompile regression cases fail with `NullReferenceException`; both streaming controls pass. The expanded callback from #13551 would continue to `_currentOperation.Push` after skipping the conditional assignment. The existing early return protects the whole operation update, so it is retained. Restoring it makes all four regression cases pass on the same merged head. Claude Code / Claude Opus 5.5 at high effort independently reached the same conclusion. The PR description now explains the guard and correctly names `ReportGasUpdateForVmTrace` as the current master failure callback. The code was not changed just to satisfy an unsafe optional suggestion.
- **[Nethermind #13801](https://github.com/NethermindEth/nethermind/pull/13801):** the checked Facade crash shared with #13666 is the test assertion “Simulate must be traced through a BlockReceiptsTracer.” Upstream already fixed the test in [#13845](https://github.com/NethermindEth/nethermind/pull/13845), commit `609ad50dd5`, merged at 15:41 UTC. Updated #13801 with a normal merge of master (`46e60de186`), verified the fix is an ancestor, and preserved the approval. No duplicate fix was opened. #13666's new push allows CI to construct a fresh merge against the corrected base.

## New upstream results

- [Nethermind #13551](https://github.com/NethermindEth/nethermind/pull/13551) merged. Its opcode benchmark summary reports no significant regressions or improvements.
- [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213) and [#27217](https://github.com/paradigmxyz/reth/pull/27217) merged.
- #13847 received human approvals and an upstream Claude “good to merge” review. Its formal review decision still requires review after the maintainer's merge; individual approvals do not imply that the current head has passed every gate.
- #13666's upstream Claude re-review found no new correctness blocker. The import and field placement were the new actionable changes.
- Erigon #24291 still has the already-addressed fixture mismatch pending companion rpc-tests #605; the old Silkworm CircleCI failures and Erigon #24032's old CI gate remain unchanged. No new code fix was identified for these checks.

The [machine-readable snapshot](pr-review-refresh-2026-09-25.json) records the final review and branch state. Code and report updates preserve commit history. No full cross-client matrix or new full Nethermind solution test run was performed; upstream CI on newly updated heads remains separate from the local checks above.

Repository validation: 242 tests passed; schema checks and deterministic report regeneration passed. The updated tracker contains 25 open, 38 merged and 2 closed PRs.
