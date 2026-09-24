# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-24T18:52:50.958598+00:00**, [preflight](../evidence/2026-09-24/adopted-stances/preflight.json)) against the previous one (checked at **2026-09-24T12:56:09.478062+00:00**, [preflight](../evidence/2026-09-24/h15-call-compat/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Besu stable | 26.8.1 · d97cbd61 | 26.8.1 · d97cbd61 | Unchanged |
| Besu dev | 26.9-develop · f9572aa8 | 26.9-develop · 85b32978 | Updated |
| Erigon stable | 3.6.1 · 0c4d9c91 | 3.6.1 · 0c4d9c91 | Unchanged |
| Erigon dev | 3.8.0-dev · e26d9bd4 | 3.8.0-dev · e26d9bd4 | Unchanged |
| Geth draft fork | 1.17.7-unstable · fa8ecb92 | 1.17.7-unstable · bb5c4682 | Updated |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-unstable · 641592d2 | 2.1.0-preview · ce501a97 | Updated |
| Reth stable | 2.6.0 · 73a3a008 | 2.6.0 · 73a3a008 | Unchanged |
| Reth dev | 2.5.2 · 58a51b3e | 2.5.2 · 58a51b3e | Unchanged |

## Verdict changes

8 verdicts changed for 1 client.

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H06 · Missing transactions and paths](decisions/H06.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Geth draft fork | ⚠️ Differs | 🟡 Partially assessed |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
