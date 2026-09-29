# Genesis filter

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** The genesis block has no transaction or reward records.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-forks/manifest.json) |

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

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. 1 unexpected extra records, first {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0xcf99eb0a280bf38e32a54b8cb1d4403fd277ef7b4ff1836b6b2dc3d8d098e409', 'blockNumber': 0, 'result': None, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'}
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property

</details>
