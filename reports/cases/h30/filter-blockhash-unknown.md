# Filter blockhash unknown

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An unknown hash is an error (-32001 recommended), never [] or another block’s records. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 245 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |

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

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001 recommended), never [] or another block’s records. Accepted: answered another block, 4 records from block 0x30 (the head).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001 recommended), never [] or another block’s records. Accepted: answered another block, 4 records from block 0x30 (the head).

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001 recommended), never [] or another block’s records. Accepted: answered another block, 3 records from block 0x30 (the head).

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001 recommended), never [] or another block’s records. Accepted: answered another block, 245 records from 48 blocks, block 0x1 to block 0x30 (the head).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001 recommended), never [] or another block’s records. Accepted: answered another block, 4 records from block 0x30 (the head).
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>
