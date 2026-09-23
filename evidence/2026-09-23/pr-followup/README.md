# Tracked PR follow-up — 2026-09-23

The 27 core client fixes comprise **16 open and 11 merged** PRs. Reth #27364,
Reth #27366 and revm-inspectors #511 have merged since the previous tracker snapshot.
The draft specification, Otterscan work and three watched third-party PRs are tracked
separately. [Machine-readable snapshot](status.json) records heads and actions.

## Besu branch refresh and native tests

Each branch was merged with upstream `main@e2c207869cf44e6cc6db3565c59318a4cdd245b7`
without conflicts. Each new commit has the previous PR head as its first parent and
that upstream commit as its second parent. Pushes preserve the existing history.
Tests ran sequentially on Fedora in an isolated build directory using Temurin 25.0.4.1.

| PR | Pushed merge commit | API tests passed |
| --- | --- | ---: |
| [#11286](https://github.com/besu-eth/besu/pull/11286) | [`c00216d5f8`](https://github.com/besu-eth/besu/commit/c00216d5f8a627c25fff88a9a7a381211981d7f9) | 813 |
| [#11345](https://github.com/besu-eth/besu/pull/11345) | [`d787df60ad`](https://github.com/besu-eth/besu/commit/d787df60ad6e334396e6ca29a3864f09930b45dd) | 816 |
| [#11346](https://github.com/besu-eth/besu/pull/11346) | [`3236946fc2`](https://github.com/besu-eth/besu/commit/3236946fc2bad7c3861168dfabb3fa23138098d2) | 813 |
| [#11347](https://github.com/besu-eth/besu/pull/11347) | [`f10f76facb`](https://github.com/besu-eth/besu/commit/f10f76facb967bbeeeed8202e2a939ac2c6ae43f) | 815 |
| [#11350](https://github.com/besu-eth/besu/pull/11350) | [`6aca59ef2e`](https://github.com/besu-eth/besu/commit/6aca59ef2e1d61f59a43612d44f28745ecd8fb0f) | 814 |
| [#11352](https://github.com/besu-eth/besu/pull/11352) | [`76bcc6c494`](https://github.com/besu-eth/besu/commit/76bcc6c494fa1de59794265974160b98cec57a00) | 813 |
| [#11353](https://github.com/besu-eth/besu/pull/11353) | [`012eed7be9`](https://github.com/besu-eth/besu/commit/012eed7be9f9052c477d3287d9bb2581f4e7f3a5) | 816 |

The selected API suites were Bonsai `TraceJsonRpcHttpBySpecTest`,
`VmTraceGeneratorTest` and `FlatTraceGeneratorTest` (where present on each branch).
#11347 additionally ran `DebugTraceBlockStreamerPrecompileTest` and the core
`DebugOperationTracerTest` suite (29 passed). Exact commands and per-suite counts are in the
snapshot. These are targeted native checks, not a complete project suite or a
fresh cross-client capture. The Forest trace suite remains disabled upstream.

## Review and CI actions

Eight Nethermind threads requesting implemented fixes were verified against the
current heads and resolved: four in #13666, one in #13667, one in #13676 and two
in #13677. Three rationale threads remain for reviewer confirmation: helper
refactoring in #13676, and the preflight/pruning window and exact error assertion
in #13677. #13667 remains stacked on #13665.

The upstream repositories grant this account read access, so workflow approval and
reruns require maintainers. The formal Besu reviewer-request API returned 404;
review was requested in the PR follow-up comment instead. The snapshot retains the pre-follow-up workflow observations;
`action_required` is not a successful test result. Review/CI requests were posted:

- [NethermindEth/nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666#issuecomment-5791970151)
- [alloy-rs/evm #411](https://github.com/alloy-rs/evm/pull/411#issuecomment-5791970484)
- [paradigmxyz/reth #27378](https://github.com/paradigmxyz/reth/pull/27378#issuecomment-5791970817)
- [paradigmxyz/reth #27217](https://github.com/paradigmxyz/reth/pull/27217#issuecomment-5791971158)
- [ethereum/execution-apis #895](https://github.com/ethereum/execution-apis/pull/895#issuecomment-5791971473)
- [besu-eth/besu #10953](https://github.com/besu-eth/besu/pull/10953#issuecomment-5791971795)
- [NethermindEth/nethermind #13622](https://github.com/NethermindEth/nethermind/pull/13622#issuecomment-5791972160)
- [besu-eth/besu #11286](https://github.com/besu-eth/besu/pull/11286#issuecomment-5792147400)

Reth #27217's four underlying failures occur in setup-mold archive extraction before
compilation or tests. The unit and lint workflow reruns were requested; no test
failure was inferred from their summary jobs.

For watched Besu #10953, a merge-tree check against the same upstream commit found
only a `CHANGELOG.md` conflict. For Nethermind #13622, the author was asked to add
CALL-then-STOP coverage, clarify stale child return data and investigate the failing
no-intrinsics `walletReorganizeOwners_Paris` case (2538/2539 passed; gas and state
mismatches). Its cause has not been established. Nethermind #13551 has no outstanding
action from this check beyond review and subsequent behavior validation.

## Dependency uptake

Reth `main@0a1d3e761230b88271a481b94b6957a3f0f50bfc` still locks
`alloy-rpc-types-trace 2.4.2`, `revm-inspectors 0.43.0` and `alloy-evm 0.39.0`.
Merged Alloy #4216/#4218 and inspectors #509/#510/#511 require dependency uptake
before new Reth observations can verify them. Alloy EVM #411 and Reth #27378 remain
open and need both merge/release coordination and a development-build rerun.

The frozen cross-client captures and generated reports were not changed by this
maintenance pass. Merged, locally tested, CI-approved and released are separate states.
