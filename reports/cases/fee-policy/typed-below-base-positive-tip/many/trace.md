# Typed below base positive tip/many/trace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Reject this independently invalid fee/funding request before execution. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../../../clients/anvil_development.md) | 1 records | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-policy/manifest.json) |

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
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "maxFeePerGas": "0x2da282a7",
          "maxPriorityFeePerGas": "0x1",
          "value": "0x7"
        },
        [
          "trace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order.
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. Positive cap/price below BASEFEE or priority cap above total cap.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee; observed base_fee with code -32000, which requires -38012. Positive cap/price below BASEFEE or priority cap above total cap.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee; observed base_fee with code -32000, which requires -38012. Positive cap/price below BASEFEE or priority cap above total cap.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee; observed base_fee with code -32000, which requires -38012. Positive cap/price below BASEFEE or priority cap above total cap.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Reject the independently invalid call for its fee/funding violation, with its eth_simulateV1 error code. Expected call 0: base_fee; observed base_fee with code -32000, which requires -38012. Positive cap/price below BASEFEE or priority cap above total cap.

</details>
