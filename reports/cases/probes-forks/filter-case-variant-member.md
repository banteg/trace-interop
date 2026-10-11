# Filter case variant member

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** TOBLOCK takes effect as toBlock, so blocks 2-3 return every record, or the request is rejected (-32602 recommended); never ignored, which would widen the range to the head.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 8 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-11/h14-case-variant/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/h14-case-variant/probes-forks/manifest.json) |

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

- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

</details>
