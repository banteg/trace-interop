# Filter failed nested create recipient

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** A failed nested CREATE has no created-address match. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

</details>
