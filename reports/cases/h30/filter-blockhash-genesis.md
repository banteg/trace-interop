# Filter blockhash genesis

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The genesis hash selects the genesis block, which has no trace records: []. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 245 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0x3870d74fb940a1a64619292ab344fa0d5dad6d8617c9079356d6949ffc80d582"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where block 0x0 has [].

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where block 0x0 has [].

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 4 records from block 0x30 (the head), where block 0x0 has [].

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 4 records from block 0x30 (the head), where block 0x0 has [].

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 3 records from block 0x30 (the head), where block 0x0 has [].

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 245 records from 48 blocks, block 0x1 to block 0x30 (the head), where block 0x0 has [].

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: invalid argument 0: json: unknown field "blockHash"), where block 0x0 has [].

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: Invalid params), where block 0x0 has [].

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 4 records from block 0x30 (the head), where block 0x0 has [].
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: Invalid params), where block 0x0 has [].

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: Invalid params), where block 0x0 has [].

</details>
