# Filter blockhash unknown count zero

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |

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

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Accepted: returned [], the count 0 shortcut before validating the selector.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Accepted: returned [], the count 0 shortcut before validating the selector.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32000: Block not found); the code must be -32001.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32000: header not found); the code must be -32001.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H33](../../decisions/H33.md): An unknown hash is an error even with count 0: the selector is validated before any count 0 shortcut, so [] does not pass. Rejected (-32602: Invalid params); the code must be -32001.

</details>
