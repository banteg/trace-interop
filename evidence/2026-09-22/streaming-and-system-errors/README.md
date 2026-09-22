# Trace cancellation and system-call errors

These fixes preserve existing error handling; they do not choose new cross-client semantics.

| Patch | What it fixes | Validation |
| --- | --- | --- |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666), follow-up `aa8b23ffd2` | Cancelled trace execution no longer returns normally and lets the response writer finish a partial success. Early timeouts use the existing error mapping; committed output and transport cancellation propagate. | Six cancelled-timeout regressions fail before the fix. All 179 selected streaming, service and response-ID tests pass afterward, including expired requests and transport disconnects. |
| [Alloy EVM #411](https://github.com/alloy-rs/evm/pull/411) | Fatal database failures in system calls retain their source type and diagnostic context as internal execution errors. Nonfatal errors, reverts and halts keep their existing handling. | Six real-EVM regressions fail before the fix. Default and no-default-feature workspace runs each pass 61 unit tests and one doctest; 12 existing doctests remain ignored. All-target/all-feature nightly Clippy passes. |
| [Reth #27378](https://github.com/paradigmxyz/reth/pull/27378) | Pruned-history errors inside execution wrappers use the existing `4444` response, including the BAL database wrapper. Other internal failures keep their code and message. | The regression fails before the fix; all 50 package tests pass afterward. Package Clippy, documentation and nightly formatting pass. Full-workspace all-feature Clippy stops at a missing LLVM 22 dependency. |

Reth's system-call path needs **both** the Reth patch and uptake of the Alloy fix.
The [earlier pruning run](../reth-main-534c60db/README.md) remains the recorded client observation.
No cross-client matrix was rerun on unmerged branches. Retest the affected trace methods once both changes are in a development build.

Exact revisions, commands and limits are in [validation.json](validation.json).
