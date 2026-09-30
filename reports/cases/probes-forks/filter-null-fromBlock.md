# Filter null fromblock

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A null fromBlock is omitted, so it resolves to the same latest head. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 355 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": null,
      "toBlock": "0x48"
    }
  ]
}
```

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>
