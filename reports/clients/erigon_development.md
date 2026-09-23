# Erigon: changes to review

The tested development build agrees on several cases that differ in the release, including tree lookup, MCOPY and historical system state. Default filter composition still needs attention; signed-transaction validity checks and error codes need alignment with the proposal. Omitted trace_filter bounds currently search history and differ from the proposed latest/latest default.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| 🛠️ Development | `3.8.0-dev-c25b8e47` | [2026-09-21](https://github.com/erigontech/erigon/commit/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec) | [2026-09-22](../../evidence/2026-09-23/harness-audit-native-a/manifest.json)<br>[2026-09-23](../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 🛠️ Development | Proposed change |
| --- | --- | --- |
| [trace_get selector and return shape](../decisions/H02.md)<br>Root and nested `trace_get` requests fail or select the wrong record. | ⚠️ Differs<br>[Transaction missing](../cases/initial/transaction-missing.md) | Interpret the selector as one `traceAddress` path: `[]` selects the root, `[0]` its first child. Checked requirements: Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.<br>[Trace lookup](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L135) |
| [Filter composition and mode](../decisions/H03.md)<br>Both lists are combined with OR by default (6 records instead of 1). With `mode: "intersection"`, a one-sided filter returns `[]` instead of treating the empty side as unrestricted. The unrecognized `mode: "garbage"` is accepted and treated as union. | ⚠️ Differs<br>[Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) | Make intersection the default. Under either mode, ignore an omitted, null or empty side. Reject unknown mode values with `-32602`.<br>[Address filtering](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L311) |
| [Missing transactions and paths](../decisions/H06.md)<br>Missing-transaction lookup can return an RPC error, and an unknown filter endpoint can return []. | ⚠️ Differs<br>[Missing block block](../cases/a/missing-block-block.md) | Return `null` for a missing transaction or path; reserve errors for unavailable history and invalid requests. Checked requirements: An unknown selected block or range endpoint returns Resource not found (-32001).<br>[Trace lookup](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L135) · [Replay results](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L880) |
| [Empty trace-type selection](../decisions/H11.md)<br>Empty-selection requests include rejected calls; the zero-fee case also fails the fee rule. | ⚠️ Differs<br>[Call empty types](../cases/initial/call-empty-types.md) | Accept an empty selection and return the execution envelope. Recheck alongside H15 before treating every rejection as a separate selection bug. Checked requirements: An empty trace-type selection executes and preserves the fixture return bytes.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Signed transaction execution validity](../decisions/H13.md)<br>Marker probes execute nonce mismatches, both insufficient-funds cases and ordinary-code-sender transactions. CREATE uses the state-nonce address. Chain, intrinsic-gas and base-fee failures are rejected with -32000. Review feedback supports stricter validation. | ⚠️ Differs<br>[Raw below basefee](../cases/a/raw-below-basefee.md) | Apply selected-state execution validity before running signed transactions. Distinguish validation rejection from execution failure, and use the proposed -32003 code for validation errors. Checked requirements: Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected).<br>[Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) |
| [Invalid-parameter error codes](../decisions/H14.md)<br>Malformed raw transactions and an unknown option use error codes other than `-32602`. | ⚠️ Differs<br>[Call unknown mode](../cases/a/call-unknown-mode.md) | Use JSON-RPC invalid params (`-32602`) for malformed input, separately from execution rejection. Checked requirements: Malformed input returns invalid params (-32602).<br>[Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) · [Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Unsigned simulation fees and block environment](../decisions/H15.md)<br>Explicit zero-fee unsigned calls are rejected. | ⚠️ Differs<br>[Call constructor](../cases/initial/call-constructor.md) | Allow zero-fee unsigned simulation without changing the block’s `BASEFEE` opcode value. Checked requirements: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) |
| [Fee accounting and sequential state diffs](../decisions/H16.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Many storage write read](../cases/a/many-storage-write-read.md) | Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Return one execution envelope per input call, in order. The declared state-diff fixture returns the requested account changes.<br>[Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) · [State differences](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L741) |
| [vmTrace executing bytecode](../decisions/H19.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Replay block tree](../cases/initial/replay-block-tree.md) | The replay/raw root VM uses the frozen initcode or resolved one-hop execution code.<br>[VM execution deltas](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L545) · [Replay results](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L880) |
| [vmTrace step timing and deltas](../decisions/H20.md)<br>The `MCOPY` step omits its memory write. | ⚠️ Differs<br>[Call tree vmtrace priced](../cases/initial/call-tree-vmTrace-priced.md) | Record the same-step memory delta, including the copied word at offset 32. Checked requirements: At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded.<br>[VM execution deltas](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L545) |
| [Omitted trace_filter range bounds](../decisions/H30.md)<br>Omitting both bounds starts at block 1 rather than head 48. Supplying only toBlock 2 searches the early range. | ⚠️ Differs<br>[Filter no bounds](../cases/h30/filter-no-bounds.md) | Default an omitted fromBlock to latest. Limit an entirely unbounded request to the current head; return a range error when an explicit end precedes that implicit start.<br>[Filter range defaults](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L335) |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 🛠️ Development | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |
| 🛠️ Development | [Trace block tags and pending state](../decisions/H32.md) | filter-pending: RPC error -32000. call-number-pending: RPC error -32000. many-number-pending: RPC error -32000. | [Call number pending](../cases/h30/call-number-pending.md) · [Filter 0 to 2](../cases/h30/filter-0-to-2.md) |

Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.

**🟡 Partially assessed:** some declared cases lack an evaluated assertion. [Failed frame results and error labels](../decisions/H09.md), [Creation result field names](../decisions/H10.md), [New-account stateDiff encoding](../decisions/H17.md), [vmTrace numeric and optional metadata encoding](../decisions/H21.md).

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Empty address lists](../decisions/H04.md) | [Filter both null](../cases/a/filter-both-null.md) · [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 35](../cases/forks/replay-35.md) · [Replay 36](../cases/forks/replay-36.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter created to](../cases/a/filter-created-to.md) · [Filter creator from](../cases/a/filter-creator-from.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [Block 35](../cases/forks/block-35.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
