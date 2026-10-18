# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-18T13:06:24.102777+00:00**, [preflight](../evidence/2026-10-18/eval/preflight.json)) against the previous one (checked at **2026-10-16T23:48:59.042359+00:00**, [preflight](../evidence/2026-10-17/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.5 · 51a52c59 | 1.8.5 · 51a52c59 | Unchanged |
| Anvil dev | 1.8.6-nightly · de005f70 | 1.8.6-nightly · 6c21ffe2 | Updated |
| Besu stable | 26.10.0 · 976ca7ea | 26.10.0 · 976ca7ea | Unchanged |
| Besu dev | 26.10-develop · 0776d82f | 26.10-develop · abdf1419 | Updated |
| Erigon stable | 3.7.1 · 8c1e3893 | 3.7.1 · 8c1e3893 | Unchanged |
| Erigon dev | 3.8.0-dev · 5b452f41 | 3.9.0-dev · 1ee57924 | Updated |
| Geth draft fork | 1.17.7-unstable · 71db3b03 | 1.17.9-unstable · fdbb46a5 | Updated |
| Nethermind stable | 2.2.0 · 1d2aff00 | 2.2.0 · 1d2aff00 | Unchanged |
| Nethermind dev | 2.2.0-preview · cd336c4c | 2.2.0-preview · 159862be | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · ec3e7e42 | 2.7.0 · e6679687 | Updated |

## Verdict changes

1 verdict changed for 1 client.

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
