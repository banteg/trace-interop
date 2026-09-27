# Missing block block

`trace_block` · a · [All reports](../../README.md)

**What this checks:** An unknown single selected block returns an error (-32001 recommended), never null or a result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 07915e32](../../clients/anvil_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 3904de43](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 5ece5fba](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |
| [Reth · 2.5.2 · 863f7055](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-27/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-27/eval/a/manifest.json) |

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

**Anvil · 1.8.4-nightly · 07915e32** (`anvil Version: 1.8.4-nightly+07915e32`)

- [H06](../../decisions/H06.md): An unknown single selected block returns an error (-32001 recommended), never null or a result.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H06](../../decisions/H06.md): An unknown single selected block returns an error (-32001 recommended), never null or a result.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown single selected block returns an error (-32001 recommended), never null or a result.
- Result shape at `/`: None is not of type 'array'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown single selected block returns an error (-32001 recommended), never null or a result.
- Result shape at `/`: None is not of type 'array'

</details>
