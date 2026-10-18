# Replay blob transfer

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. An absent account funded by the transaction is born with balance, zero nonce and empty code markers. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Assess this declared topic case. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

</details>
