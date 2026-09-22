# Beacon call 56

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Historical trace_call uses only system changes through the selected block.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup-besu-retry/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-23/geth-40eecf3-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-fork-followup/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x0000000000000000000000000000000000000000000000000000000000000230",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02"
    },
    [
      "trace"
    ],
    "0x38"
  ]
}
```

</details>
