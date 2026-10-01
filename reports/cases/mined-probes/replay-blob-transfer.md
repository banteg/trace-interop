# Replay blob transfer

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. An absent account funded by the transaction is born with balance, zero nonce and empty code markers. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

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
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x000000000000000000000000000000000000b10b: new account lacks creation markers for all fields
- Result shape at `/`: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x2632e314a000'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x000000000000000000000000000000000000b10b': {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f455

</details>
