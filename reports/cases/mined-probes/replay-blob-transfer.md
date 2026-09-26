# Replay blob transfer

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. An absent account funded by the transaction is born with balance, zero nonce and empty code markers. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x5fda3be60b37afa7b2c35c3710704c359acec12ed4d0744565663d1e96d02089",
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
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x000000000000000000000000000000000000b10b: expected {'balance': {'+': '0x7'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}.
- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x0000000000000000000000000000000000000000: expected {'balance': {'+': '0x2632e314a000'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'+': '0x2632e314a000'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x000000000000000000000000000000000000b10b: new account lacks creation markers for all fields
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x2632e314a000'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x000000000000000000000000000000000000b10b': {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f455

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x5fda3be60b37afa7b2c35c3710704c359acec12ed4d0744565663d1e96d02089.
- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x000000000000000000000000000000000000b10b: expected {'balance': {'+': '0x7'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x0', 'to': '0x7'}}, 'code': '=', 'nonce': '=', 'storage': {}}.
- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x0000000000000000000000000000000000000000: expected {'balance': {'+': '0x2632e314a000'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x0', 'to': '0x2632e314a000'}}, 'code': '=', 'nonce': '=', 'storage': {}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x000000000000000000000000000000000000b10b: new account lacks creation markers for all fields
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x0', 'to': '0x2632e314a000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000b10b': {'balance': {'*': {'from': '0x0', 'to': '0x7'}}, 'code': '=', 'nonce': '='

</details>
