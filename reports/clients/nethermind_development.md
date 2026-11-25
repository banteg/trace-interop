# Nethermind: changes to review

2.2.2 · be201120, like 2.2.1, agrees on filter modes and empty address lists (#13857), post-merge and genesis reward records (#13938, #13783, #13801), vmTrace steps (#13940, #13958), precheck and collision frames (#13957), failed-frame results and labels (#13981) and null for a missing transaction or replay (#13937, #14037). It also validates trace_rawTransaction as block inclusion does (#14091), rejects disagreeing data and input (#14089), rejects block-hash filter bounds and selects one block with the trace_filter blockHash member (#14111), runs blob calls without a positive blob fee cap at BLOBBASEFEE 0 (#14092) and answers rejected calls with the eth_simulateV1 codes (#14158). It agrees on 27 decisions. Its release branch was cut before #14212 and #14663, so an explicit type still adds requirements, fields a call’s fork lacks run, a lone maxFeePerBlobGas is ignored, and an account override with both state and stateDiff is accepted (H14). Master includes both, and #14888 adds the forms the draft pinned for exact fixtures (5e6717fe): result null on halted frames, rewards and SELFDESTRUCT records (H09), null reward transaction fields (H05), vmTrace op (H21) and -32001 for an unknown block (H06). With #15017, a noncanonical trace_filter blockHash also returns -32001 (H33), so 2.3.0-preview · 4079edfa agreed on all 33 decisions. 2.4.0-preview · e2f069a6 agrees on 32: it runs a trace_call whose `data` and `input` disagree, executing `input`, which #14089 had rejected (H14). A code sender’s rejection message, gas-defaulting probes its funds cannot cover and the legacy-priced authorization list remain unassessed or open.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Tested version | Commit | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| `2.4.0-preview` | [`e2f069a6`](https://github.com/NethermindEth/nethermind/commit/e2f069a658b58798fba678444271ec99ff6ff3c7) | 2026-11-25 | [2026-11-25](../../evidence/2026-11-25/eval/initial/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 2.4.0-preview · e2f069a6 | Proposed change |
| --- | --- | --- |
| [Invalid parameters and rejected calls](../decisions/H14.md)<br>Malformed raw input, negative filter count and integer paths expose validation differences across the captured builds. An unpriced call with a null `blobVersionedHashes` or `authorizationList` takes that member’s transaction type: 2.1.0-preview · 45912ba3 rejects it with -32000 (“need at least 1 blob”, “EIP-7702 transaction cannot be used to create contract”) and 2.0.0 truncates the authorizationList response. 2.2.0-preview · 759efed7 treats a null member as omitted (#14049), rejects a negative filter count (#14050) and rejects disagreeing `data` and `input` with -32602 (#14089). The fee and type and fork probes, measured in the matrix since 2026-10-04, add two differences in every build: an explicit `type` picks the call's class and drops the fields it lacks (type 0 or 1 with dynamic fees runs at GASPRICE 0, type 2 with an authorization list ignores it), and a field before its fork fails with -32603 (access and authorization lists) or runs (dynamic fees at the tip, blob hashes before Cancun). 2.2.2 accepts an account override that sets both state and stateDiff and applies its code; master rejects it. 2.4.0-preview · e2f069a6 runs a call whose `data` and `input` disagree, executing `input`, which #14089 had rejected. | ⚠️ Differs<br>[Field data input differ](../cases/probes-prague/field-data-input-differ.md) | Ship #14049, #14050 and #14089 in a release: reject malformed input, such as a negative filter count or disagreeing `data` and `input` (`-32602` recommended), and treat a null member as omitted, so it selects no transaction type. Merge #14212: the fields decide a call's type, and a field the call's fork lacks is rejected. Checked requirements: Malformed input returns an error (-32602 recommended). Disagreeing data and input are rejected (-32602 recommended).<br>[Signed transaction replay](https://github.com/NethermindEth/nethermind/blob/641592d2b96fa1e2fa8e8a0b1761582a1728bd51/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L150) · [Call simulation](https://github.com/NethermindEth/nethermind/blob/641592d2b96fa1e2fa8e8a0b1761582a1728bd51/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L78) |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 2.4.0-preview · e2f069a6 | [Raw-transaction block argument](../decisions/H12.md) | 6 extension cases. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2). Selector latest: rejected as invalid params (-32602: too many arguments, want at most 2). Selector block 0x19 by number: rejected as invalid params (-32602: too many arguments, want at most 2). Selector block 0x19 by hash: rejected as invalid params (-32602: too many arguments, want at most 2). Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: too many arguments, want at most 2). Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2). | [Raw valid](../cases/initial/raw-valid.md) · [Raw state hash](../cases/raw-selector/raw-state-hash.md) |

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
| [Raw-transaction block argument](../decisions/H12.md) | [Raw valid current nonce](../cases/initial/raw-valid-current-nonce.md) · [Raw state default](../cases/raw-selector/raw-state-default.md) |
| [Signed transaction execution validity](../decisions/H13.md) | [Raw below basefee](../cases/a/raw-below-basefee.md) · [Raw insufficient funds](../cases/a/raw-insufficient-funds.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | [Many storage write read](../cases/a/many-storage-write-read.md) · [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) |
| [Fee accounting and sequential state diffs](../decisions/H16.md) | [Many storage write read](../cases/a/many-storage-write-read.md) · [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) |
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
| [Trace block tags and pending state](../decisions/H32.md) | [Call number pending](../cases/h30/call-number-pending.md) · [Filter earliest](../cases/h30/filter-earliest.md) |
| [Single-block hash selection in trace_filter](../decisions/H33.md) | [Filter blockhash](../cases/h30/filter-blockhash.md) · [Filter blockhash address from](../cases/h30/filter-blockhash-address-from.md) |

</details>

[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
