# Field gas zero

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | RPC error `-38013` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-38013` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | RPC error `-38013` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x0",
      "input": "0x5a60005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. Observed rpc_error -32603: Internal error (-38013 recommended)

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
