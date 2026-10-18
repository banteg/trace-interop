# Filter blockhash unknown

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An unknown hash is an error (-32001 recommended), never [] or another block’s records. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 245 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf41d91222581f534cea6e7278e4a4e7e8e1c4fb3494dc9e4be41268beeaadd79"
    }
  ]
}
```

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001 recommended), never [] or another block’s records. Accepted: answered another block, 245 records from 48 blocks, block 0x1 to block 0x30 (the head).

</details>
