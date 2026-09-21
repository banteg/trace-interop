# Client fixes

Upstream changes arising from the trace comparison. Status checked **2026-09-22**.
A merged patch, a tested build and agreement with the proposed API are separate milestones.
The [client reports](../reports/README.md) describe the behavior; this page tracks the work to change it.

## Upstream patches

| Client / library | Fix | Upstream state | Evidence and next step |
| --- | --- | --- | --- |
| Reth / revm-inspectors | Record complete VM execution deltas ([H20](../reports/decisions/H20.md)) | [revm-inspectors #504](https://github.com/paradigmxyz/revm-inspectors/pull/504) merged September 14 | The selected [MCOPY checks](../reports/cases/a/call-mcopy.md) agree in both tested Reth builds. That check does not establish coverage of every delta handled by the patch. |
| Erigon | Include MCOPY memory writes ([H20](../reports/decisions/H20.md)) | [Erigon #23952](https://github.com/erigontech/erigon/pull/23952) merged September 14 | The [same case](../reports/cases/a/call-mcopy.md) agrees on the tested development build but differs on release 3.6.1. Retest a release containing the fix before marking release verification complete. |
| Reth | Populate VM bytecode in block replay | [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213) open; review required | The PR has native block/individual replay regression tests. Obtain review and rerun the affected cases after merge. Related to [H19](../reports/decisions/H19.md), but it does not by itself establish a fix for the separate creation-initcode case. |
| Besu | Include MCOPY memory updates ([H20](../reports/decisions/H20.md)) | [Besu #11286](https://github.com/besu-eth/besu/pull/11286) open; review required | The [checked builds](../reports/cases/a/call-mcopy.md) still omit the write. The PR has a native regression test; obtain review and retest after merge. Supersedes closed #11285. |

The [Geth draft fork](geth.md) is an implementation experiment, with no upstream PR tracked here.
Its passing selected cases do not establish upstream acceptance or production readiness.
[Reth #27217](https://github.com/paradigmxyz/reth/pull/27217) is related open Otterscan work;
it is outside the `trace_*` specification and does not count toward alignment here.

## Candidate fixes

These are preparation priorities, not commitments from client teams. No upstream patch is tracked for these rows yet.

| Client | Problem | Next step |
| --- | --- | --- |
| Nethermind | [Rejected signed transactions can produce incomplete JSON (H25)](../reports/decisions/H25.md) | Isolate the actual wire-response error path in a native test. Fix serialization independently of nonce or fee-admission policy. |
| Reth / revm-inspectors | [EIP-7702 code transitions missing from stateDiff (H18)](../reports/decisions/H18.md) | Add a native authorization-code regression, including an execution revert, then patch the state-diff builder. |
| Reth / revm-inspectors | [Creation initcode missing from vmTrace.code (H19)](../reports/decisions/H19.md) | Distinguish the constructor case from the existing block-replay PR before proposing another change. |
| Nethermind | [State-only tracing loses return bytes (H08)](../reports/decisions/H08.md) | Preserve the execution output independently of selected trace components. |
| Besu | [Precompile return bytes missing from the call frame (H22)](../reports/decisions/H22.md) | Add a native identity-precompile output regression; keep frame-inclusion policy separate. |
| Besu | [Child failure affects another frame's status (H24)](../reports/decisions/H24.md) | Test a handled failure followed by successful execution; keep error state local to its frame. |

Tree-path lookup, filter composition, signed nonce admission and precompile inclusion remain
[contract decisions](../decisions/README.md). A patch to one of those needs an agreed behavior
and compatibility plan; it should not be filed as a routine compliance fix.

## Keeping this current

Update the checked date when refreshing PR states. For each merged change, link the tested
commit and case; record release verification only after running that release. Record reviewer
or implementation ownership only when the person has explicitly accepted it. A review of an
individual fix must not be presented as endorsement of the whole specification.
