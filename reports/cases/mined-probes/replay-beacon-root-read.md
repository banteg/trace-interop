# Replay beacon root read

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. Block-level system writes belong to no transaction’s stateDiff. The reader makes one STATICCALL to the system contract. The vmTrace SSTOREs write the observed success flag and word. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |

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

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H28](../../decisions/H28.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H28](../../decisions/H28.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- [H28](../../decisions/H28.md): The vmTrace SSTOREs write the observed success flag and word. Expected root SSTORE effects [{'key': '0x1', 'val': '0x1'}, {'key': '0x0', 'val': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}], got [{'key': '0x0000000000000000000000000000000000000000000000000000000000000001', 'val': '0x01'}, {'key': '0x0000000000000000000000000000000000000000000000000000000000000000', 'val': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}].
- Result shape at `/`: {'output': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2632e314a000', 'to': '0xa975016a2000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000004788':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- [H28](../../decisions/H28.md): The vmTrace SSTOREs write the observed success flag and word. Expected root SSTORE effects [{'key': '0x1', 'val': '0x1'}, {'key': '0x0', 'val': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}], got [{'key': '0x0000000000000000000000000000000000000000000000000000000000000001', 'val': '0x01'}, {'key': '0x0000000000000000000000000000000000000000000000000000000000000000', 'val': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}].
- Result shape at `/`: {'output': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2632e314a000', 'to': '0xa975016a2000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000004788':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H28](../../decisions/H28.md): The vmTrace SSTOREs write the observed success flag and word. Expected root SSTORE effects [{'key': '0x1', 'val': '0x1'}, {'key': '0x0', 'val': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}], got [None, None].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- [H28](../../decisions/H28.md): The vmTrace SSTOREs write the observed success flag and word. Expected root SSTORE effects [{'key': '0x1', 'val': '0x1'}, {'key': '0x0', 'val': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}], got [None, None].
- Result shape at `/`: {'output': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2632e314a000', 'to': '0xa975016a2000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000004788':

</details>
