# Missing block filter

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** An unknown selected block or range endpoint returns Resource not found (-32001).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/a/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": 1,
      "fromBlock": "0x2f",
      "toBlock": "0xffff"
    }
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): An unknown selected block or range endpoint returns Resource not found (-32001).

</details>
