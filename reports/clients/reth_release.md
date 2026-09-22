# Reth: changes to review

The main changes are tree-path lookup, filter composition, replay metadata, and missing code changes in state/VM traces. Signed execution validation now matches the restored direction; error codes still need alignment.

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Build | Tested version | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| Release | `Reth Version: 2.6.0+73a3a008` | [2026-09-17](https://github.com/paradigmxyz/reth/commit/73a3a00862a8f14f89e30da8de001456f18cfae0) | [2026-09-21](../../evidence/2026-09-21/precompiles-final/manifest.json)<br>[2026-09-22](../../evidence/2026-09-23/h03-modes-a/manifest.json) |

**The nightly is newer despite its lower version number.** Its commit is from September 20, while the release commit is from September 17. The release-only version bump set `2.6.0`; the nightly still declares `2.5.2`. [Compare the tested revisions](https://github.com/paradigmxyz/reth/compare/73a3a00862a8f14f89e30da8de001456f18cfae0...03cb186c1d36eebbacc7bda08f36e25711d0804e).

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method.

## Changes to discuss

| Behavior | Release | Proposed change |
| --- | --- | --- |
| [trace_get selector and return shape](../decisions/H02.md)<br>The selector uses a flat index; `[]` returns `null` and nested paths do not work. | Differs<br>[Get nested parent](../cases/a/get-nested-parent.md) | Walk one `traceAddress` path instead. Return the root for `[]`, and one object or `null` for other paths. Existing flat-index callers will need a migration path. Checked requirements: Return the transaction-tree record at [6, 0], or null if absent. Return the transaction-tree record at [6], or null if absent. Return the transaction-tree record at [], or null if absent. Return the transaction-tree record at [0], or null if absent. Return the transaction-tree record at [1], or null if absent. Return one object whose traceAddress equals [].<br>[Trace lookup](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L220) |
| [Filter composition and mode](../decisions/H03.md)<br>Both lists are combined with OR by default (6 records instead of 1). One-sided and explicit-mode queries agree. | Differs<br>[Filter both](../cases/initial/filter-both.md) | Take up Alloy #4216, which makes intersection the default and keeps explicit union, then retest.<br>[Address filtering](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L363) |
| [Empty address lists](../decisions/H04.md)<br>Null address lists are rejected, while the revised draft treats them as unrestricted. | Differs<br>[Filter both null](../cases/a/filter-both-null.md) | Accept null like an omitted or empty list, then apply the other filter normally. Checked requirements: Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.<br>[Address filtering](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L363) |
| [Missing transactions and paths](../decisions/H06.md)<br>Missing individual replays return an error; verified pruned-history requests use `-32603`. | Differs<br>[Replay missing](../cases/initial/replay-missing.md) | Return `null` for absent transactions. For known transactions whose state is unavailable, use the proposed history-unavailable error (`4444`) rather than an internal error. Checked requirements: Unknown transaction returns null, not an empty collection or RPC error. Unavailable historical state uses the proposed pruned-history error (4444).<br>[Trace lookup](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L220) · [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [Replay transactionHash field](../decisions/H07.md)<br>Individual replay results omit `transactionHash`. | Differs<br>[Replay 7702 statediff](../cases/initial/replay-7702-stateDiff.md) | Include the requested transaction hash in the replay envelope, consistently with block replay. Checked requirements: Individual replay includes its transactionHash.<br>[Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [Signed transaction execution validity](../decisions/H13.md)<br>All fresh invalid probes are rejected, using -32000 or -32003. Valid EOA/delegated controls execute, and valid execution-OOG returns a trace halt. | Differs<br>[Raw below basefee](../cases/a/raw-below-basefee.md) | Retain execution validation and align rejection codes with the proposed -32003 mapping once agreed. Checked requirements: Proposed transaction-validation error code: -32003 (Transaction rejected).<br>[Signed transaction replay](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L121) |
| [Invalid-parameter error codes](../decisions/H14.md)<br>An integer trace_get path returns null instead of invalid params. | Differs<br>[Get integer path](../cases/a/get-integer-path.md) | Reject integer path entries with -32602; callers must convert output path integers to hex quantities. Checked requirements: Malformed input returns invalid params (-32602).<br>[Signed transaction replay](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L121) · [Call simulation](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L97) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md)<br>EIP-7702 delegation code changes are missing from `stateDiff`. | Differs<br>[Auth clear](../cases/a/auth-clear.md) | Include authorization code set, replacement and clearing, even for existing accounts and when the subsequent execution reverts. Checked requirements: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.<br>[State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) · [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [vmTrace executing bytecode](../decisions/H19.md)<br>Creation `vmTrace.code` does not contain the expected executing initcode. | Differs<br>[Call constructor](../cases/initial/call-constructor.md) | Attach the creation frame’s initcode to its VM trace, including in block replay. Checked requirements: Creation vmTrace.code is executing initcode.<br>[VM trace builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L317) · [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) |
| [Account deletion across Cancun](../decisions/H26.md)<br>Pre-Cancun account deletion loses code/nonce deletion markers. | Differs<br>[Destroy trace 55](../cases/fork-followup/destroy-trace-55.md) | Report the removed code and nonce before Cancun; preserve existing accounts after EIP-6780. Checked requirements: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.<br>[State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) |

## Extension observations

These requests explicitly select behavior outside the portable baseline. Acceptance or rejection is not a conformance verdict.

| Build | Extension | Observed | Example |
| --- | --- | --- | --- |
| Release | [Raw-transaction block argument](../decisions/H12.md) | The third-argument request returned a result; this does not prove which block state was used. | [Raw valid](../cases/initial/raw-valid.md) |

Result-shape differences are recorded on the [case pages](../technical.md#result-shape-checks); schema validity is separate from semantic coverage.

**Partially assessed:** some declared cases lack an evaluated assertion. [Post-merge reward records](../decisions/H05.md), [Failed frame results and error labels](../decisions/H09.md), [Creation result field names](../decisions/H10.md), [Unsigned simulation fees and block environment](../decisions/H15.md), [Fee accounting and sequential state diffs](../decisions/H16.md), [New-account stateDiff encoding](../decisions/H17.md), [vmTrace step timing and deltas](../decisions/H20.md), [vmTrace numeric and optional metadata encoding](../decisions/H21.md), [Special-action address matching](../decisions/H23.md), [Sibling failure isolation](../decisions/H24.md), [Filter execution across fork boundaries](../decisions/H27.md).

<details><summary>Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Beacon call 55](../cases/fork-followup/beacon-call-55.md) · [Beacon call 56](../cases/fork-followup/beacon-call-56.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) · [Nested call outer0 value1 success](../cases/precompile-values/nested-call-outer0-value1-success.md) |

</details>

[Method availability](../decisions/H01.md) · [All behavior decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
