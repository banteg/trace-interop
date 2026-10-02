# Mixed typed invalid then free/many/trace vmtrace

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Reject this independently invalid fee/funding request before execution. Identify a fee/funding validation rejection. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. A supplied error.data.index must identify the failing decoded item; the field is recommended. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../../../clients/anvil_release.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../../../clients/anvil_development.md) | 2 records | ⚠️ Differs | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../../../clients/erigon_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../../clients/go-ethereum_trace.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../../../clients/nethermind_development.md) | RPC error `-38012` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |

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
          "maxPriorityFeePerGas": "0x0",
          "value": "0x7"
        },
        [
          "trace",
          "vmTrace"
        ]
      ],
      [
        {
          "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "maxFeePerGas": "0x0",
          "maxPriorityFeePerGas": "0x0",
          "value": "0x7"
        },
        [
          "trace",
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. A free call does not exempt another call from fee validation.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. A free call does not exempt another call from fee validation.

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Identify a fee/funding validation rejection. A generic/internal/crash error does not prove validation: internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../../../decisions/H16.md): Return one execution envelope per input call, in order. H25 owns this error, an error envelope returned as a successful result. There is no executed result to inspect.
- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. A free call does not exempt another call from fee validation.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
