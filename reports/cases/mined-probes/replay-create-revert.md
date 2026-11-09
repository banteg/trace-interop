# Replay create revert

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. A reverted top-level CREATE is one failed create frame. A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. Replay output carries the revert bytes. The would-be address of a reverted CREATE is absent at both endpoints and has no account diff. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x3f1603f033127b94711dc5a0ab4250a34c8dcb8f041f2304fe16c4be34e4e1bb",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): Replay output carries the revert bytes. Expected 0xdeadbeef, got 0x.
- Result shape at `/`: {'output': '0x', 'revertReason': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (6 in total).
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

</details>
