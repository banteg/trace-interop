# Filter null fromblock

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** A null fromBlock is omitted, so it resolves to the same latest head. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 355 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |

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

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property

</details>
