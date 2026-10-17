# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-16T23:48:59.042359+00:00**, [preflight](../evidence/2026-10-17/eval/preflight.json)) against the previous one (checked at **2026-10-11T12:46:46.611161+00:00**, [preflight](../evidence/2026-10-11/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.5 · 51a52c59 | 1.8.5 · 51a52c59 | Unchanged |
| Anvil dev | 1.8.6-nightly · 32624734 | 1.8.6-nightly · de005f70 | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.10.0 · 976ca7ea | Updated |
| Besu dev | 26.10-develop · d05d8e74 | 26.10-develop · 0776d82f | Updated |
| Erigon stable | 3.7.1 · 8c1e3893 | 3.7.1 · 8c1e3893 | Unchanged |
| Erigon dev | 3.8.0-dev · 1d3ebbf2 | 3.8.0-dev · 5b452f41 | Updated |
| Geth draft fork | 1.17.7-unstable · e67cfd25 | 1.17.7-unstable · 71db3b03 | Updated |
| Nethermind stable | 2.1.0 · b3e7e84c | 2.2.0 · 1d2aff00 | Updated |
| Nethermind dev | 2.2.0-preview · 204457ad | 2.2.0-preview · cd336c4c | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 1a4dbbe1 | 2.7.0 · ec3e7e42 | Updated |

## Verdict changes

23 verdicts changed for 3 clients.

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H06 · Missing transactions and paths](decisions/H06.md) | Besu stable | ⚠️ Differs | 🟡 Partially assessed |
| [H11 · Empty trace-type selection](decisions/H11.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Besu stable | ⚠️ Differs | 🟡 Partially assessed |
| [H25 · Well-formed errors for rejected raw transactions](decisions/H25.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Besu stable | ⚠️ Differs | 🟡 Partially assessed |
| [H06 · Missing transactions and paths](decisions/H06.md) | Besu dev | ⚠️ Differs | 🟡 Partially assessed |

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H02 · trace_get selector and return shape](decisions/H02.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H03 · Filter composition and mode](decisions/H03.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H04 · Empty address lists](decisions/H04.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H05 · Post-merge reward records](decisions/H05.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H06 · Missing transactions and paths](decisions/H06.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H23 · Special-action address matching](decisions/H23.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H25 · Well-formed errors for rejected raw transactions](decisions/H25.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
