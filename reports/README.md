# Trace API: what would change?

The clients already share much of the `trace_*` API. These reports show where adopting the [draft specification](https://github.com/banteg/execution-apis/tree/e38fc96c9942f201b683e231f69432729d2737df) would change their behavior. Start with your client, then use the examples and source links to review a proposed change.

## Start with your client

| Client | Main review areas |
| --- | --- |
| [Besu](clients/besu.md) | Start with failed-frame reporting, precompile output and inclusion, and range-filter consistency. Individual replay also needs a scope decision. |
| [Erigon](clients/erigon.md) | The tested development build agrees on several cases that differ in the release, including tree lookup, MCOPY and historical system state. Default filter composition still needs attention; signed nonce-mismatch simulation matches the revised proposal. |
| [Geth draft fork](clients/geth.md) | The experimental fork implements an earlier draft; nullable filters, unknown call fields and the proposed unknown-block code need updates. It is not upstream Geth support. Filtering remains a bounded scan and pruning coverage is incomplete. Signed nonce-mismatch rejection differs from the revised simulation proposal. |
| [Nethermind](clients/nethermind.md) | Prioritize complete error responses, retained execution output, and empty trace selections. Tree lookup and stack-word encoding also need API agreement. |
| [Reth](clients/reth.md) | The main changes are tree-path lookup, filter composition, replay metadata, and missing code changes in state/VM traces. Signed nonce-mismatch rejection differs from the revised simulation proposal. |

## Decisions to review

The largest API choices are [tree-path lookup](decisions/H02.md), [address-filter composition](decisions/H03.md), and [failed-frame results](decisions/H09.md). Other rows concern missing information or inconsistent execution/reporting. All recommendations remain proposals for client review.

| Question | Proposed behavior |
| --- | --- |
| [How does trace_get select a frame?](decisions/H02.md) | Follow one tree path; return one object or null. An empty path selects the root. |
| [How do address filters combine?](decisions/H03.md) | OR within each list, AND between sender and recipient lists. |
| [What survives a failed call?](decisions/H09.md) | Keep the error on that frame and preserve revert bytes and measured gas when available. |
| [Which precompile frames are visible?](decisions/H29.md) | Keep root frames and nested frames with nonzero value; omit zero-value nested frames. |
| [Nonce-mismatch policy for signed simulation](decisions/H13.md) | Proposed: permit simulation despite a nonce mismatch. Acceptance does not demonstrate nonce rewriting; client agreement is pending. |

[All 29 decisions](../decisions/README.md) · [Method availability](decisions/H01.md)

[Client fixes](../docs/client-fixes.md) · [Client source guide](sources.md) · [Run a case](../docs/usage.md) · [Builds, coverage and raw results](technical.md) · [Standardization discussion](https://github.com/ethereum/execution-apis/issues/890)
