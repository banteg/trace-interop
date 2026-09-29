# Filter page 2

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "after": 8,
      "count": 4
    }
  ]
}
```

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

</details>
