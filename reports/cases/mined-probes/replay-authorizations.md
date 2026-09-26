# Replay authorizations

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. An absent authority is born with creation markers for zero balance, nonce one and its delegation. Tuples that end at the original delegation report no code change, but the nonce advances twice. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0xf078ce84b1ec1497957373e8cbc58cf875e8bf30097658176634414b95adb3b9",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H18](../../decisions/H18.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H18](../../decisions/H18.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H18](../../decisions/H18.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H18](../../decisions/H18.md): Assess the declared property. Cannot inspect this property: unsupported.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0xf078ce84b1ec1497957373e8cbc58cf875e8bf30097658176634414b95adb3b9.
- [H18](../../decisions/H18.md): Tuples fold per authority in order: two valid tuples replace A with B, the stale-nonce tuple is skipped, and the nonce advances once per applied tuple. 0x2b5ad5c4795c026514f8317c7a215e218dccd6cf: expected {'balance': '=', 'code': {'*': {'from': '0x', 'to': '0xef0100000000000000000000000000000000000007702b'}}, 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}, 'storage': {}}, got {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}, 'storage': {}}.
- [H18](../../decisions/H18.md): An absent authority is born with creation markers for zero balance, nonce one and its delegation. 0x6813eb9362372eef6200f3b1dbc3f819671cba69: expected {'balance': {'+': '0x0'}, 'code': {'+': '0xef0100000000000000000000000000000000000007702a'}, 'nonce': {'+': '0x1'}, 'storage': {}}, got {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}, 'storage': {}}.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x2b5ad5c4795c026514f8317c7a215e218dccd6cf; 2 of 3 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef0100000000000000000000000000000000000007702b'}}, 'nonce': {'*': {'from': '0x5', 'to': '0x7'}}}.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x6813eb9362372eef6200f3b1dbc3f819671cba69; 1 of 1 tuples valid; expected {'code': {'+': '0xef0100000000000000000000000000000000000007702a'}, 'nonce': {'+': '0x1'}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x6813eb9362372eef6200f3b1dbc3f819671cba69: new account lacks creation markers for all fields
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x340caa3742000', 'to': '0x439a11a43a000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x1eff47bc3a10a45d4b230b5d10e37751fe6aa718': {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0x3',

</details>
