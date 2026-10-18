# Filter blockhash address to

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 59 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "toAddress": [
        "0x0000000000000000000000000000000000000000",
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603"
      ]
    }
  ]
}
```

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H33](../../decisions/H33.md): Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-address-to has 6 records from block 0x2.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H33](../../decisions/H33.md): Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-address-to has 6 records from block 0x2.

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../decisions/H33.md): Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter. Answered another block: 59 records from 18 blocks, block 0x2 with hash None… to block 0x2e, where the numeric equivalent filter-block-2-address-to has 6 records from block 0x2.

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H33](../../decisions/H33.md): Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-address-to has 6 records from block 0x2.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): Recipient matching, including a reward matched by its author, applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-address-to has 6 records from block 0x2.

</details>
