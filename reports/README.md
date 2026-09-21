# Trace API draft impact

Proposals for review, not an adopted standard or a client ranking. Results apply to the pinned builds and selected cases. Schema validity, partial semantic assertions and full conformance are different claims.

Draft: [99a312e9c417](https://github.com/banteg/execution-apis/commit/99a312e9c41724f180673a636c6e200f213beb7b).

`go-ethereum_trace` is the experimental [draft implementation](https://github.com/banteg/go-ethereum/tree/feat/trace), not upstream Geth support or an independent client vote.

## Method observations

R = at least one result; E = RPC error observed; U = method not found. Mixed results remain visible.

| Method | besu_development | besu_release | erigon_development | erigon_release | go-ethereum_trace | nethermind_development | nethermind_release | reth_development | reth_release |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `trace_block` | R | R | R, E | R, E | R, E | R, E | R, E | R, E | R, E |
| `trace_call` | R, E | R, E | R, E | R, E | R, E | R, E | R, E | R, E | R, E |
| `trace_callMany` | R | R | R, E | R, E | R | R | R | R | R |
| `trace_filter` | R, E | R, E | R, E | R, E | R, E | R, E | R, E | R, E | R, E |
| `trace_get` | R, E | R, E | R, E | R, E | R, E | R, E | R, E | R, E | R, E |
| `trace_rawTransaction` | R, E | R, E | R, E | R, E | R, E | R, E, malformed JSON | R, E, malformed JSON | R, E | R, E |
| `trace_replayBlockTransactions` | R | R | R | R | R | R | R | R | R |
| `trace_replayTransaction` | U | U | R | R | R | R, E | R, E | R, E | R, E |
| `trace_transaction` | R | R | R | R | R | R, E | R, E | R, E | R, E |

## Client impact

- [besu_development](clients/besu_development.md)
- [besu_release](clients/besu_release.md)
- [erigon_development](clients/erigon_development.md)
- [erigon_release](clients/erigon_release.md)
- [go-ethereum_trace](clients/go-ethereum_trace.md)
- [nethermind_development](clients/nethermind_development.md)
- [nethermind_release](clients/nethermind_release.md)
- [reth_development](clients/reth_development.md)
- [reth_release](clients/reth_release.md)

## Runs

| Run | Corpus | Capture complete | Versions |
| --- | --- | --- | --- |
| [geth-e29edff-a](../evidence/2026-09-21/geth-e29edff-a/manifest.json) | a | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [geth-e29edff-fork-followup](../evidence/2026-09-21/geth-e29edff-fork-followup/manifest.json) | fork-followup | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [geth-e29edff-forks](../evidence/2026-09-21/geth-e29edff-forks/manifest.json) | forks | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [geth-e29edff-initial](../evidence/2026-09-21/geth-e29edff-initial/manifest.json) | initial | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [geth-e29edff-precompiles](../evidence/2026-09-21/geth-e29edff-precompiles/manifest.json) | precompiles | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [geth-e29edff-reorg-safe](../evidence/2026-09-21/geth-e29edff-reorg-safe/manifest.json) | reorg-safe | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [geth-e29edff-repeat](../evidence/2026-09-21/geth-e29edff-repeat/manifest.json) | repeat | True | {'go-ethereum_trace': 'Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1'} |
| [precompiles-final](../evidence/2026-09-21/precompiles-final/manifest.json) | precompiles | True | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-a](../evidence/2026-09-21/verified-a/manifest.json) | a | False | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-a-besu-retry](../evidence/2026-09-21/verified-a-besu-retry/manifest.json) | a | True | {'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25'} |
| [verified-fork-followup](../evidence/2026-09-21/verified-fork-followup/manifest.json) | fork-followup | False | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-fork-followup-besu-retry](../evidence/2026-09-21/verified-fork-followup-besu-retry/manifest.json) | fork-followup | True | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25'} |
| [verified-forks](../evidence/2026-09-21/verified-forks/manifest.json) | forks | True | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-initial](../evidence/2026-09-21/verified-initial/manifest.json) | initial | True | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-pruned](../evidence/2026-09-21/verified-pruned/manifest.json) | pruned | False | {'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-pruned-ready](../evidence/2026-09-21/verified-pruned-ready/manifest.json) | pruned | True | {'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-reorg-ready](../evidence/2026-09-21/verified-reorg-ready/manifest.json) | reorg-safe | False | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-reorg-safe](../evidence/2026-09-21/verified-reorg-safe/manifest.json) | reorg-safe | False | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |
| [verified-repeat](../evidence/2026-09-21/verified-repeat/manifest.json) | repeat | True | {'besu_development': 'besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25', 'besu_release': 'besu/v26.8.1/linux-x86_64/openjdk-java-25', 'erigon_development': '3.8.0-dev-c25b8e47', 'erigon_release': '3.6.1-0c4d9c91', 'nethermind_development': '2.1.0-unstable+a404c4f0', 'nethermind_release': '1.39.3+28cbe2a0', 'reth_development': 'Reth Version: 2.5.2+03cb186c', 'reth_release': 'Reth Version: 2.6.0+73a3a008'} |

## Review decisions

- [H01 — Method coverage](decisions/H01.md)
- [H02 — trace_get selector and return shape](decisions/H02.md)
- [H03 — Filter composition and mode](decisions/H03.md)
- [H04 — Empty address lists](decisions/H04.md)
- [H05 — Post-merge reward records](decisions/H05.md)
- [H06 — Missing transactions and paths](decisions/H06.md)
- [H07 — Replay transactionHash field](decisions/H07.md)
- [H08 — Empty output and unrequested components](decisions/H08.md)
- [H09 — Failed frame results and error labels](decisions/H09.md)
- [H10 — Creation result field names](decisions/H10.md)
- [H11 — Empty trace-type selection](decisions/H11.md)
- [H12 — Raw-transaction block argument](decisions/H12.md)
- [H13 — Signed transaction nonce validation](decisions/H13.md)
- [H14 — Invalid-parameter error codes](decisions/H14.md)
- [H15 — Unsigned simulation fees and block environment](decisions/H15.md)
- [H16 — Fee accounting and sequential state diffs](decisions/H16.md)
- [H17 — New-account stateDiff encoding](decisions/H17.md)
- [H18 — EIP-7702 code changes in stateDiff](decisions/H18.md)
- [H19 — vmTrace executing bytecode](decisions/H19.md)
- [H20 — vmTrace step timing and deltas](decisions/H20.md)
- [H21 — vmTrace numeric and optional metadata encoding](decisions/H21.md)
- [H22 — Precompile return bytes](decisions/H22.md)
- [H23 — Special-action address matching](decisions/H23.md)
- [H24 — Sibling failure isolation](decisions/H24.md)
- [H25 — Well-formed errors for rejected raw transactions](decisions/H25.md)
- [H26 — Account deletion across Cancun](decisions/H26.md)
- [H27 — Filter execution across fork boundaries](decisions/H27.md)
- [H28 — Historical state at system-operation boundaries](decisions/H28.md)
- [H29 — Precompile call-frame inclusion](decisions/H29.md)
