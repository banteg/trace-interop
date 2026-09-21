# Trace API draft impact

Proposals for review, not an adopted standard or a client ranking. Historical recommendations date to September 15. Fresh checks below are restricted to the exact pinned builds and selected cases. Schema validity, partial semantic assertions and full conformance are different claims.

Draft: [1143c7b33b93](https://github.com/banteg/execution-apis/commit/1143c7b33b93841d4e89f6f63d12d3e8f95d8b3c).

## Client impact

- [besu_release](clients/besu_release.md)
- [erigon_release](clients/erigon_release.md)
- [nethermind_release](clients/nethermind_release.md)
- [reth_release](clients/reth_release.md)

## Runs

| Run | Corpus | Capture complete | Versions |
| --- | --- | --- | --- |

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
