# Replay create revert

`trace_replayTransaction` · mined-probes · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. A reverted top-level CREATE is one failed create frame. A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. Replay output carries the revert bytes. The would-be address of a reverted CREATE is absent at both endpoints and has no account diff. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/mined-probes/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

**Nethermind · 2.1.0-preview · b4211ad9** (`2.1.0-preview+b4211ad9`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 5: ex {"mem": null, "push": ["0x00"], "store": null, "used": 146801} (2 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x3f1603f033127b94711dc5a0ab4250a34c8dcb8f041f2304fe16c4be34e4e1bb.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `/`: {'output': '0xdeadbeef', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x128ea5b8aec00', 'to': '0x189b4a90c8800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac586582972c6a3', 'to'

</details>
