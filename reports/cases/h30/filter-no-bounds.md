# Filter no bounds

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An omitted fromBlock starts at the genesis (earliest) block before count is applied.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": 3
    }
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H30](../../decisions/H30.md): An omitted fromBlock starts at the genesis (earliest) block before count is applied.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H30](../../decisions/H30.md): An omitted fromBlock starts at the genesis (earliest) block before count is applied.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H30](../../decisions/H30.md): An omitted fromBlock starts at the genesis (earliest) block before count is applied.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H30](../../decisions/H30.md): An omitted fromBlock starts at the genesis (earliest) block before count is applied.

</details>
