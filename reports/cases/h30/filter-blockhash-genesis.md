# Filter blockhash genesis

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The genesis hash selects the genesis block, which has no trace records: []. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 245 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/h30/manifest.json) |
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
      "blockHash": "0x3870d74fb940a1a64619292ab344fa0d5dad6d8617c9079356d6949ffc80d582"
    }
  ]
}
```

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where block 0x0 has [].

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: unknown field `blockHash`, expected one of `fromBlock`, `toBlock`, `fromAddress`, `toAddress`, `mode`, `after`, `count`), where block 0x0 has [].

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 245 records from 48 blocks, block 0x1 to block 0x30 (the head), where block 0x0 has [].

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: Invalid params), where block 0x0 has [].

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: Invalid params), where block 0x0 has [].

</details>
