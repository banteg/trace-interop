# Filter negative count

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "count": -1
    }
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

</details>
