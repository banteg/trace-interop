# Geth draft fork: changes to review

The experimental fork implements an earlier draft; nullable filters, unknown call fields and the proposed unknown-block code need updates. It is not upstream Geth support. Filtering remains a bounded scan and pruning coverage is incomplete. Signed nonce-mismatch rejection differs from the revised simulation proposal.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| Draft fork | `Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1` | [2026-09-21](https://github.com/banteg/go-ethereum/commit/e29edff514a08c38ed0b08ab67d26a0644c79548) | [2026-09-21](../../evidence/2026-09-21/geth-e29edff-a/manifest.json)<br>[2026-09-22](../../evidence/2026-09-23/h03-modes-geth-a/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.

## Changes to discuss

| Behavior | Draft fork | Proposed change |
| --- | --- | --- |
| [Filter composition and mode](../decisions/H03.md)<br>The draft fork implements the earlier baseline: it rejects `mode: "intersection"` and `mode: "union"` with `-32602`. | Differs<br>[Filter from only intersection](../cases/a/filter-from-only-intersection.md) | Accept `intersection` (identical to the default) and `union` (match either populated list); keep rejecting unknown values.<br>[Address filtering](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L186) |
| [Empty address lists](../decisions/H04.md)<br>Null address lists are rejected, while the revised draft treats them as unrestricted. | Differs<br>[Filter both null](../cases/a/filter-both-null.md) | Accept null like an omitted or empty list, then apply the other filter normally. Checked requirements: Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.<br>[Address filtering](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L186) |
| [Missing transactions and paths](../decisions/H06.md)<br>Unknown selected blocks use a different error code from the revised draft. | Differs<br>[Missing block block](../cases/a/missing-block-block.md) | Use -32001 for unknown blocks, preserving null for missing transactions and 4444 for pruned state. Checked requirements: An unknown selected block or range endpoint returns Resource not found (-32001).<br>[Trace lookup](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L153) · [Replay results](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L122) |
| [Nonce-mismatch policy for signed simulation](../decisions/H13.md)<br>The high-nonce signed transfer is rejected instead of simulated. | Differs<br>[Raw nonce high](../cases/a/raw-nonce-high.md) | If the proposed nonce policy is adopted, permit nonce-mismatch simulation. This is a compatibility decision, not evidence of a nonce-rewriting bug; other validation checks remain separate. Checked requirements: Proposed nonce policy: simulate this otherwise valid transfer despite its signed nonce being above the state nonce.<br>[Signed transaction replay](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L97) |
| [Invalid-parameter error codes](../decisions/H14.md)<br>Unknown call-object fields are rejected by the older draft implementation. | Differs<br>[Call unknown field](../cases/a/call-unknown-field.md) | Ignore unknown call fields for forward compatibility while validating known fields. Checked requirements: Unknown call-object fields are ignored without changing execution output.<br>[Signed transaction replay](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L97) · [Call simulation](https://github.com/banteg/go-ethereum/blob/e29edff514a08c38ed0b08ab67d26a0644c79548/eth/tracers/trace_namespace.go#L52) |

## Extension observations

These requests explicitly select behavior outside the portable baseline. Acceptance or rejection is not a conformance verdict.

| Build | Extension | Observed | Example |
| --- | --- | --- | --- |
| Draft fork | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |

**Partially assessed:** some declared cases lack an evaluated assertion. [trace_get selector and return shape](../decisions/H02.md), [Post-merge reward records](../decisions/H05.md), [Replay transactionHash field](../decisions/H07.md), [Failed frame results and error labels](../decisions/H09.md), [Creation result field names](../decisions/H10.md), [Unsigned simulation fees and block environment](../decisions/H15.md), [Fee accounting and sequential state diffs](../decisions/H16.md), [New-account stateDiff encoding](../decisions/H17.md), [EIP-7702 code changes in stateDiff](../decisions/H18.md), [vmTrace executing bytecode](../decisions/H19.md), [vmTrace step timing and deltas](../decisions/H20.md), [vmTrace numeric and optional metadata encoding](../decisions/H21.md), [Special-action address matching](../decisions/H23.md), [Sibling failure isolation](../decisions/H24.md), [Filter execution across fork boundaries](../decisions/H27.md).

<details><summary>Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
