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
| [Omitted trace_filter range bounds](../decisions/H30.md)<br>The experimental draft fork follows the earlier earliest-to-latest proposal: its unbounded query starts at block 1 and its toBlock-only query searches early history. | ⚠️ Differs<br>[Filter no bounds](../cases/h30/filter-no-bounds.md) | Align its omitted-bound behavior with latest/latest and reject the reversed range. This is draft-fork work, not a finding about upstream Geth trace support. |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 🧪 Draft fork | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |
| 🧪 Draft fork | [Trace block tags and pending state](../decisions/H32.md) | filter-pending: RPC error -32602. call-number-pending: RPC error -32602. many-number-pending: RPC error -32602. | [Call number pending](../cases/h30/call-number-pending.md) · [Filter earliest](../cases/h30/filter-earliest.md) |

**🟡 Partially assessed:** some declared cases lack an evaluated assertion. [trace_get selector and return shape](../decisions/H02.md), [Empty address lists](../decisions/H04.md), [Post-merge reward records](../decisions/H05.md), [Missing transactions and paths](../decisions/H06.md), [Replay transactionHash field](../decisions/H07.md), [Failed frame results and error labels](../decisions/H09.md), [Creation result field names](../decisions/H10.md), [Invalid-parameter error codes](../decisions/H14.md), [Unsigned simulation fees and block environment](../decisions/H15.md), [Fee accounting and sequential state diffs](../decisions/H16.md), [New-account stateDiff encoding](../decisions/H17.md), [EIP-7702 code changes in stateDiff](../decisions/H18.md), [vmTrace executing bytecode](../decisions/H19.md), [vmTrace step timing and deltas](../decisions/H20.md), [vmTrace numeric and optional metadata encoding](../decisions/H21.md), [Special-action address matching](../decisions/H23.md), [Sibling failure isolation](../decisions/H24.md), [Filter execution across fork boundaries](../decisions/H27.md).

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Signed transaction execution validity](../decisions/H13.md) | [Raw below basefee](../cases/a/raw-below-basefee.md) · [Raw insufficient funds](../cases/a/raw-insufficient-funds.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
