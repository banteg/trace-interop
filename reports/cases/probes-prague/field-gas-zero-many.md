# Field gas zero many

`trace_callMany` · probes-prague · [All reports](../../README.md)

**What this checks:** A trace_callMany item with an explicit gas of 0 fails the intrinsic-gas check, so the whole request is rejected (-38013 recommended) with no partial results. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-38013` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-38013` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |

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
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x0",
          "input": "0x5a60005260206000f3"
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

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../decisions/H15.md): A trace_callMany item with an explicit gas of 0 fails the intrinsic-gas check, so the whole request is rejected (-38013 recommended) with no partial results. Observed result with output {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'}
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../decisions/H15.md): A trace_callMany item with an explicit gas of 0 fails the intrinsic-gas check, so the whole request is rejected (-38013 recommended) with no partial results. Observed result with output {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'}
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
