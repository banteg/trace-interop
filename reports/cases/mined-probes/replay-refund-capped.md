# Replay refund capped

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The storage program is one call frame. Root gasUsed is execution gas before the refund (10009, refund 9600, receipt 24808). Cleared slots change from their genesis values to zero. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Assess this declared topic case. trace_replayTransaction Assess the declared property.

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
    "0xaab516a3fb838f33cf12da5aaa74a59d6a192d6f74524e0717bcc5a3b2e3b13e",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H19](../../decisions/H19.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H20](../../decisions/H20.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H19](../../decisions/H19.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H19](../../decisions/H19.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H20](../../decisions/H20.md): Assess the declared property. Cannot inspect this property: unsupported.

</details>
