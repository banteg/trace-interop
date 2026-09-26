# Consistency laws

[Back to the maintainer overview](README.md) · [Spec decision tables](spec-tables.md)

Every trace method projects one execution, so some pairs of responses must agree whatever the draft decides. A law pairs two captured requests that denote the same execution or the same records and compares what one build returned for both: a request selected with different trace types, a transaction through trace_transaction and trace_block, a stored trace and its replay, a bundle item and the same call, a filter and the blocks it covers. A law needs no expected value and no other client, and never asks which frames exist, how a record is encoded or which errors a request earns. An error on either side leaves the pair unevaluated.

Violations are reported here and are not decision verdicts: most repeat a difference a decision already measures, so they do not change the progress counts. A cause names the decision that already measures the difference; “Found by this law” marks one no decision assertion checks. Laws run on the eligible responses of every run in the current matrix; [laws.json](laws.json) keeps every violation.

## Laws

| Law | Statement | Pairs checked | Builds with violations |
| --- | --- | --- | --- |
| **L01** Tree shape | Every frame list is a preorder tree: one root, unique dense paths, subtraces equal to the number of children, and no frame using more gas than it was given. | 7730 | Besu 26.9-develop · accdae00, Besu 26.9.0 · ee9c64c8 |
| **L02** Changed values | A stateDiff `*` entry changes its value: `from` differs from `to`. | 14777 | — |
| **L03** Root output | A successful root call frame reports the envelope output. | 1363 | Besu 26.9-develop · accdae00, Besu 26.9.0 · ee9c64c8 |
| **L04** Selection is a projection | Requests that differ only in their trace types return the same output and the same value for every component both select. | 26901 | Nethermind 2.0.0 · bec830cd |
| **L05** trace_get selects from trace_transaction | A record trace_get returns is one of the trace_transaction records, unchanged. | 52 | — |
| **L06** trace_transaction is a slice of trace_block | trace_transaction(tx) equals the trace_block records carrying its hash, in order. | 136 | — |
| **L07** Stored and replayed frames agree | The frames of trace_transaction and trace_block equal the replayed trace of the same transaction, apart from localization fields. | 526 | Anvil 1.8.4-nightly · 5a99f1a8, Anvil 1.8.3 · cae51ad4, Nethermind 2.1.0-preview · fca93966, Nethermind 2.0.0 · bec830cd |
| **L08** Single and block replay agree | trace_replayTransaction(tx) equals the block replay envelope of that transaction for every selected component. | 167 | Nethermind 2.0.0 · bec830cd, Reth 2.6.0 · 73a3a008 |
| **L09** A bundle item is a call | trace_callMany items equal the same items replayed as a shorter bundle, and a first item equals trace_call on the same block. | 4263 | Anvil 1.8.4-nightly · 5a99f1a8, Anvil 1.8.3 · cae51ad4, Erigon 3.8.0-dev · 7853b922, Erigon 3.7.0 · bdc78cc4 |
| **L10** Filters select block records | trace_filter over an explicit range returns block records, unchanged and in block order; without addresses or paging it returns all of them. | 637 | Besu 26.9-develop · accdae00, Besu 26.9.0 · ee9c64c8, Erigon 3.7.0 · bdc78cc4 |
| **L11** Paging slices the filter | trace_filter with after and count returns that slice of the same filter without them. | 110 | — |
| **L12** Equivalent block and address spellings | The same request, or one that differs only in address letter case or in naming one block by number, hash or head tag, returns the same result. | 11 | — |

## Violations

### L01 Tree shape

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Besu 26.9-develop · accdae00 | 1 | Found by this law. At the call depth limit (`probes-forks/depth-limit`) the successful CREATE at depth 1 reports gasUsed 2^64 − 25357 and the phantom CREATE at depth 1025 reports 2^64 − 22239: negative gas wrapped to unsigned. The H29 depth probe records the phantom frame but no assertion checks its gas. | [depth-limit](cases/probes-forks/depth-limit.md): `[0] (create) reports gasUsed 18446744073709526259 of 1977046 gas; [1, … 1025 deep] (create) reports gasUsed 18446744073709529377 of 1401257 gas` |
| Besu 26.9.0 · ee9c64c8 | 1 | The same wrapped gasUsed as the development build. | [depth-limit](cases/probes-forks/depth-limit.md): `[0] (create) reports gasUsed 18446744073709526259 of 1977046 gas; [1, … 1025 deep] (create) reports gasUsed 18446744073709529377 of 1401257 gas` |

### L03 Root output

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Besu 26.9-develop · accdae00 | 3 | H22: a root call to a precompile reports empty frame output while the envelope carries the precompile’s return bytes. | [call-identity](cases/initial/call-identity.md): `root output 0x vs envelope "0x11223344"` · [root-failed](cases/precompiles/root-failed.md): `root output 0x vs envelope "0x6572726f72"` |
| Besu 26.9.0 · ee9c64c8 | 3 | H22, as in the development build. | [call-identity](cases/initial/call-identity.md): `root output 0x vs envelope "0x11223344"` · [root-failed](cases/precompiles/root-failed.md): `root output 0x vs envelope "0x6572726f72"` |

### L04 Selection is a projection

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Nethermind 2.0.0 · bec830cd | 584 | H08: output is missing when stateDiff alone is selected. H20: vmTrace `store` appears only when stateDiff is also selected. The development build has neither. | [call-return42](cases/a/call-return42.md) vs [state-only-nonempty-output](cases/a/state-only-nonempty-output.md): `.output: "0x000000000000000000000000000000000000000000000000000000000000002a" vs null` · [defaults-cap-only-positive/many/stateDiff](cases/fee-policy/defaults-cap-only-positive/many/stateDiff.md) vs [defaults-cap-only-positive/many/stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/many/stateDiff-vmTrace.md): `[0].output: null vs "0x000000000000000000000000000000000000000000000000000000002da282a80000000000000` |

### L07 Stored and replayed frames agree

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Anvil 1.8.4-nightly · 5a99f1a8 | 2 | H29: stored trace_transaction and trace_block records keep the zero-value identity precompile frame at `[6]`, which the replay and trace_call omit. | [block-tree](cases/initial/block-tree.md) vs [replay-tree-trace](cases/initial/replay-tree-trace.md): `list has 10 vs 9 entries` |
| Anvil 1.8.3 · cae51ad4 | 2 | H29, as in the nightly. | [block-tree](cases/initial/block-tree.md) vs [replay-tree-trace](cases/initial/replay-tree-trace.md): `list has 10 vs 9 entries` |
| Nethermind 2.1.0-preview · fca93966 | 10 | Found by this law. A suicide record has no `result` member in trace_transaction and trace_block, but `"result": null` in the replayed trace of the same transaction. Serialization only. | [block-36](cases/forks/block-36.md) vs [replay-36](cases/forks/replay-36.md): `[8].result present on one side only` · [block-4](cases/mined-probes/block-4.md) vs [replay-create-destroy-absent](cases/mined-probes/replay-create-destroy-absent.md): `[2].result present on one side only` |
| Nethermind 2.0.0 · bec830cd | 10 | The same suicide serialization as the development build. | [block-36](cases/forks/block-36.md) vs [replay-36](cases/forks/replay-36.md): `[8].result present on one side only` · [block-4](cases/mined-probes/block-4.md) vs [replay-create-destroy-absent](cases/mined-probes/replay-create-destroy-absent.md): `[2].result present on one side only` |

### L08 Single and block replay agree

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Nethermind 2.0.0 · bec830cd | 4 | H08 output and H20 `store`, as under L04. | [replay-7702-stateDiff](cases/initial/replay-7702-stateDiff.md) vs [replay-block-tree](cases/initial/replay-block-tree.md): `.output: null vs "0x"` · [replay-tree-vmTrace](cases/initial/replay-tree-vmTrace.md) vs [replay-block-tree](cases/initial/replay-block-tree.md): `.vmTrace.ops[49].sub.ops[11].ex.store: null vs {"key": "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c", "v` |
| Reth 2.6.0 · 73a3a008 | 2 | H19: the single replay reports the executing bytecode as vmTrace `code` while the block replay reports `0x`; the development build agrees. | [replay-revert-vmTrace](cases/initial/replay-revert-vmTrace.md) vs [replay-block-tree](cases/initial/replay-block-tree.md): `.vmTrace.code: differs at character 2: …0x6000356142ff54501515603b577f4e487b710000 vs …0x` |

### L09 A bundle item is a call

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Anvil 1.8.4-nightly · 5a99f1a8 | 45 | H11: an empty trace-type list returns call frames from trace_call but not from the same item in trace_callMany. | [defaults-cap-only-positive/call/none](cases/fee-policy/defaults-cap-only-positive/call/none.md) vs [defaults-cap-only-positive/many/none](cases/fee-policy/defaults-cap-only-positive/many/none.md): `.trace has 1 vs 0 entries` |
| Anvil 1.8.3 · cae51ad4 | 45 | H11, as in the nightly. | [defaults-cap-only-positive/call/none](cases/fee-policy/defaults-cap-only-positive/call/none.md) vs [defaults-cap-only-positive/many/none](cases/fee-policy/defaults-cap-only-positive/many/none.md): `.trace has 1 vs 0 entries` |
| Erigon 3.8.0-dev · 7853b922 | 184 | H15: trace_call runs with GASLIMIT 2^256 − 1 while the same item in trace_callMany sees the block gas limit. | [defaults-cap-only-positive/call/none](cases/fee-policy/defaults-cap-only-positive/call/none.md) vs [defaults-cap-only-positive/many/none](cases/fee-policy/defaults-cap-only-positive/many/none.md): `.output: differs at character 258: …00000014ffffffffffffffffffffffffffffffffffffffff vs …000000140000000000000000000000000000000000000000` |
| Erigon 3.7.0 · bdc78cc4 | 185 | H15 GASLIMIT, as in the development build. `beacon-many-55` also reads block 56’s beacon root from trace_callMany at block 55 (H28), fixed by erigon#24293 in the development build. | [defaults-cap-only-positive/call/none](cases/fee-policy/defaults-cap-only-positive/call/none.md) vs [defaults-cap-only-positive/many/none](cases/fee-policy/defaults-cap-only-positive/many/none.md): `.output: differs at character 258: …00000014ffffffffffffffffffffffffffffffffffffffff vs …000000140000000000000000000000000000000000000000` |

### L10 Filters select block records

| Build | Violations | Cause | Examples |
| --- | --- | --- | --- |
| Besu 26.9-develop · accdae00 | 4 | H27: range filters across a fork boundary (blocks 35–36, 55–56 and 59–60, and 2–5 across the Homestead transition at block 4) differ from the same blocks’ traces. | [filter-across-36](cases/forks/filter-across-36.md) vs [block-35](cases/forks/block-35.md) (1 more): `list has 8 vs 16 entries` · [filter-across-56](cases/forks/filter-across-56.md) vs [block-55](cases/forks/block-55.md) (1 more): `[3].action.gas present on one side only` |
| Besu 26.9.0 · ee9c64c8 | 4 | H27, as in the development build. | [filter-across-36](cases/forks/filter-across-36.md) vs [block-35](cases/forks/block-35.md) (1 more): `list has 8 vs 16 entries` · [filter-across-56](cases/forks/filter-across-56.md) vs [block-55](cases/forks/block-55.md) (1 more): `[3].action.gas present on one side only` |
| Erigon 3.7.0 · bdc78cc4 | 1 | H05: trace_filter over the genesis block returns a reward that trace_block(0) does not, fixed by erigon#24295 in the development build. | [genesis-filter](cases/probes-forks/genesis-filter.md) vs [genesis-block](cases/probes-forks/genesis-block.md): `list has 1 vs 0 entries` |
