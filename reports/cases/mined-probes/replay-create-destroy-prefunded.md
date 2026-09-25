# Replay create destroy prefunded

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. A deleted account reports storage {}; its account deletion implies every slot is wiped. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. The factory forwards the value it received, so only its nonce changes. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 3 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H26](../../decisions/H26.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H26](../../decisions/H26.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x00000002"], "store": null, "used": 178966} (8 in total).
- [H26](../../decisions/H26.md): A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. 0xedd09273eb6f5c2fcfb36f667405c3869a71bebb: expected {'balance': {'-': '0x1388'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x1388', 'to': None}}, 'code': '=', 'nonce': {'*': {'from': '0x0', 'to': None}}, 'storage': {}}.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=58067 (independent receipt), price=2586633408, expected tip=2000000000/gas, burn=586633408/gas, blob fee and destroyed wei=5256.
- Result shape at `/`: {'output': '0x000000000000000000000000edd09273eb6f5c2fcfb36f667405c3869a71bebb', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2837913ce7400', 'to': '0x2ed18a19f7000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H26](../../decisions/H26.md): A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. 0xedd09273eb6f5c2fcfb36f667405c3869a71bebb: expected {'balance': {'-': '0x1388'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'storage': {}}, got None.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=58067 (independent receipt), price=2586633408, expected tip=2000000000/gas, burn=586633408/gas, blob fee and destroyed wei=5256.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x39a96f08f95087d62771192efeea4c13841e76d88ff6c7dea89f12fa1358114b.
- [H26](../../decisions/H26.md): A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. 0xedd09273eb6f5c2fcfb36f667405c3869a71bebb: expected {'balance': {'-': '0x1388'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'storage': {}}, got None.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=58067 (independent receipt), price=2586633408, expected tip=2000000000/gas, burn=586633408/gas, blob fee and destroyed wei=5256.
- Result shape at `/`: {'output': '0x000000000000000000000000edd09273eb6f5c2fcfb36f667405c3869a71bebb', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x2837913ce7400', 'to': '0x2ed18a19f7000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

</details>
