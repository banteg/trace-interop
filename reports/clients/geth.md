# Geth draft fork: changes to review

The experimental fork matches most evaluated semantic assertions, including signed-transaction rejection codes, unknown-block errors and call-field handling. Its omitted trace_filter bounds still follow the earlier historical-search draft and differ from the proposed latest/latest default. It is not upstream Geth support. Filtering remains a bounded scan; pruning and other unassessed cases still need coverage.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| 🧪 Draft fork | `Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1` | [2026-09-23](https://github.com/banteg/go-ethereum/commit/c36ee43e3827331276d045bd56d1297e4c3c9b15) | [2026-09-23](../../evidence/2026-09-23/geth-contract-sync/geth-contract-a/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 🧪 Draft fork | Proposed change |
| --- | --- | --- |
| [trace_get selector and return shape](../decisions/H02.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Transaction missing](../cases/initial/transaction-missing.md) | Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.<br>[Trace lookup](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_namespace.go#L154) |
| [Fee accounting and sequential state diffs](../decisions/H16.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Call many](../cases/initial/call-many.md) | Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. The declared state-diff fixture returns the requested account changes.<br>[Call simulation](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_namespace.go#L53) · [State differences](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_capture.go#L233) |
| [vmTrace executing bytecode](../decisions/H19.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Replay block tree](../cases/initial/replay-block-tree.md) | The replay/raw root VM uses the frozen initcode or resolved one-hop execution code.<br>[VM execution deltas](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_capture.go#L264) · [Replay results](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_namespace.go#L123) |
| [vmTrace step timing and deltas](../decisions/H20.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Call tree vmtrace](../cases/initial/call-tree-vmTrace.md) | At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded.<br>[VM execution deltas](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_capture.go#L264) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Replay block tree](../cases/initial/replay-block-tree.md) | Replay VM numeric fields use nonnegative integers and stack words use minimal quantities at every depth.<br>[VM execution deltas](https://github.com/banteg/go-ethereum/blob/c36ee43e3827331276d045bd56d1297e4c3c9b15/eth/tracers/trace_capture.go#L264) |
| [Omitted trace_filter range bounds](../decisions/H30.md)<br>The experimental draft fork follows the earlier earliest-to-latest proposal: its unbounded query starts at block 1 and its toBlock-only query searches early history. | ⚠️ Differs<br>[Filter no bounds](../cases/h30/filter-no-bounds.md) | Align its omitted-bound behavior with latest/latest and reject the reversed range. This is draft-fork work, not a finding about upstream Geth trace support. |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 🧪 Draft fork | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |
| 🧪 Draft fork | [Trace block tags and pending state](../decisions/H32.md) | filter-pending: RPC error -32602. call-number-pending: RPC error -32602. many-number-pending: RPC error -32602. | [Call number pending](../cases/h30/call-number-pending.md) · [Filter 0 to 2](../cases/h30/filter-0-to-2.md) |

**🟡 Partially assessed:** some declared cases lack an evaluated assertion. [Filter composition and mode](../decisions/H03.md).

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Empty address lists](../decisions/H04.md) | [Filter both null](../cases/a/filter-both-null.md) · [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Missing transactions and paths](../decisions/H06.md) | [Missing block block](../cases/a/missing-block-block.md) · [Missing block call](../cases/a/missing-block-call.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 35](../cases/forks/replay-35.md) · [Replay 36](../cases/forks/replay-36.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Failed frame results and error labels](../decisions/H09.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set revert](../cases/a/auth-set-revert.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Call number default](../cases/h30/call-number-default.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Signed transaction execution validity](../decisions/H13.md) | [Raw below basefee](../cases/a/raw-below-basefee.md) · [Raw insufficient funds](../cases/a/raw-insufficient-funds.md) |
| [Invalid-parameter error codes](../decisions/H14.md) | [Call null mode](../cases/a/call-null-mode.md) · [Call scalar mode](../cases/a/call-scalar-mode.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | [Call constructor](../cases/initial/call-constructor.md) · [Call constructor priced](../cases/initial/call-constructor-priced.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) · [Call constructor](../cases/initial/call-constructor.md) |
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
