# Replay history read

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. Block-level system writes belong to no transaction’s stateDiff. The reader makes one STATICCALL to the system contract. The vmTrace SSTOREs write the observed success flag and word. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x5bff67694ccfbfa88f7d81a185ee437e5b484809505cc49446810603b5f823f2",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (56 in total).
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Expected 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d, got 0x0000000000000000000000000000000000000000000000000000000000000000.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. 0x0000000000000000000000000000000000002935: expected {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d'}}, '0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}, got {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): The vmTrace SSTOREs write the observed success flag and word. Expected root SSTORE effects [('0x1', '0x1'), ('0x0', '0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d')], got [('0x1', '0x1'), ('0x0', '0x0')].
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=70071 (independent receipt), price=2765670938, expected tip=2000000000/gas, burn=765670938/gas, blob fee and destroyed wei=0.
- Result shape at `/`: {'output': '0x0000000000000000000000000000000000000000000000000000000000000000', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x816901b22000', 'to': '0xdcabb2f63c00'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000002935':

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H28](../../decisions/H28.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (56 in total).
- Result shape at `/`: {'output': '0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa975016a2000', 'to': '0x128ea5b8aec00'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000002935'

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (56 in total).
- Result shape at `/`: {'output': '0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xa975016a2000', 'to': '0x128ea5b8aec00'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000002935'

</details>
