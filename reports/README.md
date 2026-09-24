# Trace API: what would change?

The clients already share much of the `trace_*` API. These reports show where adopting the [draft specification](https://github.com/banteg/execution-apis/tree/b979aefe57e4f63af0397b5a068237c04a9d6e3b) would change their behavior. Start with your client, then use the examples and source links to review a proposed change.

Published builds checked at **2026-09-24T12:21:08.909575+00:00**. [Freshness preflight](../evidence/2026-09-24/h17-retest/preflight.json) · [Nine-build lock](../evidence/2026-09-24/h17-retest/clients.lock.json). All corpora use this snapshot; later upstream changes require a new capture.

## Start with your client

| Client | Main review areas |
| --- | --- |
| [Besu](clients/besu.md) | Start with failed-frame reporting, precompile output and inclusion, and range-filter consistency. Individual replay also needs a scope decision. |
| [Erigon](clients/erigon.md) | The tested development build agrees on several cases that differ in the release, including tree lookup, MCOPY and historical system state. Default filter composition still needs attention; signed-transaction validity checks and error codes need alignment with the proposal. Omitted trace_filter bounds currently search history and differ from the proposed latest/latest default. |
| [Geth draft fork](clients/geth.md) | The experimental fork matches most evaluated semantic assertions, including signed-transaction rejection codes, unknown-block errors and call-field handling. Its omitted trace_filter bounds still follow the earlier historical-search draft and differ from the proposed latest/latest default. It is not upstream Geth support. Filtering remains a bounded scan; pruning and other unassessed cases still need coverage. |
| [Nethermind](clients/nethermind.md) | 2.1.0-unstable · 9d6e8b8d fixes empty trace selections, state-only output, empty-code birth/deletion markers and stack-word quantities. 2.0.0 · bec830cd still differs. Complete validation errors, tree lookup and other serialization details remain review areas. |
| [Reth](clients/reth.md) | Reth 2.5.2 · 58a51b3e fixes tree-path lookup, default filter intersection, missing-replay nulls and replay transaction hashes that still differ in 2.6.0 · 73a3a008. Remaining work includes simulation fees, state/VM trace details, error-code alignment and omitted filter bounds. |

## Decisions to review

The largest API choices are [tree-path lookup](decisions/H02.md), [address-filter composition](decisions/H03.md), and [failed-frame results](decisions/H09.md). Other rows concern missing information or inconsistent execution/reporting. All recommendations remain proposals for client review.

| Question | Status | Proposed behavior |
| --- | --- | --- |
| [How does trace_get select a frame?](decisions/H02.md) | ⚪ Under review | Follow one tree path; return one object or null. An empty path selects the root. |
| [How do address filters combine?](decisions/H03.md) | 🤝 Converged | OR within each list, AND between sender and recipient lists. |
| [Where does an unbounded filter start?](decisions/H30.md) | ⚪ Under review | Default both omitted bounds to latest; historical searches specify fromBlock. |
| [What block does trace_callMany use by default?](decisions/H31.md) | ⚪ Under review | Accept an omitted block and use latest, matching trace_call. |
| [Which tags and pending state can trace methods use?](decisions/H32.md) | ⚪ Under review | Resolve mined-block tags; agree pending state and localization per method. |
| [What survives a failed call?](decisions/H09.md) | ⚪ Under review | Keep the error on that frame and preserve revert bytes and measured gas when available. |
| [Which precompile frames are visible?](decisions/H29.md) | ⚪ Under review | Keep root frames and nested frames with nonzero value; omit zero-value nested frames. |
| [Signed transaction execution validity](decisions/H13.md) | 🤝 Converged | Validate against the selected state, including nonce, funds and gas. Keep pool policies separate; propose -32003 for validation rejection. |

[Status definitions](../decisions/README.md#status-key). Policy direction is distinct from verified implementation on the captured builds.

[All decisions](../decisions/README.md) · [Method availability](decisions/H01.md)

[Client fixes](../docs/client-fixes.md) · [Client source guide](sources.md) · [Run a case](../docs/usage.md) · [Builds, coverage and raw results](technical.md) · [Standardization discussion](https://github.com/ethereum/execution-apis/issues/890)
