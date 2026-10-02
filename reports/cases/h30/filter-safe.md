# Filter safe

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The safe tag resolves to the fixture safe head, block 48.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/h30/manifest.json) |

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

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H32](../../decisions/H32.md): The safe tag resolves to the fixture safe head, block 48.

</details>
