# Replay missing

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Retain supporting reference evidence. Unknown transaction returns null, not an empty collection or RPC error. The method responds without Method not found (-32601).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H06](../../decisions/H06.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H06](../../decisions/H06.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 0a663f3c** (`Geth/v1.17.7-unstable-0a663f3c-2026-09-24/linux-amd64/go1.26.1`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
