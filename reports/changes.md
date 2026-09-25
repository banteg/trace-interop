# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-25T08:32:17.467627+00:00**, [preflight](../evidence/2026-09-25/refresh/preflight.json)) against the previous one (checked at **2026-09-24T21:54:10.993904+00:00**, [preflight](../evidence/2026-09-25/fixture-wave/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Besu stable | 26.8.1 · d97cbd61 | 26.8.1 · d97cbd61 | Unchanged |
| Besu dev | 26.9-develop · cf89071f | 26.9-develop · accdae00 | Updated |
| Erigon stable | 3.6.1 · 0c4d9c91 | 3.7.0 · bdc78cc4 | Updated |
| Erigon dev | 3.8.0-dev · 01c118ee | 3.8.0-dev · f8cfe5a7 | Updated |
| Geth draft fork | 1.17.7-unstable · 0a663f3c | 1.17.7-unstable · 0a663f3c | Unchanged |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · 54b760cd | 2.1.0-preview · ee1f57da | Updated |
| Reth stable | 2.6.0 · 73a3a008 | 2.6.0 · 73a3a008 | Unchanged |
| Reth dev | 2.5.2 · 58a51b3e | 2.5.2 · 4630cc58 | Updated |

## Verdict changes

7 verdicts changed for 3 clients.

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H02 · trace_get selector and return shape](decisions/H02.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H03 · Filter composition and mode](decisions/H03.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H05 · Post-merge reward records](decisions/H05.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
| [H31 · Omitted trace_callMany block](decisions/H31.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
