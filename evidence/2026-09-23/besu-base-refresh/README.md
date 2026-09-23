# Besu base refresh — 2026-09-23 UTC

Seven tracked Besu PRs were six commits behind upstream and GitHub reported their
up-to-date gate as `BEHIND`. Each branch now includes
`main@a7867768741ffe7239bab07c38926d065ab16229` through a normal merge.
No force pushes or conflict resolutions were needed.

All seven merges are pushed. [GitHub's refreshed state](github-after-push.json)
reports every head as `MERGEABLE`; the previous `BEHIND` gate is cleared.
Review and [workflow approval](workflows-after-push.json) remain outstanding.

The previous PR head is the first parent of every merge; the upstream head is its
second parent. Each PR's diff against upstream is unchanged after excluding blob
IDs in diff headers (only the shared changelog's IDs differ).

## Native validation

Tests ran sequentially on Fedora with Temurin 25.0.4.1 in an isolated source tree.
Each branch ran Bonsai `TraceJsonRpcHttpBySpecTest`, available
`VmTraceGeneratorTest` and `FlatTraceGeneratorTest` suites, plus
`StreamBackpressureTest` and both HTTP/WebSocket `JsonResponseStreamerTest` suites.
The streaming tests cover the new upstream disconnect-handling changes.
#11347 additionally ran `DebugTraceBlockStreamerPrecompileTest` and core
`DebugOperationTracerTest`. Test outputs were cleaned before every run.

| PR | Merge commit | Tests passed |
| --- | --- | ---: |
| [#11286](https://github.com/besu-eth/besu/pull/11286) | `f9a26052e9` | 843 API |
| [#11345](https://github.com/besu-eth/besu/pull/11345) | `bb4ad7397b` | 846 API |
| [#11346](https://github.com/besu-eth/besu/pull/11346) | `4b11054610` | 843 API |
| [#11347](https://github.com/besu-eth/besu/pull/11347) | `f3edcaf00f` | 845 API + 29 core |
| [#11350](https://github.com/besu-eth/besu/pull/11350) | `6426f704a8` | 844 API |
| [#11352](https://github.com/besu-eth/besu/pull/11352) | `c30d008ac6` | 843 API |
| [#11353](https://github.com/besu-eth/besu/pull/11353) | `320ee27cf4` | 846 API |

All selected tests passed with zero failures, errors or skips. Exact commands,
parents and per-suite counts are in [validation.json](validation.json).
These are focused native tests; full upstream CI still requires maintainer approval.
The Forest trace suite remains disabled upstream. No cross-client matrix was rerun.
