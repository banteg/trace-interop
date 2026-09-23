# Client fixes

Upstream changes arising from the trace comparison. Status checked **2026-09-23**.
A merged patch, a tested build and agreement with the proposed API are separate milestones.
The [client reports](../reports/README.md) describe the behavior; this page tracks the work to change it.

**17 pending · 11 merged**

## Pending

The full workflows on these 17 PRs are awaiting maintainer approval. Passing DCO
and label checks do not establish that the test workflows passed. Review and CI
follow-ups are recorded in the [2026-09-23 status snapshot](../evidence/2026-09-23/pr-followup/README.md).

### Erigon

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Erigon #24255](https://github.com/erigontech/erigon/pull/24255) | Default address filtering to AND, retain explicit modes, fix empty-side intersection and reject unknown modes ([H03](../reports/decisions/H03.md)) | [Native validation](../evidence/2026-09-23/erigon-h03/README.md): ten regression subtests fail before the fix; all 649 top-level JSON-RPC tests pass, as do lint and both binary builds. Migration guidance documents explicit union for both-list activity queries. CI approval, review and a post-merge matrix retest remain. One pre-existing documentation assertion is disclosed in the PR. |

### Besu

All seven branches were refreshed with merge commits from `main@e2c207869c`,
preserving their history. The [follow-up validation](../evidence/2026-09-23/pr-followup/README.md)
records the pushed heads and targeted Fedora results. Counts in individual rows
below describe the earlier regression proofs.

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Besu #11286](https://github.com/besu-eth/besu/pull/11286) | Include MCOPY memory updates ([H20](../reports/decisions/H20.md)) | The [checked builds](../reports/cases/a/call-mcopy.md) still omit the write. The PR has a native regression test; obtain review and retest after merge. Supersedes closed #11285. |
| [Besu #11345](https://github.com/besu-eth/besu/pull/11345) | Keep sibling and handled precompile failures local ([H24](../reports/decisions/H24.md)) | Regressions cover both sibling orders and all four CALL variants. Seven unit tests and 809 HTTP trace fixtures pass. Review and matrix retest remain. |
| [Besu #11346](https://github.com/besu-eth/besu/pull/11346) | Preserve root precompile return bytes ([H22](../reports/decisions/H22.md)) | Unit regression reproduced the missing bytes. Three unit tests and 810 HTTP trace fixtures pass, including a new identity-precompile fixture. Review and matrix retest remain. |
| [Besu #11347](https://github.com/besu-eth/besu/pull/11347) | Preserve errors from failed root precompiles ([H09](../reports/decisions/H09.md)) | A regression reproduces the lost exceptional-halt reason. After the fix, 29 tracer tests, one flat-trace test and 810 HTTP trace fixtures pass, including invalid bn128Add input. This covers root precompile error reporting, not every H09 difference. Review and matrix retest remain. |
| [Besu #11350](https://github.com/besu-eth/besu/pull/11350) | Remove fabricated CALL memory writes from `vmTrace` ([H20](../reports/decisions/H20.md)) | Real-EVM HTTP tests reproduce parent RETURN bytes being attributed to earlier CALL/DELEGATECALL operations. Four cases cover zero output and real writes at offset 32; all 813 active HTTP trace tests pass. Corrected 45 fabricated memory deltas in 27 existing fixtures. The upstream Forest suite remains disabled. |
| [Besu #11352](https://github.com/besu-eth/besu/pull/11352) | Preserve VM frame ownership, child bytecode and CALL resumption gas after omitted opcodes | Three real-EVM regressions fail before the fix: immediate INVALID and stack-underflow child halts, plus repeated failed calls. Both child-halt cases also verify bytecode retention, failing before the follow-up. Independently tested on upstream: 812 trace HTTP tests and 400 debug-trace HTTP tests pass. Review and matrix retest remain. |
| [Besu #11353](https://github.com/besu-eth/besu/pull/11353) | Omit execution effects for root out-of-gas steps | Regression reproduces a fabricated ADD result and negative remaining gas; a sufficient-gas control still records the result. Independently tested on upstream: 811 trace HTTP tests and 400 debug-trace HTTP tests pass. Review and matrix retest remain. |

The separate [Besu #11357 method-coverage request](https://github.com/besu-eth/besu/issues/11357), opened 2026-09-23, asks for `trace_replayTransaction` or an explicit scope decision ([H01](../reports/decisions/H01.md)). It is an issue, not a submitted fix; the pinned Besu builds still return `-32601`.

### Nethermind

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Nethermind #13665](https://github.com/NethermindEth/nethermind/pull/13665) | Preserve return and revert bytes in state-only traces ([H08](../reports/decisions/H08.md)) | Four original output regressions and 13 review regressions reproduce failures before their fixes. Output-only callbacks avoid unused actions; streamed VM-only actions return pooled inputs; stored replay retains output and filters calls/rewards correctly. Trace RPC/Parity: 123 passed, one existing skip; TraceStore: 21 passed. Review and matrix retest remain. |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666) | Return complete errors for early streamed execution failures ([H25](../reports/decisions/H25.md)) | Preserves response byte limits, flush accounting and internal-error classification while buffering early failures. Seven review regressions fail before the first follow-up; 188 response-writer, service and log tests pass. A [cancellation follow-up](../evidence/2026-09-22/streaming-and-system-errors/README.md) prevents partial successes after timeout: six new regressions fail before it and all 179 selected streaming/service tests pass afterward. The current head also aborts committed HTTP responses after streaming failures instead of appending a second error envelope. Four implemented-fix review threads were verified and resolved; review and matrix retest remain. |
| [Nethermind #13667](https://github.com/NethermindEth/nethermind/pull/13667) | Accept an empty trace-type selection ([H11](../reports/decisions/H11.md)) | Depends on [#13665](https://github.com/NethermindEth/nethermind/pull/13665), including its allocation and stored-output fixes. Covers calls and stored transaction/block replay with empty selections. Trace RPC/Parity: 129 passed, one existing skip; TraceStore: 25 passed. Review and matrix retest remain. |
| [Nethermind #13668](https://github.com/NethermindEth/nethermind/pull/13668) | Serialize deleted account fields with deletion markers ([H26](../reports/decisions/H26.md)) | Five regressions reproduce changes to null instead of `-` markers. Serializer and streamed/buffered RPC tests cover pre-Cancun deletion, zero/empty fields and retained accounts after Cancun: 120 related tests passed, one existing skip. Review and matrix retest remain. |
| [Nethermind #13676](https://github.com/NethermindEth/nethermind/pull/13676) | Preserve `trace_get` failures and guard position bounds | Preserves lookup/state errors and bounds checks, and disposes materialized streams on success or failure. Three lifetime checks cover timeout cleanup and exactly-once materialization. All 82 trace RPC tests and 17 TraceStore module tests pass. Existing position semantics are preserved; tree-path agreement remains separate. |
| [Nethermind #13677](https://github.com/NethermindEth/nethermind/pull/13677) | Reject incomplete `trace_filter` queries when history is unavailable | Rejects known missing history before replay, skips genesis and reuses validated parent headers for contiguous blocks. Six missing-state and eight genesis-range cases cover both response modes; all 89 trace RPC tests pass. Preflight does not pin state against concurrent pruning. |

### Reth / Alloy / revm-inspectors

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Alloy EVM #411](https://github.com/alloy-rs/evm/pull/411) | Preserve fatal system-call error sources ([H06](../reports/decisions/H06.md)) | Six real-EVM regressions fail before the fix; default/no-default workspace tests and all-feature Clippy pass. [Validation](../evidence/2026-09-22/streaming-and-system-errors/README.md). Reth also needs #27378 and dependency uptake. |
| [Reth #27378](https://github.com/paradigmxyz/reth/pull/27378) | Preserve existing pruned-history errors through execution wrappers ([H06](../reports/decisions/H06.md)) | All 50 package tests and package Clippy pass. Handles the BAL database wrapper as well as ordinary sources. Full-workspace Clippy needs LLVM 22. System-call fixes require Alloy EVM #411; rerun after both land in a development build. |
| [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213) | Populate VM bytecode in block replay | The PR has native block/individual replay regression tests. Obtain review and rerun the affected cases after merge. Related to [H19](../reports/decisions/H19.md), but it does not by itself establish a fix for the separate creation-initcode case. |

## Merged

### Erigon

| PR | Fix | Merged (UTC) | Verification remaining |
| --- | --- | --- | --- |
| [Erigon #23952](https://github.com/erigontech/erigon/pull/23952) | Include MCOPY memory writes ([H20](../reports/decisions/H20.md)) | 2026-09-14 | The [MCOPY case](../reports/cases/a/call-mcopy.md) agrees on the tested development build but differs on release 3.6.1. Retest a release containing the fix before marking release verification complete. |

### Reth / Alloy / revm-inspectors

| PR | Fix | Merged (UTC) | Verification remaining |
| --- | --- | --- | --- |
| [Reth #27364](https://github.com/paradigmxyz/reth/pull/27364) | Return `null` for a missing replay transaction ([H06](../reports/decisions/H06.md)) | 2026-09-22 | Merged into `main`; refresh development-build observations separately. Execution failures still return errors. |
| [Reth #27366](https://github.com/paradigmxyz/reth/pull/27366) | Select `trace_get` results by tree path ([H02](../reports/decisions/H02.md)) | 2026-09-22 | Merged into `main`; this implements a proposed contract change, not evidence of cross-client agreement. |
| [revm-inspectors #511](https://github.com/paradigmxyz/revm-inspectors/pull/511) | Record executed bytecode, including constructor initcode ([H19](../reports/decisions/H19.md)) | 2026-09-22 | Awaiting dependency uptake: current Reth `main@0a1d3e7612` still locks `revm-inspectors 0.43.0`. Retest creation and delegated/executing bytecode after the update. |
| [Reth #27365](https://github.com/paradigmxyz/reth/pull/27365) | Include `transactionHash` in individual replay results ([H07](../reports/decisions/H07.md)) | 2026-09-22 | Verified on `main@534c60db9d`: all 12 individual replay cases return the requested hash. [Results and evidence](../evidence/2026-09-22/reth-main-534c60db/README.md). Release verification remains. |
| [Reth #27367](https://github.com/paradigmxyz/reth/pull/27367) | Classify pruned changeset errors as unavailable history ([H06](../reports/decisions/H06.md)) | 2026-09-22 | Verified on `main@534c60db9d`: old-state nonce access returns `4444`, but all four historical trace methods still return `-32603` through the blockhash system-call wrapper. [Partial result and evidence](../evidence/2026-09-22/reth-main-534c60db/README.md). H06 remains open. |
| [Alloy #4216](https://github.com/alloy-rs/alloy/pull/4216) | Default address filtering to AND; retain explicit union ([H03](../reports/decisions/H03.md)) | 2026-09-22 | Awaiting Reth dependency uptake. `main@0a1d3e7612` (checked 2026-09-23) still locks `alloy-rpc-types-trace 2.4.2`, which predates the fix. The 2026-09-23 recapture confirms the tested Reth builds still OR the two lists; their one-sided and explicit-mode results already agree. This implements a proposed contract choice, not group consensus. |
| [Alloy #4218](https://github.com/alloy-rs/alloy/pull/4218) | Serialize absent reward transaction fields as explicit `null` | 2026-09-22 | Awaiting Reth dependency uptake. The locked Alloy 2.4.2 does not contain this fix; no rerun. |
| [revm-inspectors #504](https://github.com/paradigmxyz/revm-inspectors/pull/504) | Record complete VM execution deltas ([H20](../reports/decisions/H20.md)) | 2026-09-14 | The selected [MCOPY checks](../reports/cases/a/call-mcopy.md) agree in both tested Reth builds. That check does not establish coverage of every delta handled by the patch. |
| [revm-inspectors #509](https://github.com/paradigmxyz/revm-inspectors/pull/509) | Include EIP-7702 code changes in stateDiff ([H18](../reports/decisions/H18.md)) | 2026-09-15 | `main@0a1d3e7612` (checked 2026-09-23) still locks `revm-inspectors 0.43.0`, which predates this fix. No rerun until dependency uptake; the pinned observations remain unchanged. |
| [revm-inspectors #510](https://github.com/paradigmxyz/revm-inspectors/pull/510) | Report pre-Cancun selfdestruct deletions ([H26](../reports/decisions/H26.md)) | 2026-09-15 | `main@0a1d3e7612` (checked 2026-09-23) still locks `revm-inspectors 0.43.0`, which predates this fix. No rerun until dependency uptake. |

## Development verification

Matthias Seitz opened the six Reth/Alloy proposals above; all six have merged
(four in Reth, two in Alloy). Reth's locked Alloy version does not yet contain the
Alloy changes. The earlier run verified #27365 and #27367; see the
[replay and pruning results](../evidence/2026-09-22/reth-main-534c60db/README.md).
No dependency overrides or unmerged PR branches were included in that cross-client run; native regression tests for pending patches are tracked separately.

## Related work

The [Geth draft fork](geth.md) is an implementation experiment, with no upstream PR tracked here.
Its passing selected cases do not establish upstream acceptance or production readiness.
[Reth #27217](https://github.com/paradigmxyz/reth/pull/27217) is related open Otterscan work;
it is outside the `trace_*` specification and does not count toward alignment here.
Its four underlying CI failures occur during setup-mold archive extraction, before
compilation or tests. A [maintainer rerun was requested](https://github.com/paradigmxyz/reth/pull/27217#issuecomment-5791971158).

## Remaining work

[The Besu VM-trace follow-ups](next-fixes.md) are submitted as #11352 and #11353 and
included above. Both target upstream independently; neither depends on #11350.
Their upstream Forest trace suite remains disabled and skipped.

Eight implemented-fix review threads across Nethermind #13666, #13667, #13676 and
#13677 were verified against their current heads and resolved. Three rationale
threads remain open for reviewer confirmation; resolution is not maintainer approval.

The open client fixes have native regression tests. Nethermind #13667 is stacked on #13665
because empty selections also need its output-capture fix; the other patches were tested on
separate upstream bases. They have not yet been built into a fresh cross-client matrix.
The reports and frozen captures continue to describe their pinned builds, not the proposed patches.

Tree-path lookup, filter composition, signed transaction execution validation and precompile inclusion remain
[contract decisions](../decisions/README.md). The tree-path and address-filter default proposals above are now being implemented by Reth/Alloy;
client patches do not settle the cross-client decision or compatibility plan.

## Keeping this current

Update the checked date when refreshing PR states. For each merged change, link the tested
commit and case; record release verification only after running that release. Record reviewer
or implementation ownership only when the person has explicitly accepted it. A review of an
individual fix must not be presented as endorsement of the whole specification.
