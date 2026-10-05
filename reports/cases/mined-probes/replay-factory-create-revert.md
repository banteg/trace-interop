# Replay factory create revert

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. The factory call contains its failed nested create frame. The handled nested failure leaves the root successful; root gasUsed is its execution gas, action.gas excludes intrinsic gas. A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. The would-be address of a reverted nested CREATE has no account diff. The creator’s nonce increment survives its child’s REVERT. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H17](../../decisions/H17.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result {'address': '0xd8353791c13be48589d7247c3284625edca5aa72', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0x0000000000000000000000000000000000000000000000000000000000000000', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x189b4a90c8800', 'to': '0x1ea8d660b1000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0x0000000000000000000000000000000000000000000000000000000000000000', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x189b4a90c8800', 'to': '0x1ea8d660b1000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result {'address': '0xd8353791c13be48589d7247c3284625edca5aa72', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0x0000000000000000000000000000000000000000000000000000000000000000', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x189b4a90c8800', 'to': '0x1ea8d660b1000'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000fac0

</details>
