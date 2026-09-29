# Filter blockhash address from

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Address matching applies to the hash-selected block as to the numeric single-block filter. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 133 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/h33-blockhash/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/h33-blockhash/h30/manifest.json) |

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
      ]
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Answered another block: 133 records from 48 blocks, block 0x1 to block 0x30 (the head), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: invalid argument 0: json: unknown field "blockHash"), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Answered another block: 3 records from block 0x30 (the head), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): Address matching applies to the hash-selected block as to the numeric single-block filter. Rejected (-32602: Invalid params), where the numeric equivalent filter-block-2-address-from has 5 records from block 0x2.

</details>
