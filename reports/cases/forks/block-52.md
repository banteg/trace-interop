# Block 52

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x34"
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x133d8', 'input': '0x74bff204de43b4a2656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xa9578be0967413b9adc40736fd4ec67d0529b890a81d62102db05e61d6de1897', 'blo

</details>
