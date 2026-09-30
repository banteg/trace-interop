# Filter safe

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The safe tag resolves to the fixture safe head, block 48.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "safe",
      "toBlock": "safe",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

</details>
