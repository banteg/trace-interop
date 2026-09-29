# Block 59

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
    "0x3b"
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x1'}, 'blockHash': '0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b', 'blockNumber': 59, 'result': {'g

</details>
