# Replay 56

`trace_replayBlockTransactions` · forks · [All reports](../../README.md)

**What this checks:** Block replay has exactly one envelope per frozen transaction, with hashes in transaction order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/forks/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x38",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a8742bfd', 'to': '0xc4f200cb8a874f699'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b347f875eff99958', 'to': '0xc097ce7bc90
- Result shape at `1/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a874f699', 'to': '0xc4f200cb8a875c135'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b347f52eeae14655', 'to': '0xc097ce7bc90
- Result shape at `2/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f200cb8a875c135', 'to': '0xc4f200cb8a876839d'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b347f1e7e5c8f352', 'to': '0xc097ce7bc90

</details>
