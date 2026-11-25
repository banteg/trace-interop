# Filter blockhash genesis

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** The genesis hash selects the genesis block, which has no trace records: [].

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |

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

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 3 records from block 0x30 (the head), where block 0x0 has [].

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Answered another block: 3 records from block 0x30 (the head), where block 0x0 has [].

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H33](../../decisions/H33.md): The genesis hash selects the genesis block, which has no trace records: []. Rejected (-32602: Invalid params), where block 0x0 has [].

</details>
