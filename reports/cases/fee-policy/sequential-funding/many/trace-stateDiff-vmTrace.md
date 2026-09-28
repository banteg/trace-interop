# Sequential funding/many/trace statediff vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Return one execution envelope per input call, in order. Reject this independently invalid fee/funding request before execution. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../../../clients/anvil_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · a1ce80fb](../../../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · 45912ba3](../../../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-28/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-28/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "to": "0x0000000000000000000000000000000000004444",
          "value": "0x0"
        },
        [
          "trace",
          "stateDiff",
          "vmTrace"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "to": "0x0000000000000000000000000000000000004444",
          "value": "0xde02b6f7625c0c0"
        },
        [
          "trace",
          "stateDiff",
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 1: funds; observed funds with code -32003, which requires -38014. Second call funding must use the post-fee balance of the first call.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 1: funds; observed funds with code -32003, which requires -38014. Second call funding must use the post-fee balance of the first call.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order. H25 owns this error, an error envelope returned as a successful result. There is no executed result to inspect.
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order. H25 owns this error, an error envelope returned as a successful result. There is no executed result to inspect.
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Erigon · 3.8.0-dev · a1ce80fb** (`3.8.0-dev-a1ce80fb`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 1: funds; observed funds with code -32000, which requires -38014. Second call funding must use the post-fee balance of the first call.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.

**Nethermind · 2.1.0-preview · 45912ba3** (`2.1.0-preview+45912ba3`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code; a defect invalid regardless of state takes precedence. Expected call 1: funds; observed funds with code -32000, which requires -38014. Second call funding must use the post-fee balance of the first call.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Second call funding must use the post-fee balance of the first call.

</details>
