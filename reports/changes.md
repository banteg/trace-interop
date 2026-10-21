# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-21T12:45:09.576437+00:00**, [preflight](../evidence/2026-10-21/eval/preflight.json)) against the previous one (checked at **2026-10-18T13:06:24.102777+00:00**, [preflight](../evidence/2026-10-18/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.5 · 51a52c59 | 1.8.5 · 51a52c59 | Unchanged |
| Anvil dev | 1.8.6-nightly · 6c21ffe2 | 1.8.6-nightly · 9089a6bf | Updated |
| Besu stable | 26.10.0 · 976ca7ea | 26.10.0 · 976ca7ea | Unchanged |
| Besu dev | 26.10-develop · abdf1419 | 26.10-develop · 7590302e | Updated |
| Erigon stable | 3.7.1 · 8c1e3893 | 3.8.0 · 7539da15 | Updated |
| Erigon dev | 3.9.0-dev · 1ee57924 | 3.9.0-dev · d23467c5 | Updated |
| Geth draft fork | 1.17.9-unstable · fdbb46a5 | 1.17.9-unstable · a15b96ff | Updated |
| Nethermind stable | 2.2.0 · 1d2aff00 | 2.2.0 · 1d2aff00 | Unchanged |
| Nethermind dev | 2.2.0-preview · 159862be | 2.3.0-preview · e2e011c8 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.8.0 · 05ba4812 | Updated |
| Reth dev | 2.7.0 · e6679687 | 2.8.0 · 05ba4812 | Updated |

## Verdict changes

26 verdicts changed for 4 clients.

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H03 · Filter composition and mode](decisions/H03.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
| [H31 · Omitted trace_callMany block](decisions/H31.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H03 · Filter composition and mode](decisions/H03.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Erigon stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H11 · Empty trace-type selection](decisions/H11.md) | Erigon stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Erigon stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Erigon stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H23 · Special-action address matching](decisions/H23.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H05 · Post-merge reward records](decisions/H05.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H06 · Missing transactions and paths](decisions/H06.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H05 · Post-merge reward records](decisions/H05.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H06 · Missing transactions and paths](decisions/H06.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
