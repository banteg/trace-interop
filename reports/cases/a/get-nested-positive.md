# Get nested positive

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [6, 0], or null if absent. Reward and SELFDESTRUCT records carry result null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | One frame, path `[6, 0]` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | One frame, path `[6, 0]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x6",
      "0x0"
    ]
  ]
}
```

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `/`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

</details>
