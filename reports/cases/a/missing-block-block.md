# Missing block block

`trace_block` · a · [All reports](../../README.md)

**What this checks:** An unknown selected block returns an error with code -32001, never null or a result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0xffff"
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

</details>
