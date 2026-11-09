# Filter blockhash unknown count zero

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf41d91222581f534cea6e7278e4a4e7e8e1c4fb3494dc9e4be41268beeaadd79",
      "count": 0
    }
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`); the code must be -32001.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`); the code must be -32001.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32000: Block not found); the code must be -32001.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32000: header not found); the code must be -32001.

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32602: Invalid params); the code must be -32001.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32602: Invalid params); the code must be -32001.

</details>
