# Replay selfdestruct self

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Reward and SELFDESTRUCT records carry result null. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. A pre-existing contract survives SELFDESTRUCT after Cancun with its balance, code and storage, so it has no account diff. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 2 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 2 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x1ea8d660b1000', 'to': '0x219d985fd7800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac483d103a4b8c0', 'to': '0x8ac

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H26](../../decisions/H26.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x1ea8d660b1000', 'to': '0x219d985fd7800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac483d103a4b8c0', 'to': '0x8ac

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x1ea8d660b1000', 'to': '0x219d985fd7800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac483d103a4b8c0', 'to': '0x8ac

</details>
