# Reth: changes to review

The main changes are tree-path lookup, filter composition, replay metadata, and missing code changes in state/VM traces.

[All clients](../README.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| Development | `Reth Version: 2.5.2+03cb186c` | [2026-09-20](https://github.com/paradigmxyz/reth/commit/03cb186c1d36eebbacc7bda08f36e25711d0804e) | [2026-09-21](../../evidence/2026-09-21/precompiles-final/manifest.json) |

**The nightly is newer despite its lower version number.** Its commit is from September 20, while the release commit is from September 17. The release-only version bump set `2.6.0`; the nightly still declares `2.5.2`. [Compare the tested revisions](https://github.com/paradigmxyz/reth/compare/73a3a00862a8f14f89e30da8de001456f18cfae0...03cb186c1d36eebbacc7bda08f36e25711d0804e).

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.

## Changes to discuss

| Behavior | Development | Proposed change |
| --- | --- | --- |
| [trace_get selector and return shape](../decisions/H02.md)<br>The selector uses a flat index; `[]` returns `null` and nested paths do not work. | Differs<br>[Get nested parent](../cases/a/get-nested-parent.md) | Walk one `traceAddress` path instead. Return the root for `[]`, and one object or `null` for other paths. Existing flat-index callers will need a migration path.<br>[Trace lookup](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L220) |
| [Filter composition and mode](../decisions/H03.md)<br>Sender and recipient lists are combined with OR by default. | Differs<br>[Filter both](../cases/initial/filter-both.md) | Use AND between lists so a second filter narrows the search; preserve union only as an explicit extension.<br>[Address filtering](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L363) |
| [Missing transactions and paths](../decisions/H06.md)<br>Missing individual replays return an error; verified pruned-history requests use `-32603`. | Differs<br>[Replay missing](../cases/initial/replay-missing.md) | Return `null` for absent transactions. For known transactions whose state is unavailable, use the proposed history-unavailable error (`4444`) rather than an internal error.<br>[Trace lookup](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L220) · [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [Replay transactionHash field](../decisions/H07.md)<br>Individual replay results omit `transactionHash`. | Differs<br>[Replay 7702 statediff](../cases/initial/replay-7702-stateDiff.md) | Include the requested transaction hash in the replay envelope, consistently with block replay.<br>[Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [Raw-transaction block argument](../decisions/H12.md)<br>Raw-transaction tracing accepts a third block-selector argument. | Differs<br>[Raw valid](../cases/initial/raw-valid.md) | Agree how to retain this extension alongside the draft’s two-argument baseline. This is a compatibility decision, not an execution defect.<br>[Signed transaction replay](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L121) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md)<br>EIP-7702 delegation code changes are missing from `stateDiff`. | Differs<br>[Auth clear](../cases/a/auth-clear.md) | Include authorization code set, replacement and clearing, even for existing accounts and when the subsequent execution reverts.<br>[State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) · [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [vmTrace executing bytecode](../decisions/H19.md)<br>Creation `vmTrace.code` does not contain the expected executing initcode. | Differs<br>[Call constructor](../cases/initial/call-constructor.md) | Attach the creation frame’s initcode to its VM trace, including in block replay.<br>[VM trace builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L317) · [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [Account deletion across Cancun](../decisions/H26.md)<br>Pre-Cancun account deletion loses code/nonce deletion markers. | Differs<br>[Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) | Report the removed code and nonce before Cancun; preserve existing accounts after EIP-6780.<br>[State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) |

**Reward record shape:** the checked PoW rewards omit `transactionHash` and `transactionPosition`; the draft requires explicit `null` values for non-transaction records. [Compare a reward response](../cases/forks/block-35.md).

<details><summary>Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Empty address lists](../decisions/H04.md) | [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) · [Filter to empty from set](../cases/a/filter-to-empty-from-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [Block 2](../cases/a/block-2.md) · [Block 3](../cases/a/block-3.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Failed frame results and error labels](../decisions/H09.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set revert](../cases/a/auth-set-revert.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Call constructor](../cases/initial/call-constructor.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Signed transaction nonce validation](../decisions/H13.md) | [Raw nonce high](../cases/a/raw-nonce-high.md) · [Raw nonce high](../cases/repeat/raw-nonce-high.md) |
| [Invalid-parameter error codes](../decisions/H14.md) | [Call scalar mode](../cases/a/call-scalar-mode.md) · [Call unknown mode](../cases/a/call-unknown-mode.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | [Call constructor](../cases/initial/call-constructor.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Fee accounting and sequential state diffs](../decisions/H16.md) | [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) · [Many storage write revert read](../cases/repeat/many-storage-write-revert-read.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) |
| [vmTrace step timing and deltas](../decisions/H20.md) | [Call mcopy](../cases/a/call-mcopy.md) · [Call mcopy](../cases/repeat/call-mcopy.md) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter created to](../cases/a/filter-created-to.md) · [Filter creator from](../cases/a/filter-creator-from.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call value0 failed](../cases/precompiles/nested-call-value0-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [Filter 35](../cases/forks/filter-35.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call value0 failed](../cases/precompiles/nested-call-value0-failed.md) · [Nested call value0 success](../cases/precompiles/nested-call-value0-success.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
