# Geth draft fork: changes to review

The experimental fork matches the selected assertions. It is a place to try the draft, not upstream Geth support; historical filtering is a bounded scan and pruning coverage remains incomplete.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| Draft fork | `Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1` | [2026-09-21](https://github.com/banteg/go-ethereum/commit/e29edff514a08c38ed0b08ab67d26a0644c79548) | [2026-09-21](../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.

## Changes to discuss

No differences were found by the selected semantic assertions.

## Extension observations

These requests explicitly select behavior outside the portable baseline. Acceptance or rejection is not a conformance verdict.

| Build | Extension | Observed | Example |
| --- | --- | --- | --- |
| Draft fork | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request was rejected as invalid params. | [Raw valid](../cases/initial/raw-valid.md) |

<details><summary>Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [trace_get selector and return shape](../decisions/H02.md) | [Get nested parent](../cases/a/get-nested-parent.md) · [Get nested positive](../cases/a/get-nested-positive.md) |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter all](../cases/initial/filter-all.md) |
| [Empty address lists](../decisions/H04.md) | [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) · [Filter to empty from set](../cases/a/filter-to-empty-from-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Missing transactions and paths](../decisions/H06.md) | [Get missing](../cases/initial/get-missing.md) · [Get missing tx](../cases/initial/get-missing-tx.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 7702 statediff](../cases/initial/replay-7702-stateDiff.md) · [Replay 7702 trace](../cases/initial/replay-7702-trace.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Failed frame results and error labels](../decisions/H09.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set revert](../cases/a/auth-set-revert.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Call constructor](../cases/initial/call-constructor.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Signed transaction nonce validation](../decisions/H13.md) | [Raw nonce high](../cases/a/raw-nonce-high.md) · [Raw nonce high](../cases/repeat/raw-nonce-high.md) |
| [Invalid-parameter error codes](../decisions/H14.md) | [Call scalar mode](../cases/a/call-scalar-mode.md) · [Call unknown mode](../cases/a/call-unknown-mode.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | [Call constructor](../cases/initial/call-constructor.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Fee accounting and sequential state diffs](../decisions/H16.md) | [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) · [Many storage write revert read](../cases/repeat/many-storage-write-revert-read.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace executing bytecode](../decisions/H19.md) | [Call constructor](../cases/initial/call-constructor.md) · [Call constructor priced](../cases/initial/call-constructor-priced.md) |
| [vmTrace step timing and deltas](../decisions/H20.md) | [Call mcopy](../cases/a/call-mcopy.md) · [Call mcopy](../cases/repeat/call-mcopy.md) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set](../cases/a/auth-set.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter created to](../cases/a/filter-created-to.md) · [Filter creator from](../cases/a/filter-creator-from.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call value0 failed](../cases/precompiles/nested-call-value0-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) · [Destroy trace 56](../cases/fork-followup/destroy-trace-56.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [Filter 35](../cases/forks/filter-35.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call value0 failed](../cases/precompiles/nested-call-value0-failed.md) · [Nested call value0 success](../cases/precompiles/nested-call-value0-success.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
