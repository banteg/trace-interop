# Field from omitted

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** An omitted from defaults to the zero address, observed by CALLER. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "gas": "0x493e0",
      "input": "0x3360005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER. Depends on H15: The zero-address sender is unfunded, so the call runs only if its fees are zero; an error rejects the fee, not the from default. Observed rpc_error -32603 Internal error.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER. Depends on H15: The zero-address sender is unfunded, so the call runs only if its fees are zero; an error rejects the fee, not the from default. Observed rpc_error -32603 Internal error.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER. Expected ['0x0000000000000000000000000000000000000000000000000000000000000000']; got ['0x']

</details>
