# Geth draft fork: changes to review

The experimental fork follows the adopted source-review stances; its checked cases agree on every assessed decision except the H12 raw-transaction block argument and simulation pending, which remain policy observations. It is not upstream Geth support or a consensus vote. Filtering remains a bounded scan; pruning still needs runtime coverage.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Tested version | Commit | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| `1.17.7-unstable` | [`0a663f3c`](https://github.com/banteg/go-ethereum/commit/0a663f3cd1245f3510ccbbe5146fdfc7007cd290) | 2026-09-24 | [2026-09-25](../../evidence/2026-09-25/refresh/initial/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 1.17.7-unstable · 0a663f3c | Proposed change |
| --- | --- | --- |
| [Precompile call-frame inclusion](../decisions/H29.md)<br>The captured draft implementation (0a663f3c) still follows the previous rule and emits no frame for a CALL or CREATE that fails its precheck. | ⚠️ Differs<br>[Precheck call value](../cases/probes-prague/precheck-call-value.md) | Fixed on feat/trace in 07a99c67, which keeps the failed frame with the new labels; the next capture measures it. Checked requirements: A CALL or CREATE that fails its balance precheck emits a failed frame with no result and no subtraces; the next sibling follows at [1] and the parent counts both.<br>[Call frames and precompiles](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L123) |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 1.17.7-unstable · 0a663f3c | [Raw-transaction block argument](../decisions/H12.md) | 1 policy-open case. The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |
| 1.17.7-unstable · 0a663f3c | [Invalid-parameter error codes](../decisions/H14.md) | 1 policy-open case. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected a result; observed rpc_error -32602 gasPrice conflicts with blob or authorization fields | [Field authorization](../cases/probes-prague/field-authorization.md) |
| 1.17.7-unstable · 0a663f3c | [Trace block tags and pending state](../decisions/H32.md) | 2 policy-open cases. call-number-pending: RPC error -32602. many-number-pending: RPC error -32602. | [Call number pending](../cases/h30/call-number-pending.md) · [Many number pending](../cases/h30/many-number-pending.md) |

## Assessment gaps

| Decision | Build | Reason | Example |
| --- | --- | --- | --- |
| [Failed frame results and error labels](../decisions/H09.md) | 1.17.7-unstable · 0a663f3c | 1 blocked case: No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'call'}. 1 blocked case: No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}. | [Precheck call value](../cases/probes-prague/precheck-call-value.md) · [Precheck create value](../cases/probes-prague/precheck-create-value.md) |
| [Fee accounting and sequential state diffs](../decisions/H16.md) | 1.17.7-unstable · 0a663f3c | 1 blocked case: The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0. 1 blocked case: The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. 4 blocked cases: The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. 2 blocked cases: The refund is not independently derived; balances settle within the refund bound. Gas=21700..26335 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. 4 blocked cases: The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. | [Many storage write read](../cases/a/many-storage-write-read.md) · [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) |

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [trace_get selector and return shape](../decisions/H02.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) |
| [Empty address lists](../decisions/H04.md) | [Filter both null](../cases/a/filter-both-null.md) · [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Missing transactions and paths](../decisions/H06.md) | [Missing block block](../cases/a/missing-block-block.md) · [Missing block call](../cases/a/missing-block-call.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 35](../cases/forks/replay-35.md) · [Replay 36](../cases/forks/replay-36.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Signed transaction execution validity](../decisions/H13.md) | [Raw below basefee](../cases/a/raw-below-basefee.md) · [Raw insufficient funds](../cases/a/raw-insufficient-funds.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | [Model environment](../cases/coverage/model-environment.md) · [Model environment free](../cases/coverage/model-environment-free.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace executing bytecode](../decisions/H19.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace step timing and deltas](../decisions/H20.md) | [Call mcopy](../cases/a/call-mcopy.md) · [Call return42](../cases/a/call-return42.md) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter created to](../cases/a/filter-created-to.md) · [Filter creator from](../cases/a/filter-creator-from.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [Filter 35](../cases/forks/filter-35.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Omitted trace_filter range bounds](../decisions/H30.md) | [Filter no bounds](../cases/h30/filter-no-bounds.md) · [Filter to 2 implicit from](../cases/h30/filter-to-2-implicit-from.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |

</details>

[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
