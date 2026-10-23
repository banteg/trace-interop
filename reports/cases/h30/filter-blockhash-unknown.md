# Filter blockhash unknown

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An unknown hash is an error (-32001), never [] or another block’s records.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/h30/manifest.json) |

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

**Anvil · 1.8.7-nightly · 4e8874b2** (`anvil Version: 1.8.7-nightly+4e8874b2`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`); the code must be -32001.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`); the code must be -32001.

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32000: Block not found); the code must be -32001.

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32000: header not found); the code must be -32001.

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32602: Invalid params); the code must be -32001.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H33](../../decisions/H33.md): An unknown hash is an error (-32001), never [] or another block’s records. Rejected (-32602: Invalid params); the code must be -32001.

</details>
