# Filter blockhash union

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** mode union applies to the hash-selected block as to the numeric single-block filter. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "toAddress": [
        "0x0000000000000000000000000000000000000000"
      ],
      "mode": "union"
    }
  ]
}
```

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

</details>
