# Genesis filter

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** The genesis block has no transaction or reward records.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x0",
      "toBlock": "0x0"
    }
  ]
}
```

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. 1 unexpected extra records, first {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xcf99eb0a280bf38e32a54b8cb1d4403fd277ef7b4ff1836b6b2dc3d8d098e409', 'blockNumber': 0, 'result': None, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. 1 unexpected extra records, first {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xcf99eb0a280bf38e32a54b8cb1d4403fd277ef7b4ff1836b6b2dc3d8d098e409', 'blockNumber': 0, 'result': None, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. 1 unexpected extra records, first {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xcf99eb0a280bf38e32a54b8cb1d4403fd277ef7b4ff1836b6b2dc3d8d098e409', 'blockNumber': 0, 'result': None, 'subtraces': 0, 'traceAddress': [], 'transactionHash': None, 'transactionPosition': None, 'type': 'reward'}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. 1 unexpected extra records, first {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xcf99eb0a280bf38e32a54b8cb1d4403fd277ef7b4ff1836b6b2dc3d8d098e409', 'blockNumber': 0, 'result': None, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

</details>
