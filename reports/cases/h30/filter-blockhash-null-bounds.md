# Filter blockhash null bounds

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Null fromBlock and toBlock are omitted, so a blockHash with null bounds selects that block. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "fromBlock": null,
      "toBlock": null,
      "count": 3
    }
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H33](../../decisions/H33.md): Null fromBlock and toBlock are omitted, so a blockHash with null bounds selects that block. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2 has 3 records from block 0x2.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H33](../../decisions/H33.md): Null fromBlock and toBlock are omitted, so a blockHash with null bounds selects that block. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2 has 3 records from block 0x2.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H33](../../decisions/H33.md): Null fromBlock and toBlock are omitted, so a blockHash with null bounds selects that block. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2 has 3 records from block 0x2.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H33](../../decisions/H33.md): Null fromBlock and toBlock are omitted, so a blockHash with null bounds selects that block. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2 has 3 records from block 0x2.

</details>
