# Filter case variant member

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** TOBLOCK takes effect as toBlock, so blocks 2-3 return every record, or the request is rejected (-32602 recommended); never ignored, which would widen the range to the head.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "TOBLOCK": "0x3",
      "fromBlock": "0x2"
    }
  ]
}
```

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

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

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

</details>
