# Filter 48

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x30",
      "toBlock": "0x30"
    }
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':

</details>
