# Erigon: changes to review

The tested development build agrees on several cases that differ in the release, including tree lookup, MCOPY and historical system state. Default filter composition and signed nonce validation still need attention.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| Release | `3.6.1-0c4d9c91` | [2026-09-09](https://github.com/erigontech/erigon/commit/0c4d9c91dbaffd52890235f7ea395b0231738501) | [2026-09-21](../../evidence/2026-09-21/precompiles-final/manifest.json)<br>[2026-09-22](../../evidence/2026-09-23/precompile-values-native/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.

## Changes to discuss

| Behavior | Release | Proposed change |
| --- | --- | --- |
| [trace_get selector and return shape](../decisions/H02.md)<br>Root and nested `trace_get` requests fail or select the wrong record. | Differs<br>[Get nested positive](../cases/a/get-nested-positive.md) | Interpret the selector as one `traceAddress` path: `[]` selects the root, `[0]` its first child. Checked requirements: Return the transaction-tree record at [6, 0], or null if absent. Return the transaction-tree record at [], or null if absent. Return one object whose traceAddress equals [].<br>[Trace lookup](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L135) |
| [Filter composition and mode](../decisions/H03.md)<br>Supplying both sender and recipient lists broadens the search by default (OR). | Differs<br>[Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) | Use AND between the two lists, so adding a recipient filter narrows a sender query. Keep union as an explicit extension if desired. Checked requirements: The portable filter profile rejects the mode extension as invalid params. Compare address bytes: OR within each list, AND across lists; missing/null/empty lists are unrestricted.<br>[Address filtering](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L311) |
| [Missing transactions and paths](../decisions/H06.md)<br>Missing-transaction lookup can return an RPC error, and an unknown filter endpoint can return []. | Differs<br>[Missing block block](../cases/a/missing-block-block.md) | Return `null` for a missing transaction or path; reserve errors for unavailable history and invalid requests. Checked requirements: An unknown selected block or range endpoint returns Resource not found (-32001). Unknown transaction returns null, not an empty collection or RPC error.<br>[Trace lookup](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L135) · [Replay results](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L880) |
| [Empty output and unrequested components](../decisions/H08.md)<br>An unrequested `trace` component is `null`. | Differs<br>[State only nonempty output](../cases/a/state-only-nonempty-output.md) | Return `trace: []` when call traces were not requested; keep the execution output independently. Checked requirements: Unrequested trace is an empty array.<br>[Replay results](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L880) · [Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Empty trace-type selection](../decisions/H11.md)<br>Empty-selection requests include rejected calls; the zero-fee case also fails the fee rule. | Differs<br>[Empty types](../cases/a/empty-types.md) | Accept an empty selection and return the execution envelope. Recheck alongside H15 before treating every rejection as a separate selection bug. Checked requirements: An empty trace-type selection executes successfully.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Signed transaction nonce validation](../decisions/H13.md)<br>A signed transaction with a nonce above the account nonce is accepted. | Differs<br>[Raw nonce high](../cases/a/raw-nonce-high.md) | If the proposed admission policy is adopted, reject nonce mismatches without rewriting the signed nonce. This is a contract decision, separate from well-formed error reporting. Checked requirements: Proposed admission policy: reject a signed nonce mismatch rather than replace it; client agreement is pending.<br>[Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) |
| [Invalid-parameter error codes](../decisions/H14.md)<br>Malformed raw transactions and an unknown option use error codes other than `-32602`. | Differs<br>[Call null mode](../cases/a/call-null-mode.md) | Use JSON-RPC invalid params (`-32602`) for malformed input, separately from execution rejection. Checked requirements: Malformed input returns invalid params (-32602).<br>[Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) · [Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Unsigned simulation fees and block environment](../decisions/H15.md)<br>Explicit zero-fee unsigned calls are rejected. | Differs<br>[Call constructor](../cases/initial/call-constructor.md) | Allow zero-fee unsigned simulation without changing the block’s `BASEFEE` opcode value. Checked requirements: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Fee accounting and sequential state diffs](../decisions/H16.md)<br>The linked case differs from the proposed behavior. | Differs<br>[Call many](../cases/initial/call-many.md) | Return one execution envelope per input call, in order.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) · [State differences](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L741) |
| [vmTrace step timing and deltas](../decisions/H20.md)<br>The `MCOPY` step omits its memory write. | Differs<br>[Call mcopy](../cases/a/call-mcopy.md) | Record the same-step memory delta, including the copied word at offset 32. Checked requirements: MCOPY reports its same-step write of word 42 at offset 32.<br>[VM execution deltas](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L545) |
| [Historical state at system-operation boundaries](../decisions/H28.md)<br>A historical beacon-root lookup includes a following block’s system update. | Differs<br>[Beacon call 55](../cases/fork-followup/beacon-call-55.md) | Read the selected block’s post-state, before applying the next block’s system operations. Checked requirements: Historical beacon-root storage excludes the following block system update. Historical trace_call uses only system changes through the selected block.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |

## Extension observations

These requests explicitly select behavior outside the portable baseline. Acceptance or rejection is not a conformance verdict.

| Build | Extension | Observed | Example |
| --- | --- | --- | --- |
| Release | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |

Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.

**Partially assessed:** some declared cases lack an evaluated assertion. [Empty address lists](../decisions/H04.md), [Post-merge reward records](../decisions/H05.md), [Replay transactionHash field](../decisions/H07.md), [Failed frame results and error labels](../decisions/H09.md), [Creation result field names](../decisions/H10.md), [New-account stateDiff encoding](../decisions/H17.md), [EIP-7702 code changes in stateDiff](../decisions/H18.md), [vmTrace executing bytecode](../decisions/H19.md), [vmTrace numeric and optional metadata encoding](../decisions/H21.md), [Special-action address matching](../decisions/H23.md), [Sibling failure isolation](../decisions/H24.md), [Filter execution across fork boundaries](../decisions/H27.md).

<details><summary>Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
