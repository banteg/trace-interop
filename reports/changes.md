# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-04T19:36:57.679798+00:00**, [preflight](../evidence/2026-10-04/eval/preflight.json)) against the previous one (checked at **2026-10-02T14:41:05.957366+00:00**, [preflight](../evidence/2026-10-02/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.4 · 50af4efe | 1.8.4 · 50af4efe | Unchanged |
| Anvil dev | 1.8.4-nightly · 328811cb | 1.8.4-nightly · 60255eee | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.10-develop · 711f8142 | 26.10-develop · 1d62d893 | Updated |
| Erigon stable | 3.7.1 · 8c1e3893 | 3.7.1 · 8c1e3893 | Unchanged |
| Erigon dev | 3.8.0-dev · 6da806cb | 3.8.0-dev · 5cb6c867 | Updated |
| Geth draft fork | 1.17.7-unstable · 67f41dea | 1.17.7-unstable · e67cfd25 | Updated |
| Nethermind stable | 2.1.0 · b3e7e84c | 2.1.0 · b3e7e84c | Unchanged |
| Nethermind dev | 2.2.0-preview · 3370d566 | 2.2.0-preview · 6dff813b | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 078d0262 | 2.7.0 · 10bcf461 | Updated |

## Verdict changes

6 verdicts changed for 4 clients.

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Erigon dev | ⚠️ Differs | 🟡 Partially assessed |

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Nethermind dev | ✅ Checked cases agree | ⚠️ Differs |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
