# Anvil: changes to review

Foundry’s development node, captured by replaying each chain instead of through Hive. Foundry 1.8.5 · 51a52c59 ships ten trace-interop fixes (#17301–#17304, #17306, #17307, #17309–#17312): tree-path trace_get, missing blocks and replays, replay transaction hashes, mined traces without nested precompile frames, EIP-3607 rejection for signed raw transactions, conflicting call fields, pending in block trace methods, and the fee-free, cap-only and omitted-gas call environment. With revm-inspectors 0.44.1 (#17226) it also carries the reverted-CREATE results, failure labels and vmTrace fixes. 1.8.5 still accepts integer trace_get indices and executes calls priced below the base fee, and cannot set a parent beacon root, so the mined-probes chain is not replayed on it. The nightly 32624734 adds #17305, #17308 and #17419 (by figtracer): it replays mined-probes and agrees on 28 decisions. Its remaining differences are null address lists in trace_filter (H04), the self-destruct-to-self payload (H23, H26; open bluealloy/revm#3833) and the filter tags and blockHash that Alloy’s `TraceFilter` lacks (H32, H33).

[All clients](../README.md) · [Client fixes](../../docs/client-fixes.md) · [Source guide](../sources.md)

| Tested version | Commit | Commit date (UTC) | Tested (UTC) |
| --- | --- | --- | --- |
| `1.8.6-nightly` | [`32624734`](https://github.com/foundry-rs/foundry/commit/32624734aaf99e89a5046a3017a374a911000da8) | 2026-10-10 | [2026-10-11](../../evidence/2026-10-11/eval/initial/manifest.json) |

Code links use the tested development sources (or the Geth fork). These are proposed changes for the tested builds. “Checked cases agree” refers to the linked examples, not every behavior of a method. [Test status key](../technical.md#test-status-key).

## Changes to discuss

| Behavior | 1.8.6-nightly · 32624734 | Proposed change |
| --- | --- | --- |
| [Empty address lists](../decisions/H04.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Filter both null](../cases/a/filter-both-null.md) | Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.<br>[Address filtering](https://github.com/foundry-rs/foundry/blob/5a99f1a851488fe26863505088e80183ad73cf07/crates/anvil/src/eth/backend/mem/mod.rs#L4223) |
| [Special-action address matching](../decisions/H23.md)<br>The nightly 32624734 replays mined-probes through #17305. With the zeroed self-destruct-to-self payload (H26), trace_filter misses that suicide record by its executing account and by its beneficiary. | ⚠️ Differs<br>3 blocked cases: The H04 list semantics differ, so the special-action records cannot be judged separately.<br>[Filter self destruct from](../cases/mined-probes/filter-self-destruct-from.md) | None beyond bluealloy/revm#3833 (H26). Checked requirements: A SELFDESTRUCT matches fromAddress by its executing account. A SELFDESTRUCT to self also matches toAddress as its own beneficiary.<br>[Address filtering](https://github.com/foundry-rs/foundry/blob/5a99f1a851488fe26863505088e80183ad73cf07/crates/anvil/src/eth/backend/mem/mod.rs#L4223) |
| [Account deletion across Cancun](../decisions/H26.md)<br>With revm-inspectors 0.44.0 the nightlies reported the calltree’s child, created and self-destructed in one transaction and absent at both endpoints, as a deleted account. 1.8.4 and the nightly 328811cb include #17106 and omit it. The nightly 32624734 replays mined-probes through #17305: a post-Cancun SELFDESTRUCT to self yields a suicide record with a zero address, balance and refundAddress in trace_transaction, trace_block and both replays, because revm passes no payload to the tracer for it. | ⚠️ Differs<br>[Block 4](../cases/mined-probes/block-4.md) | Merge bluealloy/revm#3833, which passes the executing account, beneficiary and balance to the tracer, and take it through revm-inspectors. Checked requirements: The suicide frame records the contract’s whole balance transferred to itself.<br>[State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) |
| [Trace block tags and pending state](../decisions/H32.md)<br>The linked case differs from the proposed behavior. | ⚠️ Differs<br>[Filter earliest](../cases/h30/filter-earliest.md) | The safe tag resolves to the fixture safe head, block 48. The earliest tag resolves like explicit block 0 on this fixture.<br>[Batched call block default](https://github.com/foundry-rs/foundry/blob/5a99f1a851488fe26863505088e80183ad73cf07/crates/anvil/src/eth/api.rs#L4148) |
| [Single-block hash selection in trace_filter](../decisions/H33.md)<br>Both builds reject every non-null `blockHash` with -32602 through Alloy’s `TraceFilter`, so they pass the error cases and differ wherever block 2’s records are expected. A null `blockHash` beside numeric bounds is rejected too. The reorg scenario does not run on the replica. | ⚠️ Differs<br>[Filter blockhash](../cases/h30/filter-blockhash.md) | Take the Alloy `TraceFilter` member and select exactly the hashed canonical block; treat a null member as omitted.<br>[Address filtering](https://github.com/foundry-rs/foundry/blob/5a99f1a851488fe26863505088e80183ad73cf07/crates/anvil/src/eth/backend/mem/mod.rs#L4223) |

## Open policy observations

These results record behavior whose policy is unresolved. Passing a checked part of a topic does not settle the remaining choices.

| Build | Decision | Observed | Example |
| --- | --- | --- | --- |
| 1.8.6-nightly · 32624734 | [Raw-transaction block argument](../decisions/H12.md) | 6 extension cases. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0. Selector latest: honored: the latest (block 0x30) post-state in the head (block 0x30) environment. Selector block 0x19 by number: honored: the block 0x19 post-state in the block 0x19 environment. Selector block 0x19 by hash: honored: the block 0x19 post-state in the block 0x19 environment. Selector block 0x19 as an EIP-1898 object: honored: the block 0x19 post-state in the block 0x19 environment. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment. | [Raw valid](../cases/initial/raw-valid.md) · [Raw state hash](../cases/raw-selector/raw-state-hash.md) |

<details><summary>✅ Behaviors with no difference in the checked cases</summary>

| Behavior | Examples |
| --- | --- |
| [trace_get selector and return shape](../decisions/H02.md) | [_reference/block/0x30](../cases/a/_reference/block/0x30.md) · [Block 2](../cases/a/block-2.md) |
| [Filter composition and mode](../decisions/H03.md) | [Filter all](../cases/a/filter-all.md) · [Filter both unknown mode](../cases/a/filter-both-unknown-mode.md) |
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
| [vmTrace step timing and deltas](../decisions/H20.md) | [Call gas7400](../cases/a/call-gas7400.md) · [Call mcopy](../cases/a/call-mcopy.md) |
| [vmTrace numeric and optional metadata encoding](../decisions/H21.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Precompile return bytes](../decisions/H22.md) | [Call identity](../cases/initial/call-identity.md) |
| [Sibling failure isolation](../decisions/H24.md) | [Call siblings revert ok](../cases/a/call-siblings-revert-ok.md) · [Nested call outer0 value1 failed](../cases/precompile-values/nested-call-outer0-value1-failed.md) |
| [Well-formed errors for rejected raw transactions](../decisions/H25.md) | [Auth clear](../cases/a/auth-clear.md) · [Auth replace](../cases/a/auth-replace.md) |
| [Filter execution across fork boundaries](../decisions/H27.md) | [Filter two blocks](../cases/a/filter-two-blocks.md) · [_reference/block/0x30](../cases/a/_reference/block/0x30.md) |
| [Historical state at system-operation boundaries](../decisions/H28.md) | [Block 2](../cases/mined-probes/block-2.md) · [Replay beacon root read](../cases/mined-probes/replay-beacon-root-read.md) |
| [Precompile call-frame inclusion](../decisions/H29.md) | [Block 2](../cases/a/block-2.md) · [Filter all](../cases/a/filter-all.md) |
| [Omitted trace_filter range bounds](../decisions/H30.md) | [Filter no bounds](../cases/h30/filter-no-bounds.md) · [Filter to 2 implicit from](../cases/h30/filter-to-2-implicit-from.md) |
| [Omitted trace_callMany block](../decisions/H31.md) | [Call number default](../cases/h30/call-number-default.md) · [Call number latest](../cases/h30/call-number-latest.md) |

</details>

[Method availability](../decisions/H01.md) · [All decisions](../../decisions/README.md)

For setup gaps, exact run inventories and reproduction, see the [technical appendix](../technical.md).
