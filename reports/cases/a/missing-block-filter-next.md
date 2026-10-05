# Missing block filter next

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** A range bound beyond the head returns an error (-32602 recommended), as eth_getLogs does; never a clamped or partial result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x30",
      "toBlock": "0x31",
      "count": 1
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns an error (-32602 recommended), as eth_getLogs does; never a clamped or partial result.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H06](../../decisions/H06.md): A range bound beyond the head returns an error (-32602 recommended), as eth_getLogs does; never a clamped or partial result.

</details>
