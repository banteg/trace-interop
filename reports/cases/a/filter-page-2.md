# Filter page 2

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |

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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

</details>
