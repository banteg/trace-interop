# Block 56

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x38"
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x11ba0', 'input': '0x74fb911b03a9f447656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x3'}, 'blockHash': '0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3', 'blo

</details>
