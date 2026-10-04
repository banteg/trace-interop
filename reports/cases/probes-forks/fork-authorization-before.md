# Fork authorization before

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "authorizationList": [
        {
          "address": "0x00000000000000000000000000000000000000ee",
          "chainId": "0xc72dd9d5e883e",
          "nonce": "0x0",
          "r": "0x86af3a52abd32c04ce6704ee2710dab8447f7af79930e97d893a2ec773c02964",
          "s": "0x4043b2933aefee93438b1a0599d16ee5f806844140a43d4883e5a2f99423862b",
          "yParity": "0x1"
        }
      ],
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    [
      "trace"
    ],
    "0x3b"
  ]
}
```

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). Observed rpc_error -32603: Internal error (-32003 recommended)

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). Observed result with output 0x

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H14](../../decisions/H14.md): The authorization fields at block 59, before Prague (block 60) name a feature not active at the selected block, so the call is rejected (-32003 recommended). Observed rpc_error -32603: Internal error (-32003 recommended)

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H14](../../decisions/H14.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
