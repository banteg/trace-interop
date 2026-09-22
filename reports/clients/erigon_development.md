# Erigon: changes to review

The tested development build agrees on several cases that differ in the release, including tree lookup, MCOPY and historical system state. Default filter composition still needs attention; signed-transaction validity checks and error codes need alignment with the proposal.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| Development | `3.8.0-dev-c25b8e47` | [2026-09-21](https://github.com/erigontech/erigon/commit/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec) | [2026-09-21](../../evidence/2026-09-21/precompiles-final/manifest.json)<br>[2026-09-22](../../evidence/2026-09-23/h03-modes-a/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.

## Changes to discuss

| Behavior | Development | Proposed change |
| --- | --- | --- |
| [Filter composition and mode](../decisions/H03.md)<br>Both lists are combined with OR by default (6 records instead of 1). With `mode: "intersection"`, a one-sided filter returns `[]` instead of treating the empty side as unrestricted. The unrecognized `mode: "garbage"` is accepted and treated as union. | Differs<br>[Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) | Make intersection the default. Under either mode, ignore an omitted, null or empty side. Reject unknown mode values with `-32602`.<br>[Address filtering](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L311) |
| [Missing transactions and paths](../decisions/H06.md)<br>Missing-transaction lookup can return an RPC error, and an unknown filter endpoint can return []. | Differs<br>[Missing block block](../cases/a/missing-block-block.md) | Return `null` for a missing transaction or path; reserve errors for unavailable history and invalid requests. Checked requirements: An unknown selected block or range endpoint returns Resource not found (-32001).<br>[Trace lookup](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L135) · [Replay results](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L880) |
| [Empty trace-type selection](../decisions/H11.md)<br>Empty-selection requests include rejected calls; the zero-fee case also fails the fee rule. | Differs<br>[Call empty types](../cases/initial/call-empty-types.md) | Accept an empty selection and return the execution envelope. Recheck alongside H15 before treating every rejection as a separate selection bug. Checked requirements: An empty trace-type selection executes successfully.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Signed transaction execution validity](../decisions/H13.md)<br>Marker probes execute nonce mismatches, both insufficient-funds cases and ordinary-code-sender transactions. CREATE uses the state-nonce address. Chain, intrinsic-gas and base-fee failures are rejected with -32000. Review feedback supports stricter validation. | Differs<br>[Raw below basefee](../cases/a/raw-below-basefee.md) | Apply selected-state execution validity before running signed transactions. Distinguish validation rejection from execution failure, and use the proposed -32003 code for validation errors. Checked requirements: Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected).<br>[Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) |
| [Invalid-parameter error codes](../decisions/H14.md)<br>Malformed raw transactions and an unknown option use error codes other than `-32602`. | Differs<br>[Call unknown mode](../cases/a/call-unknown-mode.md) | Use JSON-RPC invalid params (`-32602`) for malformed input, separately from execution rejection. Checked requirements: Malformed input returns invalid params (-32602).<br>[Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) · [Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Unsigned simulation fees and block environment](../decisions/H15.md)<br>Explicit zero-fee unsigned calls are rejected. | Differs<br>[Call constructor](../cases/initial/call-constructor.md) | Allow zero-fee unsigned simulation without changing the block’s `BASEFEE` opcode value. Checked requirements: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Fee accounting and sequential state diffs](../decisions/H16.md)<br>The linked case differs from the proposed behavior. | Differs<br>[Call many](../cases/initial/call-many.md) | Return one execution envelope per input call, in order.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) · [State differences](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L741) |

## Extension observations

These requests explicitly select behavior outside the portable baseline. Acceptance or rejection is not a conformance verdict.

| Build | Extension | Observed | Example |
| --- | --- | --- | --- |
| Development | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |

Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.

**Partially assessed:** some declared cases lack an evaluated assertion. [trace_get selector and return shape](../decisions/H02.md), [Empty address lists](../decisions/H04.md), [Post-merge reward records](../decisions/H05.md), [Replay transactionHash field](../decisions/H07.md), [Failed frame results and error labels](../decisions/H09.md), [Creation result field names](../decisions/H10.md), [New-account stateDiff encoding](../decisions/H17.md), [EIP-7702 code changes in stateDiff](../decisions/H18.md), [vmTrace executing bytecode](../decisions/H19.md), [vmTrace step timing and deltas](../decisions/H20.md), [vmTrace numeric and optional metadata encoding](../decisions/H21.md), [Special-action address matching](../decisions/H23.md), [Sibling failure isolation](../decisions/H24.md), [Filter execution across fork boundaries](../decisions/H27.md).

<details><summary>Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
