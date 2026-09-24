# Geth draft fork: changes to review

The experimental fork matches the priced-call witnesses but retains the earlier zero-fee BASEFEE-preserving proposal, so its trace_call differs from eth_call and revised H15. Omitted trace_filter bounds also retain the earlier historical-search draft. It is not upstream Geth support or a consensus vote. Filtering remains a bounded scan; pruning still needs runtime coverage.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Tested version | Commit | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| `1.17.7-unstable` | [`fa8ecb92`](https://github.com/banteg/go-ethereum/commit/fa8ecb9242dda61858c44cf43c70d00548fbd7cd) | 2026-09-24 | [2026-09-24](../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 1.17.7-unstable · fa8ecb92 | Proposed change |
| --- | --- | --- |
| [Missing transactions and paths](../decisions/H06.md)<br>A filter bound beyond the head returns -32001. | ⚠️ Differs<br>[Missing block filter](../cases/a/missing-block-filter.md) | Return `-32602`, as the draft already does for a reversed range and as eth_getLogs does. Checked requirements: A range bound beyond the head returns invalid params (-32602), as eth_getLogs does; never a clamped or partial result.<br>[Trace lookup](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L154) · [Replay results](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L123) |
| [Empty output and unrequested components](../decisions/H08.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Model environment free](../cases/coverage/model-environment-free.md) | Modelled execution returns exactly the independently computed bytes.<br>[Replay results](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L123) · [Call simulation](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L53) |
| [Unsigned simulation fees and block environment](../decisions/H15.md)<br>The captured draft eth_call uses BASEFEE 0 while trace_call preserves B for explicit zero and omitted fees: 40 defined-policy pairs differ. Priced upfront debit and positive-price rejection match across methods. The fork implements the earlier H15 proposal and is not an upstream consensus vote. | ⚠️ Differs<br>[Model environment free](../cases/coverage/model-environment-free.md) | Align the draft trace simulation with eth_call’s zero-fee BASEFEE convention for any zero effective price while retaining priced validation and accounting.<br>[Call simulation](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L53) |
| [Fee accounting and sequential state diffs](../decisions/H16.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Many storage write read](../cases/a/many-storage-write-read.md) | Only the first call writes slot zero; reverted writes and later reads add no storage transition.<br>[Call simulation](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L53) · [State differences](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L233) |
| [vmTrace executing bytecode](../decisions/H19.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Auth clear](../cases/a/auth-clear.md) | The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs.<br>[VM execution deltas](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L264) · [Replay results](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L123) |
| [vmTrace step timing and deltas](../decisions/H20.md)<br>MLOAD has no `mem` and a short CALL return reports only the returned bytes; CREATE `cost` omits forwarded gas; code that runs off its end gets a synthetic STOP; an EOA target returns a null vmTrace. | ⚠️ Differs<br>[Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) | Report MLOAD and the full CALL output window, include forwarded gas in CREATE `cost`, drop the synthetic STOP, and return `{code: "0x", ops: []}` for EOA, precompile and empty-code frames. Checked requirements: At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects.<br>[VM execution deltas](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L264) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Replay block tree](../cases/initial/replay-block-tree.md) | Replay VM numeric fields use nonnegative integers; stack words and storage operands use minimal quantities at every depth.<br>[VM execution deltas](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L264) |
| [Omitted trace_filter range bounds](../decisions/H30.md)<br>The experimental draft fork follows the earlier earliest-to-latest proposal: its unbounded query starts at block 1 and its toBlock-only query searches early history. | ⚠️ Differs<br>[Filter no bounds](../cases/h30/filter-no-bounds.md) | Align its omitted-bound behavior with latest/latest and reject the reversed range with `-32602`. This is draft-fork work, not a finding about upstream Geth trace support. |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 1.17.7-unstable · fa8ecb92 | [Raw-transaction block argument](../decisions/H12.md) | 1 policy-open case. The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |
| 1.17.7-unstable · fa8ecb92 | [Trace block tags and pending state](../decisions/H32.md) | 2 policy-open cases. call-number-pending: RPC error -32602. many-number-pending: RPC error -32602. | [Call number pending](../cases/h30/call-number-pending.md) · [Many number pending](../cases/h30/many-number-pending.md) |

Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [trace_get selector and return shape](../decisions/H02.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) |
| [Empty address lists](../decisions/H04.md) | [Filter both null](../cases/a/filter-both-null.md) · [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 35](../cases/forks/replay-35.md) · [Replay 36](../cases/forks/replay-36.md) |
| [Failed frame results and error labels](../decisions/H09.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set revert](../cases/a/auth-set-revert.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Signed transaction execution validity](../decisions/H13.md) | [Raw below basefee](../cases/a/raw-below-basefee.md) · [Raw insufficient funds](../cases/a/raw-insufficient-funds.md) |
| [Invalid-parameter error codes](../decisions/H14.md) | [Call null mode](../cases/a/call-null-mode.md) · [Call scalar mode](../cases/a/call-scalar-mode.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter created to](../cases/a/filter-created-to.md) · [Filter creator from](../cases/a/filter-creator-from.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [Filter 35](../cases/forks/filter-35.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |

</details>

[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
