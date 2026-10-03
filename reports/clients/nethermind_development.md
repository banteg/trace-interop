# Nethermind: changes to review

2.2.0-preview · 3370d566 agrees on filter modes and empty address lists (#13857), post-merge and genesis reward records (#13938, #13783, #13801), vmTrace steps (#13940, #13958), precheck and collision frames (#13957), failed-frame results and labels (#13981) and null for a missing transaction or replay (#13937, #14037). Since the 2026-10-01 merges it also validates trace_rawTransaction as block inclusion does (#14091), rejects disagreeing data and input (#14089), rejects block-hash filter bounds and selects one block with the trace_filter blockHash member (#14111), runs blob calls without a positive blob fee cap at BLOBBASEFEE 0 (#14092) and answers rejected calls with the eth_simulateV1 codes (#14158). 2.1.0 · b3e7e84c retains output and empty selections and fixes the account markers (#13667, #13668), but none of the later fixes, and still truncates rejected streamed traces (#13666). No checked case differs in the development build; a code sender’s rejection message, gas-defaulting probes its funds cannot cover and the legacy-priced authorization list remain unassessed or open.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Tested version | Commit | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| `2.2.0-preview` | [`3370d566`](https://github.com/NethermindEth/nethermind/commit/3370d566b67ad741e91a6e647d98c5c28c3a2ed9) | 2026-10-02 | [2026-10-02](../../evidence/2026-10-02/eval/initial/manifest.json)<br>[2026-10-03](../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 2.2.0-preview · 3370d566 | Proposed change |
| --- | --- | --- |
| [Invalid parameters and rejected calls](../decisions/H14.md)<br>Malformed raw input, negative filter count and integer paths expose validation differences across the captured builds. An unpriced call with a null `blobVersionedHashes` or `authorizationList` takes that member’s transaction type: 2.1.0-preview · 45912ba3 rejects it with -32000 (“need at least 1 blob”, “EIP-7702 transaction cannot be used to create contract”) and 2.0.0 truncates the authorizationList response. 2.2.0-preview · 759efed7 treats a null member as omitted (#14049), rejects a negative filter count (#14050) and rejects disagreeing `data` and `input` with -32602 (#14089). | ⚠️ Differs · [Nethermind #14212](https://github.com/NethermindEth/nethermind/pull/14212) (partial fix)<br>[Fork access list before](../cases/probes-forks/fork-access-list-before.md) | Ship #14049, #14050 and #14089 in a release: reject malformed input, such as a negative filter count or disagreeing `data` and `input` (`-32602` recommended), and treat a null member as omitted, so it selects no transaction type. Checked requirements: The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. The call runs with type 1, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. The access-list fields at block 31, before Berlin (block 32) name a feature not active at the selected block, so the call is rejected (-32003 recommended). An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. The blob fields at block 55, before Cancun (block 56) name a feature not active at the selected block, so the call is rejected (-32003 recommended). An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). An explicit type 4 with no authorization fields runs at block 59, before Prague (block 60): type is not a feature.<br>[Signed transaction replay](https://github.com/NethermindEth/nethermind/blob/641592d2b96fa1e2fa8e8a0b1761582a1728bd51/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L150) · [Call simulation](https://github.com/NethermindEth/nethermind/blob/641592d2b96fa1e2fa8e8a0b1761582a1728bd51/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L78) |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 2.2.0-preview · 3370d566 | [Raw-transaction block argument](../decisions/H12.md) | 6 extension cases. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params). Selector latest: rejected as invalid params (-32602: Invalid params). Selector block 0x19 by number: rejected as invalid params (-32602: Invalid params). Selector block 0x19 by hash: rejected as invalid params (-32602: Invalid params). Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: Invalid params). Selector pending: rejected as invalid params (-32602: Invalid params). | [Raw valid](../cases/initial/raw-valid.md) · [Raw state hash](../cases/raw-selector/raw-state-hash.md) |

Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.

## Assessment gaps

| Decision | Build | Reason | Example |
| --- | --- | --- | --- |
| [Signed transaction execution validity](../decisions/H13.md) | 2.2.0-preview · 3370d566 | 4 blocked cases: The error does not identify a validation failure: -32000 sender has deployed code. | [Raw validation code sender all](../cases/raw-validation/raw-validation-code-sender-all.md) · [Raw validation code sender statediff](../cases/raw-validation/raw-validation-code-sender-stateDiff.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | 2.2.0-preview · 3370d566 | 1 blocked case: Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000. 2 blocked cases: Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000. 1 blocked case: The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. 4 blocked cases: The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. 2 blocked cases: The refund is not independently derived; balances settle within the refund bound. Gas=21700..26335 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. 4 blocked cases: The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0. | [Many storage write read](../cases/a/many-storage-write-read.md) · [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) |
| [Fee accounting and sequential state diffs](../decisions/H16.md) | 2.2.0-preview · 3370d566 | 1 blocked case: H15 owns this error, a funds validation rejection: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000 . There is no executed result to inspect. | [Field gas omitted allowance many](../cases/probes-prague/field-gas-omitted-allowance-many.md) |

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [trace_get selector and return shape](../decisions/H02.md) | [_reference/block/0x30](../cases/a/_reference/block/0x30.md) · [Block 2](../cases/a/block-2.md) |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) |
| [Empty address lists](../decisions/H04.md) | [Filter both null](../cases/a/filter-both-null.md) · [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [_reference/block/0x30](../cases/a/_reference/block/0x30.md) · [Block 2](../cases/a/block-2.md) |
| [Missing transactions and paths](../decisions/H06.md) | [Missing block block](../cases/a/missing-block-block.md) · [Missing block call](../cases/a/missing-block-call.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 35](../cases/forks/replay-35.md) · [Replay 36](../cases/forks/replay-36.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Failed frame results and error labels](../decisions/H09.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set revert](../cases/a/auth-set-revert.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Raw-transaction block argument](../decisions/H12.md) | [Raw valid](../cases/initial/raw-valid.md) · [Raw state hash](../cases/raw-selector/raw-state-hash.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace executing bytecode](../decisions/H19.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace step timing and deltas](../decisions/H20.md) | [Call gas7400](../cases/a/call-gas7400.md) · [Call mcopy](../cases/a/call-mcopy.md) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter all](../cases/a/filter-all.md) · [Filter both null](../cases/a/filter-both-null.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [Filter 35](../cases/forks/filter-35.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Block 2](../cases/a/block-2.md) · [Filter all](../cases/a/filter-all.md) |
| [Omitted trace_filter range bounds](../decisions/H30.md) | [Filter no bounds](../cases/h30/filter-no-bounds.md) · [Filter to 2 implicit from](../cases/h30/filter-to-2-implicit-from.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |
| [Trace block tags and pending state](../decisions/H32.md) | [Block pending](../cases/h30/block-pending.md) · [Call number pending](../cases/h30/call-number-pending.md) |
| [Single-block hash selection in trace_filter](../decisions/H33.md) | [Filter blockhash](../cases/h30/filter-blockhash.md) · [Filter blockhash address from](../cases/h30/filter-blockhash-address-from.md) |

</details>

[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
