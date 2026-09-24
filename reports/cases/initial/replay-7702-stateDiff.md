# Replay 7702 statediff

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The method responds without Method not found (-32601). Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0xb54bc1221b206db9ee0449a716ddde73c1e2d0f72d2e789fcb51230fe851cc8a",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H08](../../decisions/H08.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H18](../../decisions/H18.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H08](../../decisions/H08.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H18](../../decisions/H18.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- Result shape at `/`: {'output': None, 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x718ba', 'to': '0x7a87a'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34a455f328dfca1', 'to': '0xc097c

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0xeda8645ba6948855e3b3cd596bbb07596d59c603; 1 of 1 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef01004055cae5c7d838cda10d40f9d07106c7f5f3be1c'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0xeda8645ba6948855e3b3cd596bbb07596d59c603; 1 of 1 tuples valid; expected {'code': {'*': {'from': '0x', 'to': '0xef01004055cae5c7d838cda10d40f9d07106c7f5f3be1c'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}.
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x718ba', 'to': '0x7a87a'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34a455f328dfca1', 'to': '0xc097c

</details>
