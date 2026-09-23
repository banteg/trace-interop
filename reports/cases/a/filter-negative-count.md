# Filter negative count

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": -1,
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). -1 is less than the minimum of 0

</details>
