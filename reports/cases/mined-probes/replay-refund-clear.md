# Replay refund clear

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The storage program is one call frame. Root gasUsed is execution gas before the refund (5004, refund 4800, receipt 21204). Cleared slots change from their genesis values to zero. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x6c9c863f8bedabd9d2b96c9f1582c133b0eeaa83343a29c6ad72d77ba46b297a",
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
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H19](../../decisions/H19.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H19](../../decisions/H19.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2ed18a19f7000', 'to': '0x313aa83660000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000005501': {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x00

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2ed18a19f7000', 'to': '0x313aa83660000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000005501': {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x00

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH0) used: expected 178998, got 179000; step 0 (PUSH0) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH0) used: expected 178996, got 178998; step 1 (PUSH0) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH0) used: expected 178998, got 179000; step 0 (PUSH0) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH0) used: expected 178996, got 178998; step 1 (PUSH0) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover, subtraces appear only on calls and creations, MLOAD and call mem cover their operand range, and RETURN/REVERT report no mem. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2ed18a19f7000', 'to': '0x313aa83660000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000005501': {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x00

</details>
