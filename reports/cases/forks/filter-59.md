# Filter 59

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-geth-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-forks/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 3 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 3 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/harness-audit-native-forks/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3b",
      "toBlock": "0x3b"
    }
  ]
}
```

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

</details>
