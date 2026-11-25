# Filter failed nested create recipient

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** A failed nested CREATE has no created-address match.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3",
      "toAddress": [
        "0xd8353791c13be48589d7247c3284625edca5aa72"
      ],
      "toBlock": "0x3"
    }
  ]
}
```

</details>
