# H33 trace_filter blockHash selection — 2026-09-29

A focused recapture of the `h30` and `reorg-safe` corpora with H33's `blockHash` cases added. It
reuses the [2026-09-29 refresh](../refresh/README.md)'s [build lock](clients.lock.json) byte for
byte (`--reproduce-lock`, hence the `historical-reproduction` [preflight](preflight.json)), so all
eleven builds are the refresh's images. Each run resends every request of the refresh's run of its
corpus, so [reports.lock.json](../../../reports.lock.json) selects these two runs in place of
`refresh/h30` and `refresh/reorg-safe`. Captured on Fedora from harness commit `3f764566` with
disposable chains: Hive for the native builds and the Geth draft, a
[replica](../../../docs/usage.md#replica-captures) for Anvil (h30 only, since the reorg scenario
needs the Engine API). The manifests keep `source_dirty: true` only because the matrix runner
created this untracked output folder and its log first.

[h30](h30/summary.json) is complete: **495 responses**, and every build passed the setup
controls. [reorg-safe](reorg-safe/summary.json) is incomplete, as in the refresh: **188
responses**, and both Erigon builds stop at the branch switch ("Invalid forkchoice state", open
[erigon#24032](https://github.com/erigontech/erigon/pull/24032)), so their phases are blocked.
Every response to a request the refresh also sent is the same, except one setup query that is
not assessed: after the switch, the Reth nightly now returns null for the dropped transaction's
receipt, as Reth 2.7.0 does, where the refresh captured -32001.

## Cases

On chain a, block 2 (`0xf5de2a84…`, head 0x30), each hash case has a numeric twin
`filter-block-2…` with the same members and `fromBlock = toBlock = 0x2`, and must equal the twin's
records at block 2 from the same build. The records carry `blockNumber` and `blockHash`, so
equality shows that the hash selected block 2. The address lists (block 2's sender, its recipients
including the coinbase) also match records in other blocks, so a wider scan returns more than the
twin. Chain a is proof of stake after genesis, so no block has a genuine reward; the coinbase in
the recipient list matches the synthetic reward that Besu and Nethermind 2.0.0 emit (H05), as their
twins do. [docs/assertion-models.md](../../../docs/assertion-models.md#isolating-the-property-under-test)
describes the `block-hash` probe.

In reorg-safe, `filter-hash-a` and `filter-hash-b` select block 0x2d of branch A (two transactions)
and of branch B (empty) by hash in each phase. A canonical block must equal that phase's
`filter-tail` records at the block; B before its payloads arrive, A after the switch and B after
the restore must be errors. Hive imports the frozen branches, so the hashes are literal and the
adapter needed no change.

## Findings

Cells classify the response: **honored** (equals the numeric twin), **rejected** with its code,
**another block** (records localized elsewhere), `[]` where block 2 has records, or **accepted**
(a result where an error is required). ✅ marks a response that matches the recommendation.
Besu, Erigon and Nethermind name both builds unless a build is given; Erigon's reorg phases are
blocked, and so is a case whose numeric twin returns no result.

| Case | Besu, Erigon, Nethermind | Reth, Anvil, Geth draft |
| --- | --- | --- |
| `filter-blockhash`, `-page`, `-null-bounds` | another block: the head 0x30 (Erigon 3.7.0: from block 1) | rejected -32602 |
| `-address-from`, `-genesis` | another block: the head (Erigon 3.7.0: blocks 0x1 to 0x30) | rejected -32602 |
| `-address-to` | `[]` (Erigon 3.7.0: 18 blocks) | rejected -32602 |
| `-union` | Besu blocked (it rejects mode union, twin included); Erigon, Nethermind 2.2.0: another block; Nethermind 2.0.0: `[]` | rejected -32602 |
| `-page-past-end`, `-empty` | ✅ `[]`, as the twin (cannot discriminate) | rejected -32602 |
| `-null` (`blockHash: null` with bounds) | ✅ honored | Geth draft ✅ honored; Reth, Anvil rejected -32602 |
| `-and-range` | accepted: block 2's records | ✅ rejected -32602 |
| `-unknown` | accepted: the head (Erigon 3.7.0: the whole chain) | ✅ rejected -32602 |
| `-unknown-count-zero` | accepted: `[]` | ✅ rejected -32602 |
| `-malformed-short`, `-malformed-object` | Besu ✅ rejected -32602; Erigon, Nethermind accepted: the head (Erigon 3.7.0: the whole chain) | ✅ rejected -32602 |
| reorg `before/filter-hash-a`, `restored/filter-hash-a` | Besu, Nethermind: another block, the head | Reth, Geth draft: rejected -32602 |
| reorg `after/filter-hash-a` | Besu, Nethermind 2.0.0: accepted, the head's reward; Nethermind 2.2.0: accepted, `[]` | Reth, Geth draft: ✅ rejected -32602 |
| reorg `before/filter-hash-b`, `restored/filter-hash-b` | Besu, Nethermind: accepted, the head | Reth, Geth draft: ✅ rejected -32602 |
| reorg `after/filter-hash-b` | Besu, Nethermind 2.0.0: another block, the head's reward; Nethermind 2.2.0: ✅ `[]` (cannot discriminate) | Reth, Geth draft: rejected -32602 |

No build implements the member. Besu, Erigon and Nethermind silently answer for another block,
and after the reorg Nethermind 2.2.0-preview answers A's hash with B's empty head, the ambiguity
the member exists to remove. Reth, Anvil and the Geth draft reject it as an unknown member, which
passes only the error cases. See [the H33 report](../../../reports/decisions/H33.md).
