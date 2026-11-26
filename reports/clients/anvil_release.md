# Anvil: changes to review

Foundry’s development node, captured by replaying each chain instead of through Hive. Foundry 1.8.5 · 51a52c59 shipped ten trace-interop fixes (#17301–#17304, #17306, #17307, #17309–#17312): tree-path trace_get, missing blocks and replays, replay transaction hashes, mined traces without nested precompile frames, EIP-3607 rejection for signed raw transactions, conflicting call fields, pending in block trace methods, and the fee-free, cap-only and omitted-gas call environment. With revm-inspectors 0.44.1 (#17226) it also carries the reverted-CREATE results, failure labels and vmTrace fixes. 1.8.6 · 6bad0a66 carried the same fixes and agreed on 18 decisions; it accepted integer trace_get indices, executed calls priced below the base fee and could not set a parent beacon root, so the mined-probes chain was not replayed on it. 1.9.0 · 6056c584 added #17305, #17308, #17419 (by figtracer) and #17777, the draft's pinned -32001 for an unknown block (H06): it replayed mined-probes and agreed on 28 decisions. 1.10.0 · 083e2299 and the nightly 1.10.1-nightly · 50d75f19 replace revm and revm-inspectors with evm2 and take Alloy 2.6.1: the post-Cancun self-destruct-to-self payload is reported (H23, H26) and null filter address lists are omitted (H04, Alloy #4257). Both agree on 30 decisions. With evm2 they share Reth’s vmTrace CREATE cost, which leaves out the forwarded gas (H20, evm2 #876); they still lack the trace_filter block tags (H32, Alloy #4442), and they parse the trace_filter blockHash member but ignore it (H33).

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Tested version | Commit | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| `1.10.0` | [`083e2299`](https://github.com/foundry-rs/foundry/commit/083e22994195d6a7e3ad3104d0b57f478c9b9062) | 2026-11-19 | [2026-11-25](../../evidence/2026-11-25/eval/initial/manifest.json)<br>[2026-11-26](../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 1.10.0 · 083e2299 | Proposed change |
| --- | --- | --- |
| [vmTrace step timing and deltas](../decisions/H20.md)<br>1.8.3 locks revm-inspectors 0.43.0 (whole-memory `mem`, pre-operation `used`, no `store`). 1.8.4 and the nightly 328811cb ship 0.44.1 (#532): memory and subs follow execution, MLOAD reports its memory, there is no synthetic STOP, and a call that fails its precheck has no `sub`. The nightly 32624734 replays mined-probes through #17305 and agrees there too. 1.9.0 · 6056c584 includes #17305 and replays mined-probes too. 1.10.0 · 083e2299 and the nightly 50d75f19 run evm2: the CREATE in call-tree-vmTrace costs 32,002 where Erigon, Nethermind and the Geth draft report 480,269, as on Reth. | ⚠️ Differs<br>[Call tree vmtrace](../cases/initial/call-tree-vmTrace.md) | Take evm2#876, which adds the gas forwarded to a CREATE or CREATE2 to its vmTrace `cost`. Checked requirements: At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem.<br>[VM trace builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L317) |
| [Trace block tags and pending state](../decisions/H32.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Filter earliest](../cases/h30/filter-earliest.md) | The safe tag resolves to the fixture safe head, block 48. The earliest tag resolves like explicit block 0 on this fixture.<br>[Batched call block default](https://github.com/foundry-rs/foundry/blob/5a99f1a851488fe26863505088e80183ad73cf07/crates/anvil/src/eth/api.rs#L4148) |
| [Single-block hash selection in trace_filter](../decisions/H33.md)<br>Both builds reject every non-null `blockHash` with -32602 through Alloy’s `TraceFilter`, so they pass the error cases and differ wherever block 2’s records are expected. A null `blockHash` beside numeric bounds is rejected too. The reorg scenario does not run on the replica. 1.10.0 · 083e2299 and the nightly 50d75f19 take Alloy 2.6.1, which parses the member, but ignore it: the hashed filter answers the head block’s records. | ⚠️ Differs<br>[Filter blockhash](../cases/h30/filter-blockhash.md) | Take the Alloy `TraceFilter` member and select exactly the hashed canonical block; treat a null member as omitted.<br>[Address filtering](https://github.com/foundry-rs/foundry/blob/5a99f1a851488fe26863505088e80183ad73cf07/crates/anvil/src/eth/backend/mem/mod.rs#L4223) |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 1.10.0 · 083e2299 | [Raw-transaction block argument](../decisions/H12.md) | 6 extension cases. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0. Selector latest: honored: the latest (block 0x30) post-state in the head (block 0x30) environment. Selector block 0x19 by number: honored: the block 0x19 post-state in the block 0x19 environment. Selector block 0x19 by hash: honored: the block 0x19 post-state in the block 0x19 environment. Selector block 0x19 as an EIP-1898 object: honored: the block 0x19 post-state in the block 0x19 environment. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment. | [Raw valid](../cases/initial/raw-valid.md) · [Raw state hash](../cases/raw-selector/raw-state-hash.md) |

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [trace_get selector and return shape](../decisions/H02.md) | [_reference/block/0x30](../cases/a/_reference/block/0x30.md) · [Block 2](../cases/a/block-2.md) |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) |
| [Empty address lists](../decisions/H04.md) | [Filter both null](../cases/a/filter-both-null.md) · [Filter from empty to set](../cases/a/filter-from-empty-to-set.md) |
| [Post-merge reward records](../decisions/H05.md) | [_reference/block/0x30](../cases/a/_reference/block/0x30.md) · [Block 2](../cases/a/block-2.md) |
| [Missing transactions and paths](../decisions/H06.md) | [Missing block block](../cases/a/missing-block-block.md) · [Missing block call](../cases/a/missing-block-call.md) |
| [Replay transactionHash field](../decisions/H07.md) | [Replay 7702 statediff](../cases/initial/replay-7702-stateDiff.md) · [Replay 7702 trace](../cases/initial/replay-7702-trace.md) |
| [Empty output and unrequested components](../decisions/H08.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Failed frame results and error labels](../decisions/H09.md) | [Auth replace](../cases/a/auth-replace.md) · [Auth set revert](../cases/a/auth-set-revert.md) |
| [Creation result field names](../decisions/H10.md) | [Call mixed create](../cases/a/call-mixed-create.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [Empty trace-type selection](../decisions/H11.md) | [Empty types](../cases/a/empty-types.md) · [Call empty types](../cases/initial/call-empty-types.md) |
| [Raw-transaction block argument](../decisions/H12.md) | [Raw valid current nonce](../cases/initial/raw-valid-current-nonce.md) · [Raw state default](../cases/raw-selector/raw-state-default.md) |
| [Signed transaction execution validity](../decisions/H13.md) | [Raw below basefee](../cases/a/raw-below-basefee.md) · [Raw insufficient funds](../cases/a/raw-insufficient-funds.md) |
| [Invalid parameters and rejected calls](../decisions/H14.md) | [Call null mode](../cases/a/call-null-mode.md) · [Call scalar mode](../cases/a/call-scalar-mode.md) |
| [Unsigned simulation fees and block environment](../decisions/H15.md) | [Many storage write read](../cases/a/many-storage-write-read.md) · [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) |
| [Fee accounting and sequential state diffs](../decisions/H16.md) | [Many storage write read](../cases/a/many-storage-write-read.md) · [Many storage write revert read](../cases/a/many-storage-write-revert-read.md) |
| [New-account stateDiff encoding](../decisions/H17.md) | [Prefunded empty](../cases/a/prefunded-empty.md) · [Model empty runtime](../cases/coverage/model-empty-runtime.md) |
| [EIP-7702 code changes in stateDiff](../decisions/H18.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace executing bytecode](../decisions/H19.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Special-action address matching](../decisions/H23.md) | [Filter all](../cases/a/filter-all.md) · [Filter both null](../cases/a/filter-both-null.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Account deletion across Cancun](../decisions/H26.md) | [Call tree statediff](../cases/initial/call-tree-stateDiff.md) · [Call tree statediff priced](../cases/initial/call-tree-stateDiff-priced.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [_reference/block/0x30](../cases/a/_reference/block/0x30.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Block 2](../cases/mined-probes/block-2.md) · [Replay beacon root read](../cases/mined-probes/replay-beacon-root-read.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Block 2](../cases/a/block-2.md) · [Filter all](../cases/a/filter-all.md) |
| [Omitted trace_filter range bounds](../decisions/H30.md) | [Filter no bounds](../cases/h30/filter-no-bounds.md) · [Filter to 2 implicit from](../cases/h30/filter-to-2-implicit-from.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |

</details>

[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
