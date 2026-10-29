# Replay create destroy prefunded

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Reward and SELFDESTRUCT records carry result null. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. The factory forwards the value it received, so only its nonce changes. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Assess this declared topic case. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x39a96f08f95087d62771192efeea4c13841e76d88ff6c7dea89f12fa1358114b",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H26](../../decisions/H26.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H26](../../decisions/H26.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (15 in total).
- Result shape at `/`: {'output': '0x000000000000000000000000edd09273eb6f5c2fcfb36f667405c3869a71bebb', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2837913ce7400', 'to': '0x2ed18a19f7000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (15 in total).
- Result shape at `/`: {'output': '0x000000000000000000000000edd09273eb6f5c2fcfb36f667405c3869a71bebb', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2837913ce7400', 'to': '0x2ed18a19f7000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

</details>
