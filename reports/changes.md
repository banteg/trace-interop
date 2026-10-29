# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-29T12:46:43.495599+00:00**, [preflight](../evidence/2026-10-29/eval/preflight.json)) against the previous one (checked at **2026-10-23T15:49:32.883363+00:00**, [preflight](../evidence/2026-10-23/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.6 · 6bad0a66 | 1.8.6 · 6bad0a66 | Unchanged |
| Anvil dev | 1.8.7-nightly · 4e8874b2 | 1.8.7-nightly · 716e795c | Updated |
| Besu stable | 26.10.1 · e83703cd | 26.10.2 · d3e1aea7 | Updated |
| Besu dev | 26.10-develop · 781a7e1d | 26.10-develop · 7f08e68a | Updated |
| Erigon stable | 3.8.0 · 7539da15 | 3.8.1 · cf6f1413 | Updated |
| Erigon dev | 3.9.0-dev · 598ba625 | 3.9.0-dev · 6955d198 | Updated |
| Geth draft fork | 1.17.9-unstable · a15b96ff | 1.17.11-unstable · 0f1fb2ae | Updated |
| Nethermind stable | 2.2.1 · c4f1015b | 2.2.2 · be201120 | Updated |
| Nethermind dev | 2.3.0-preview · 7192e7f3 | 2.3.0-preview · fc9abf09 | Updated |
| Reth stable | 2.8.1 · d763342f | 2.9.0 · c9a780f4 | Updated |
| Reth dev | 2.8.0 · 53bf066f | 2.8.1 · 966010c9 | Updated |

## Verdict changes

8 verdicts changed for 2 clients.

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H03 · Filter composition and mode](decisions/H03.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H31 · Omitted trace_callMany block](decisions/H31.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Reth stable | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Reth stable | ⚠️ Differs | 🟡 Partially assessed |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Reth dev | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Reth dev | ⚠️ Differs | 🟡 Partially assessed |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
