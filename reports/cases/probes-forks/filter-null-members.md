# Filter null members

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Null mode, after, count and address lists are omitted, so blocks 2-5 return every record.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": null,
      "count": null,
      "fromAddress": null,
      "fromBlock": "0x2",
      "mode": null,
      "toAddress": null,
      "toBlock": "0x5"
    }
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Erigon · 3.8.0-dev · 923b4d31** (`3.8.0-dev-923b4d31`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

</details>
