# Withdrawal filter 51

`trace_filter` · fork-followup · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x33",
      "toBlock": "0x33",
      "toAddress": [
        "0x717f8aa2b982bee0e29f573d31df288663e1ce16"
      ]
    }
  ]
}
```

</details>
