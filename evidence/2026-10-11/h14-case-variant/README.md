# H14 filter member case — 2026-10-11

A focused recapture of `probes-forks` that adds `filter-case-variant-member`. It runs with the
[2026-10-05 eval](../../2026-10-05/eval/README.md)'s [build lock](../../2026-10-05/eval/clients.lock.json)
(`trace_interop run --lock`), so every build is that matrix's image; Anvil is not captured for `probes-forks`
(it needs Hive). It resends every request of that matrix's `probes-forks` run, so
[reports.lock.json](../../../reports.lock.json) selects it in place of that run. Captured on Fedora from harness
commit `8c57047e` with disposable Hive chains.

[probes-forks](probes-forks/summary.json) is complete: **576 responses**, and every build passed the setup
controls.

## Probe

[Erigon #24706](https://github.com/erigontech/erigon/pull/24706) rejects unknown `trace_filter` members but keeps
Go's case-insensitive member names, so the draft had to say whether `FROMBLOCK` is an unknown member. The
probe sends `{"fromBlock": "0x2", "TOBLOCK": "0x3"}`. Honoring `TOBLOCK` as `toBlock` returns the 8 records of
blocks 2-3; ignoring it leaves `toBlock` at the head, a wider range; rejecting it is an error.

## Findings

| Builds | Response |
| --- | --- |
| Besu 26.9.0 and develop | -32602 `Invalid filter params` |
| Reth 2.7.0 (both builds) | -32602 ``unknown field `TOBLOCK`, expected one of `fromBlock`, `toBlock`, …`` |
| Erigon 3.7.1 and 3.8.0-dev, Nethermind 2.1.0 and 2.2.0-preview, Geth draft | the 8 records of blocks 2-3 |

No build ignores the member. Exact-name decoders (Jackson, serde) reject it; case-insensitive ones (Go's
`encoding/json`, Nethermind's `PropertyNameCaseInsensitive`) apply it. The draft
([execution-apis 29df74f](https://github.com/banteg/execution-apis/commit/29df74f9327e2ab5e6ba7ee9f2888c1f661f441d))
therefore lets a server match member names case-insensitively, provided each member takes effect or is rejected,
and the probe accepts either answer.
