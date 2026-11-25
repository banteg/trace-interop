# Withdrawal filter 51

`trace_filter` · fork-followup · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/fork-followup/manifest.json) |

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
