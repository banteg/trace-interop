# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-05T19:51:21.922482+00:00**, [preflight](../evidence/2026-10-05/eval/preflight.json)) against the previous one (checked at **2026-10-04T19:36:57.679798+00:00**, [preflight](../evidence/2026-10-04/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.4 · 50af4efe | 1.8.5 · 51a52c59 | Updated |
| Anvil dev | 1.8.4-nightly · 60255eee | 1.8.4-nightly · e15c2f1c | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.10-develop · 1d62d893 | 26.10-develop · 1d62d893 | Unchanged |
| Erigon stable | 3.7.1 · 8c1e3893 | 3.7.1 · 8c1e3893 | Unchanged |
| Erigon dev | 3.8.0-dev · 5cb6c867 | 3.8.0-dev · 96188a47 | Updated |
| Geth draft fork | 1.17.7-unstable · e67cfd25 | 1.17.7-unstable · e67cfd25 | Unchanged |
| Nethermind stable | 2.1.0 · b3e7e84c | 2.1.0 · b3e7e84c | Unchanged |
| Nethermind dev | 2.2.0-preview · 6dff813b | 2.2.0-preview · e8955c4c | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 10bcf461 | 2.7.0 · 42fa3c56 | Updated |

## Verdict changes

8 verdicts changed for 1 client.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H02 · trace_get selector and return shape](decisions/H02.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H06 · Missing transactions and paths](decisions/H06.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H07 · Replay transactionHash field](decisions/H07.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H02 · trace_get selector and return shape](decisions/H02.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H07 · Replay transactionHash field](decisions/H07.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
