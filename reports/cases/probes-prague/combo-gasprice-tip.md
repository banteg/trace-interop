# Combo gasprice tip

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "maxPriorityFeePerGas": "0xb2d05e00"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). {'data': '0x3a60005260206000f3', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x493e0', 'gasPrice': '0x77359400', 'maxPriorityFeePerGas': '0xb2d05e00'} should not be valid under {'anyOf': [{'properties': {'maxFeePerGas': {'not': {'type': 'null'}}}, 'required': ['maxFeePerGas']}, {'properties': {'maxPriorityFeePerGas': {'not': {'type': 'null'}}}, 'required': ['maxPriorityFeePerGas']}], 'properties': {'gasPrice': {'not': {'type': 'null'}}}, 'required': ['gasPrice']}. Code -32603 (-32602 recommended).
- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). Observed rpc_error -32603: Internal error (-32602 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). {'data': '0x3a60005260206000f3', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x493e0', 'gasPrice': '0x77359400', 'maxPriorityFeePerGas': '0xb2d05e00'} should not be valid under {'anyOf': [{'properties': {'maxFeePerGas': {'not': {'type': 'null'}}}, 'required': ['maxFeePerGas']}, {'properties': {'maxPriorityFeePerGas': {'not': {'type': 'null'}}}, 'required': ['maxPriorityFeePerGas']}], 'properties': {'gasPrice': {'not': {'type': 'null'}}}, 'required': ['gasPrice']}
- [H14](../../decisions/H14.md): gasPrice with maxFeePerGas or maxPriorityFeePerGas is a fee combination no call can carry, so the call is rejected (-32602 recommended). Observed result with output 0x0000000000000000000000000000000000000000000000000000000077359400

</details>
