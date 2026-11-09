# Filter page 2

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 4 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/a/manifest.json) |

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

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `1`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

</details>
