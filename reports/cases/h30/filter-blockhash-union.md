# Filter blockhash union

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** mode union applies to the hash-selected block as to the numeric single-block filter. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 133 records | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |

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

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. The numeric equivalent filter-block-2-union returned no result.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. The numeric equivalent filter-block-2-union returned no result.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Answered another block: 133 records from 48 blocks, block 0x1 to block 0x30 (the head), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Returned [] where the numeric equivalent filter-block-2-union has 1 record from block 0x2.

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): mode union applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-union has 5 records from block 0x2.

</details>
