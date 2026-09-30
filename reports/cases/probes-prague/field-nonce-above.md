# Field nonce above

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. A supplied nonce 13 is ignored: the creation runs at the address of state nonce 10.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3060005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "nonce": "0xd"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A supplied nonce 13 is ignored: the creation runs at the address of state nonce 10. Expected a result; observed rpc_error -32603 Internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A supplied nonce 13 is ignored: the creation runs at the address of state nonce 10. Expected a result; observed rpc_error -32603 Internal error

</details>
