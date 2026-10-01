# Block 55

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x37"
  ]
}
```

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x133d8', 'input': '0xe62b8536019651e7656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee', 'blo

</details>
