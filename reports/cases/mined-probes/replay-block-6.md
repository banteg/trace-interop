# Replay block 6

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. An absent authority is born with creation markers for zero balance, nonce one and its delegation. Tuples that end at the original delegation report no code change, but the nonce advances twice. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x6",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H18](../../decisions/H18.md): Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. 0x2b5ad5c4795c026514f8317c7a215e218dccd6cf: expected {'balance': '=', 'code': {'*': {'from': '0x', 'to': '0xef0100000000000000000000000000000000000007702b'}}, 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}, 'storage': {}}, got {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}, 'storage': {}}.
- [H18](../../decisions/H18.md): An absent authority is born with creation markers for zero balance, nonce one and its delegation. 0x6813eb9362372eef6200f3b1dbc3f819671cba69: expected {'balance': {'+': '0x0'}, 'code': {'+': '0xef0100000000000000000000000000000000000007702a'}, 'nonce': {'+': '0x1'}, 'storage': {}}, got {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}, 'storage': {}}.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x2b5ad5c4795c026514f8317c7a215e218dccd6cf; 2 of 3 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef0100000000000000000000000000000000000007702b'}}, 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}}.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x6813eb9362372eef6200f3b1dbc3f819671cba69; 1 of 1 tuples valid; expected {'code': {'+': '0xef0100000000000000000000000000000000000007702a'}, 'nonce': {'+': '0x1'}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x6813eb9362372eef6200f3b1dbc3f819671cba69: new account lacks creation markers for all fields

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H18](../../decisions/H18.md): Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. 0x2b5ad5c4795c026514f8317c7a215e218dccd6cf: expected {'balance': '=', 'code': {'*': {'from': '0x', 'to': '0xef0100000000000000000000000000000000000007702b'}}, 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}, 'storage': {}}, got {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}, 'storage': {}}.
- [H18](../../decisions/H18.md): An absent authority is born with creation markers for zero balance, nonce one and its delegation. 0x6813eb9362372eef6200f3b1dbc3f819671cba69: expected {'balance': {'+': '0x0'}, 'code': {'+': '0xef0100000000000000000000000000000000000007702a'}, 'nonce': {'+': '0x1'}, 'storage': {}}, got {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}, 'storage': {}}.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x2b5ad5c4795c026514f8317c7a215e218dccd6cf; 2 of 3 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef0100000000000000000000000000000000000007702b'}}, 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}}.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x6813eb9362372eef6200f3b1dbc3f819671cba69; 1 of 1 tuples valid; expected {'code': {'+': '0xef0100000000000000000000000000000000000007702a'}, 'nonce': {'+': '0x1'}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x6813eb9362372eef6200f3b1dbc3f819671cba69: new account lacks creation markers for all fields

</details>
