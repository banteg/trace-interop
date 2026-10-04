# Replay missing

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Unknown transaction returns null, not an empty collection or RPC error. The method responds without Method not found (-32601). Retain supporting reference evidence. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | RPC error `-32001` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | `null` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H06](../../decisions/H06.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H06](../../decisions/H06.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H06](../../decisions/H06.md): Unknown transaction returns null, not an empty collection or RPC error.
- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H07](../../decisions/H07.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
