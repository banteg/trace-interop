# Replay beacon root read

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. Block-level system writes belong to no transaction’s stateDiff. The reader makes one STATICCALL to the system contract. The vmTrace SSTOREs write the observed success flag and word. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Each completed SSTORE reports its store {key, val}.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0xf6fb42057650e021027fc81457375b2bcc6f4b01e40b3f02e3df48ed2d65ab36",
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
- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H28](../../decisions/H28.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H28](../../decisions/H28.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x0000000000000014"], "store": null, "used": 178998} (27 in total).
- Result shape at `/`: {'output': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2632e314a000', 'to': '0xa975016a2000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000004788':

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0xf6fb42057650e021027fc81457375b2bcc6f4b01e40b3f02e3df48ed2d65ab36.
- [H20](../../decisions/H20.md): Each completed SSTORE reports its store {key, val}. SSTORE at pc [34, 38] reported no store, so the root writes cannot show the H28 values.
- Result shape at `/`: {'output': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2632e314a000', 'to': '0xa975016a2000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000004788':

</details>
