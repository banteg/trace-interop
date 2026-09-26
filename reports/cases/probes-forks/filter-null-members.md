# Filter null members

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Null mode, after, count and address lists are omitted, so blocks 2-5 return every record.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-forks/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 invalid argument 0: invalid trace filter mode "": want union or intersection

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

</details>
