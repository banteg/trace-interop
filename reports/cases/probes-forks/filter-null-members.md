# Filter null members

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Null mode, after, count and address lists are omitted, so blocks 2-5 return every record.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

</details>
