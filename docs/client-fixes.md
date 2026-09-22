# Client fixes

Upstream changes arising from the trace comparison. Status checked **2026-09-22**.
A merged patch, a tested build and agreement with the proposed API are separate milestones.
The [client reports](../reports/README.md) describe the behavior; this page tracks the work to change it.

**15 pending · 4 merged**

## Pending

### Besu

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Besu #11286](https://github.com/besu-eth/besu/pull/11286) | Include MCOPY memory updates ([H20](../reports/decisions/H20.md)) | The [checked builds](../reports/cases/a/call-mcopy.md) still omit the write. The PR has a native regression test; obtain review and retest after merge. Supersedes closed #11285. |
| [Besu #11345](https://github.com/besu-eth/besu/pull/11345) | Keep sibling and handled precompile failures local ([H24](../reports/decisions/H24.md)) | Regressions cover both sibling orders and all four CALL variants. Seven unit tests and 809 HTTP trace fixtures pass. Review and matrix retest remain. |
| [Besu #11346](https://github.com/besu-eth/besu/pull/11346) | Preserve root precompile return bytes ([H22](../reports/decisions/H22.md)) | Unit regression reproduced the missing bytes. Three unit tests and 810 HTTP trace fixtures pass, including a new identity-precompile fixture. Review and matrix retest remain. |
| [Besu #11347](https://github.com/besu-eth/besu/pull/11347) | Preserve errors from failed root precompiles ([H09](../reports/decisions/H09.md)) | A regression reproduces the lost exceptional-halt reason. After the fix, 29 tracer tests, one flat-trace test and 810 HTTP trace fixtures pass, including invalid bn128Add input. This covers root precompile error reporting, not every H09 difference. Review and matrix retest remain. |
| [Besu #11350](https://github.com/besu-eth/besu/pull/11350) | Remove fabricated CALL memory writes from `vmTrace` ([H20](../reports/decisions/H20.md)) | Real-EVM HTTP tests reproduce parent RETURN bytes being attributed to earlier CALL/DELEGATECALL operations. Four cases cover zero output and real writes at offset 32; all 813 active HTTP trace tests pass. Corrected 45 fabricated memory deltas in 27 existing fixtures. The upstream Forest suite remains disabled. |
| [Besu #11352](https://github.com/besu-eth/besu/pull/11352) | Preserve VM frame ownership and CALL resumption gas after omitted opcodes | Three real-EVM regressions fail before the fix: immediate INVALID and stack-underflow child halts, plus repeated failed calls. Independently tested on upstream: 812 trace HTTP tests and 400 debug-trace HTTP tests pass. Review and matrix retest remain. |
| [Besu #11353](https://github.com/besu-eth/besu/pull/11353) | Omit execution effects for root out-of-gas steps | Regression reproduces a fabricated ADD result and negative remaining gas; a sufficient-gas control still records the result. Independently tested on upstream: 811 trace HTTP tests and 400 debug-trace HTTP tests pass. Review and matrix retest remain. |

### Nethermind

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Nethermind #13665](https://github.com/NethermindEth/nethermind/pull/13665) | Preserve return and revert bytes in state-only traces ([H08](../reports/decisions/H08.md)) | Four new regressions reproduce the loss before the fix. The trace RPC suite passes (79 tests); related Parity tests also pass. Review and matrix retest remain. |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666) | Return complete errors for early streamed execution failures ([H25](../reports/decisions/H25.md)) | Buffers the initial response and reuses buffered-call exception mapping, including missing trie nodes during replay. Regressions cover both replay methods, tracer flushes, committed output, transport failures and module disposal: 238 related tests passed. Review and matrix retest remain. |
| [Nethermind #13667](https://github.com/NethermindEth/nethermind/pull/13667) | Accept an empty trace-type selection ([H11](../reports/decisions/H11.md)) | Depends on [#13665](https://github.com/NethermindEth/nethermind/pull/13665). Six empty-selection regressions fail before the fix. The patch covers `trace_call` and `trace_callMany`, including streamed responses: 124 related tests passed, one existing skip. Review and matrix retest remain. |
| [Nethermind #13668](https://github.com/NethermindEth/nethermind/pull/13668) | Serialize deleted account fields with deletion markers ([H26](../reports/decisions/H26.md)) | Five regressions reproduce changes to null instead of `-` markers. Serializer and streamed/buffered RPC tests cover pre-Cancun deletion, zero/empty fields and retained accounts after Cancun: 120 related tests passed, one existing skip. Review and matrix retest remain. |
| [Nethermind #13676](https://github.com/NethermindEth/nethermind/pull/13676) | Preserve `trace_get` failures and guard position bounds | Six regressions reproduce lost lookup/state errors or invalid array indexes across the regular and trace-store paths. All 81 trace RPC tests and 24 trace-store tests pass. Existing successful position semantics are preserved; tree-path agreement remains separate. |
| [Nethermind #13677](https://github.com/NethermindEth/nethermind/pull/13677) | Reject incomplete `trace_filter` queries when history is unavailable | Six regressions reproduce successful empty or partial results with missing state at either end of a range or its initial parent, in both response modes. Preflight now returns the existing error before replay. All 81 trace RPC tests pass. |

### Reth / revm-inspectors

| PR | Fix | Evidence and next step |
| --- | --- | --- |
| [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213) | Populate VM bytecode in block replay | The PR has native block/individual replay regression tests. Obtain review and rerun the affected cases after merge. Related to [H19](../reports/decisions/H19.md), but it does not by itself establish a fix for the separate creation-initcode case. |
| [revm-inspectors #511](https://github.com/paradigmxyz/revm-inspectors/pull/511) | Record executed bytecode, including constructor initcode ([H19](../reports/decisions/H19.md)) | The existing PR covers creation and delegated/executing bytecode with native tests. Follow its review rather than submit a duplicate. This is separate from Reth #27213 above. |

## Merged

### Erigon

| PR | Fix | Merged (UTC) | Verification remaining |
| --- | --- | --- | --- |
| [Erigon #23952](https://github.com/erigontech/erigon/pull/23952) | Include MCOPY memory writes ([H20](../reports/decisions/H20.md)) | 2026-09-14 | The [MCOPY case](../reports/cases/a/call-mcopy.md) agrees on the tested development build but differs on release 3.6.1. Retest a release containing the fix before marking release verification complete. |

### Reth / revm-inspectors

| PR | Fix | Merged (UTC) | Verification remaining |
| --- | --- | --- | --- |
| [revm-inspectors #504](https://github.com/paradigmxyz/revm-inspectors/pull/504) | Record complete VM execution deltas ([H20](../reports/decisions/H20.md)) | 2026-09-14 | The selected [MCOPY checks](../reports/cases/a/call-mcopy.md) agree in both tested Reth builds. That check does not establish coverage of every delta handled by the patch. |
| [revm-inspectors #509](https://github.com/paradigmxyz/revm-inspectors/pull/509) | Include EIP-7702 code changes in stateDiff ([H18](../reports/decisions/H18.md)) | 2026-09-15 | Upstream already fixed this. Our pinned Reth builds use an older library revision; rerun with the fix before updating the observed result. |
| [revm-inspectors #510](https://github.com/paradigmxyz/revm-inspectors/pull/510) | Report pre-Cancun selfdestruct deletions ([H26](../reports/decisions/H26.md)) | 2026-09-15 | Upstream already fixed this. Dependency uptake and a fresh matrix run remain to be verified. |

## Related work

The [Geth draft fork](geth.md) is an implementation experiment, with no upstream PR tracked here.
Its passing selected cases do not establish upstream acceptance or production readiness.
[Reth #27217](https://github.com/paradigmxyz/reth/pull/27217) is related open Otterscan work;
it is outside the `trace_*` specification and does not count toward alignment here.

## Remaining work

[The Besu VM-trace follow-ups](next-fixes.md) are submitted as #11352 and #11353 and
included above. Both target upstream independently; neither depends on #11350.
Their upstream Forest trace suite remains disabled and skipped.

The open client fixes have native regression tests. Nethermind #13667 is stacked on #13665
because empty selections also need its output-capture fix; the other patches were tested on
separate upstream bases. They have not yet been built into a fresh cross-client matrix.
The reports and frozen captures continue to describe their pinned builds, not the proposed patches.

Tree-path lookup, filter composition, signed nonce admission and precompile inclusion remain
[contract decisions](../decisions/README.md). A patch to one of those needs an agreed behavior
and compatibility plan; it should not be filed as a routine compliance fix.

## Keeping this current

Update the checked date when refreshing PR states. For each merged change, link the tested
commit and case; record release verification only after running that release. Record reviewer
or implementation ownership only when the person has explicitly accepted it. A review of an
individual fix must not be presented as endorsement of the whole specification.
