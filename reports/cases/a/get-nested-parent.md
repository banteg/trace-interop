# Get nested parent

`trace_get` · a · [All reports](../../README.md)

**What this checks:** Return the transaction-tree record at [6], or null if absent.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | One frame, path `[6]` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | One frame, path `[6]` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | One frame, path `[6]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x6"
    ]
  ]
}
```

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- Result shape at `/`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- Result shape at `/`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

</details>
