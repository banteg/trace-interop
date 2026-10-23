# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-23T15:49:32.883363+00:00**, [preflight](../evidence/2026-10-23/eval/preflight.json)) against the previous one (checked at **2026-10-21T12:45:09.576437+00:00**, [preflight](../evidence/2026-10-21/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.5 · 51a52c59 | 1.8.6 · 6bad0a66 | Updated |
| Anvil dev | 1.8.6-nightly · 9089a6bf | 1.8.7-nightly · 4e8874b2 | Updated |
| Besu stable | 26.10.0 · 976ca7ea | 26.10.1 · e83703cd | Updated |
| Besu dev | 26.10-develop · 7590302e | 26.10-develop · 781a7e1d | Updated |
| Erigon stable | 3.8.0 · 7539da15 | 3.8.0 · 7539da15 | Unchanged |
| Erigon dev | 3.9.0-dev · d23467c5 | 3.9.0-dev · 598ba625 | Updated |
| Geth draft fork | 1.17.9-unstable · a15b96ff | 1.17.9-unstable · a15b96ff | Unchanged |
| Nethermind stable | 2.2.0 · 1d2aff00 | 2.2.1 · c4f1015b | Updated |
| Nethermind dev | 2.3.0-preview · e2e011c8 | 2.3.0-preview · 7192e7f3 | Updated |
| Reth stable | 2.8.0 · 05ba4812 | 2.8.1 · d763342f | Updated |
| Reth dev | 2.8.0 · 05ba4812 | 2.8.0 · 53bf066f | Updated |

## Verdict changes

1 verdict changed for 1 client.

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
