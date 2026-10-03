# Consistency laws

[Back to the maintainer overview](README.md) · [Spec decision tables](spec-tables.md)

Every trace method projects one execution, so some pairs of responses must agree whatever the draft decides. A law pairs two captured requests that denote the same execution or the same records and compares what one build returned for both: a request selected with different trace types, a transaction through trace_transaction and trace_block, a stored trace and its replay, a bundle item and the same call, a filter and the blocks it covers. A law needs no expected value and no other client, and never asks which frames exist, how a record is encoded or which errors a request earns. Selector and transaction-identity checks in L05 and L08 additionally require the pinned trace profile. An error on either side leaves the pair unevaluated.

Violations are reported here and are not decision verdicts: most repeat a difference a decision already measures, so they do not change the progress counts. A cause names the decision that already measures the difference; “Found by this law” marks one no decision assertion checks. Laws run on the eligible responses of every run in the current matrix; [laws.json](laws.json) keeps every violation.

## Laws

| Law | Statement | Pairs checked | Builds with violations |
| --- | --- | --- | --- |
| **L01** Tree shape | Every frame list is a preorder tree: one root, unique dense paths, subtraces equal to the number of children, and no frame using more gas than it was given. | 8293 | Besu 26.10-develop · 711f8142, Besu 26.9.0 · ee9c64c8 |
| **L02** Changed values | A stateDiff `*` entry changes its value: `from` differs from `to`. | 14976 | — |
| **L03** Root output | A successful root call frame reports the envelope output. | 1553 | Besu 26.10-develop · 711f8142, Besu 26.9.0 · ee9c64c8 |
| **L04** Selection is a projection | Requests that differ only in their trace types return the same output and the same value for every component both select. | 28349 | Nethermind 2.1.0 · b3e7e84c |
| **L05** trace_get selects from trace_transaction | A record trace_get returns is one of the trace_transaction records, unchanged; under the trace profile it is the requested traceAddress, or null for an absent path. | 90 | Anvil 1.8.4-nightly · 328811cb, Anvil 1.8.4 · 50af4efe, Nethermind 2.1.0 · b3e7e84c |
| **L06** trace_transaction is a slice of trace_block | trace_transaction(tx) equals the trace_block records carrying its hash, in order. | 136 | — |
| **L07** Stored and replayed frames agree | The frames of trace_transaction and trace_block equal the replayed trace of the same transaction, apart from localization fields. | 526 | Anvil 1.8.4-nightly · 328811cb, Anvil 1.8.4 · 50af4efe, Nethermind 2.2.0-preview · 3370d566, Nethermind 2.1.0 · b3e7e84c |
| **L08** Single and block replay agree | trace_replayTransaction(tx) equals the block replay envelope of that transaction for every shared selected component; under the trace profile that envelope must exist at its transaction index and carry its hash. | 185 | Nethermind 2.1.0 · b3e7e84c |
| **L09** A bundle item is a call | trace_callMany items equal the same items replayed as a shorter bundle, and a first item equals trace_call on the same block. | 4519 | Erigon 3.7.1 · 8c1e3893 |
| **L10** Filters select block records | trace_filter over an explicit range returns block records, unchanged and in block order; without addresses or paging it returns all of them. | 721 | Besu 26.10-develop · 711f8142, Besu 26.9.0 · ee9c64c8, Erigon 3.7.1 · 8c1e3893 |
| **L11** Paging slices the filter | trace_filter with after and count returns that slice of the same filter without them. | 115 | — |
| **L12** Equivalent block and address spellings | The same request, or one that differs only in address letter case or in naming one block by number, hash or head tag, returns the same result. | 14 | — |

## Violations

### L01 Tree shape

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Besu 26.10-develop · 711f8142 | 1 | Found by this law. At the call depth limit (`probes-forks/depth-limit`) the successful CREATE at depth 1 reports gasUsed 2^64 − 25357 and the phantom CREATE at depth 1025 reports 2^64 − 22239: negative gas wrapped to unsigned. The H29 depth probe records the phantom frame but no assertion checks its gas. | [depth-limit](cases/probes-forks/depth-limit.md): `[0] (create) reports gasUsed 18446744073709526259 of 1977046 gas; [1, … 1025 deep] (create) reports gasUsed 18446744073709529377 of 1401257 gas` |
| Besu 26.9.0 · ee9c64c8 | 1 | The same wrapped gasUsed as the development build. | [depth-limit](cases/probes-forks/depth-limit.md): `[0] (create) reports gasUsed 18446744073709526259 of 1977046 gas; [1, … 1025 deep] (create) reports gasUsed 18446744073709529377 of 1401257 gas` |

### L03 Root output

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Besu 26.10-develop · 711f8142 | 3 | H22: a root call to a precompile reports empty frame output while the envelope carries the precompile’s return bytes. | [call-identity](cases/initial/call-identity.md): `root output 0x vs envelope "0x11223344"` · [root-failed](cases/precompiles/root-failed.md): `root output 0x vs envelope "0x6572726f72"` |
| Besu 26.9.0 · ee9c64c8 | 3 | H22, as in the development build. | [call-identity](cases/initial/call-identity.md): `root output 0x vs envelope "0x11223344"` · [root-failed](cases/precompiles/root-failed.md): `root output 0x vs envelope "0x6572726f72"` |

### L04 Selection is a projection

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Nethermind 2.1.0 · b3e7e84c | 30 | H08: output is missing when stateDiff alone is selected. H20: vmTrace `store` appears only when stateDiff is also selected. The development build has neither. | [legacy-refund-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/trace-vmTrace.md) vs [legacy-refund-then-observe/many/stateDiff-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/stateDiff-vmTrace.md): `[0].vmTrace.ops[2].ex.store: null vs {"key": "0x0000000000000000000000000000000000000000000000000000000000000000", "v` · [legacy-refund/call/trace-vmTrace](cases/fee-policy/legacy-refund/call/trace-vmTrace.md) vs [legacy-refund/call/stateDiff-vmTrace](cases/fee-policy/legacy-refund/call/stateDiff-vmTrace.md): `.vmTrace.ops[2].ex.store: null vs {"key": "0x0000000000000000000000000000000000000000000000000000000000000000", "v` |

### L05 trace_get selects from trace_transaction

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Anvil 1.8.4-nightly · 328811cb | 5 | Not yet triaged. | [get-nested-parent](cases/a/get-nested-parent.md) vs [transaction-tree](cases/a/transaction-tree.md): `requested traceAddress [6]: .action.callType: differs at character 4: …call vs …callcode` · [get-one](cases/initial/get-one.md) vs [transaction-tree](cases/initial/transaction-tree.md): `requested traceAddress [1]: .action.gas: differs at character 2: …0xea60 vs …0xf35c` |
| Anvil 1.8.4 · 50af4efe | 5 | Not yet triaged. | [get-nested-parent](cases/a/get-nested-parent.md) vs [transaction-tree](cases/a/transaction-tree.md): `requested traceAddress [6]: .action.callType: differs at character 4: …call vs …callcode` · [get-one](cases/initial/get-one.md) vs [transaction-tree](cases/initial/transaction-tree.md): `requested traceAddress [1]: .action.gas: differs at character 2: …0xea60 vs …0xf35c` |
| Nethermind 2.1.0 · b3e7e84c | 8 | Not yet triaged. | [get-nested-parent](cases/a/get-nested-parent.md) vs [transaction-tree](cases/a/transaction-tree.md): `requested traceAddress [6]: value: {"action": {"creationMethod": "create", "from": "0x9dcd17433742f4c0ca53122ab541d vs [{"action": {"creationMethod": "create", ` · [get-nested-positive](cases/a/get-nested-positive.md) vs [transaction-tree](cases/a/transaction-tree.md): `requested traceAddress [6, 0]: value: {"action": {"address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893", "balance":  vs [{"action": {"creationMethod": "create` |

### L07 Stored and replayed frames agree

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Anvil 1.8.4-nightly · 328811cb | 2 | H29: stored trace_transaction and trace_block records keep the zero-value identity precompile frame at `[6]`, which the replay and trace_call omit. | [block-tree](cases/initial/block-tree.md) vs [replay-tree-trace](cases/initial/replay-tree-trace.md): `list has 10 vs 9 entries` |
| Anvil 1.8.4 · 50af4efe | 2 | H29, as in the nightly. | [block-tree](cases/initial/block-tree.md) vs [replay-tree-trace](cases/initial/replay-tree-trace.md): `list has 10 vs 9 entries` |
| Nethermind 2.2.0-preview · 3370d566 | 10 | Found by this law. A suicide record has no `result` member in trace_transaction and trace_block, but `"result": null` in the replayed trace of the same transaction. Serialization only. | [block-36](cases/forks/block-36.md) vs [replay-36](cases/forks/replay-36.md): `[8].result present on one side only` · [block-4](cases/mined-probes/block-4.md) vs [replay-create-destroy-absent](cases/mined-probes/replay-create-destroy-absent.md): `[2].result present on one side only` |
| Nethermind 2.1.0 · b3e7e84c | 10 | The same suicide serialization as the development build. | [block-36](cases/forks/block-36.md) vs [replay-36](cases/forks/replay-36.md): `[8].result present on one side only` · [block-4](cases/mined-probes/block-4.md) vs [replay-create-destroy-absent](cases/mined-probes/replay-create-destroy-absent.md): `[2].result present on one side only` |

### L08 Single and block replay agree

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Nethermind 2.1.0 · b3e7e84c | 1 | H08 output and H20 `store`, as under L04. | [replay-tree-vmTrace](cases/initial/replay-tree-vmTrace.md) vs [replay-block-tree](cases/initial/replay-block-tree.md): `.vmTrace.ops[49].sub.ops[11].ex.store: null vs {"key": "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c", "v` |

### L09 A bundle item is a call

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Erigon 3.7.1 · 8c1e3893 | 185 | H15: trace_call runs with GASLIMIT 2^256 − 1 while the same item in trace_callMany sees the block gas limit, fixed by erigon#24343 in the development build. `beacon-many-55` also reads block 56’s beacon root from trace_callMany at block 55 (H28), fixed by erigon#24293 in the development build. | [defaults-cap-only-positive/call/none](cases/fee-policy/defaults-cap-only-positive/call/none.md) vs [defaults-cap-only-positive/many/none](cases/fee-policy/defaults-cap-only-positive/many/none.md): `.output: differs at character 258: …00000014ffffffffffffffffffffffffffffffffffffffff vs …000000140000000000000000000000000000000000000000` |

### L10 Filters select block records

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Besu 26.10-develop · 711f8142 | 4 | H27: range filters across a fork boundary (blocks 35–36, 55–56 and 59–60, and 2–5 across the Homestead transition at block 4) differ from the same blocks’ traces. | [filter-across-36](cases/forks/filter-across-36.md) vs [block-35](cases/forks/block-35.md) (1 more): `list has 8 vs 16 entries` · [filter-across-56](cases/forks/filter-across-56.md) vs [block-55](cases/forks/block-55.md) (1 more): `[3].action.gas present on one side only` |
| Besu 26.9.0 · ee9c64c8 | 4 | H27, as in the development build. | [filter-across-36](cases/forks/filter-across-36.md) vs [block-35](cases/forks/block-35.md) (1 more): `list has 8 vs 16 entries` · [filter-across-56](cases/forks/filter-across-56.md) vs [block-55](cases/forks/block-55.md) (1 more): `[3].action.gas present on one side only` |
| Erigon 3.7.1 · 8c1e3893 | 1 | H05: trace_filter over the genesis block returns a reward that trace_block(0) does not, fixed by erigon#24295 in the development build. | [genesis-filter](cases/probes-forks/genesis-filter.md) vs [genesis-block](cases/probes-forks/genesis-block.md): `list has 1 vs 0 entries` |
