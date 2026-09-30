# Field from omitted zero fee

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. An omitted from defaults to the zero address, observed by CALLER, on an explicitly zero-fee call.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
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
      "data": "0x3360005260206000f3",
      "gas": "0x493e0",
      "gasPrice": "0x0"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER, on an explicitly zero-fee call. Depends on H15: The zero-address sender is unfunded, so the call runs only if its fees are zero; an error rejects the fee, not the from default. Observed rpc_error -32603 Internal error.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER, on an explicitly zero-fee call. Depends on H15: The zero-address sender is unfunded, so the call runs only if its fees are zero; an error rejects the fee, not the from default. Observed rpc_error -32603 Internal error.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER, on an explicitly zero-fee call. Depends on H15: The zero-address sender is unfunded, so the call runs only if its fees are zero; an error rejects the fee, not the from default. Observed rpc_error -32000 fee cap less than block base fee: address <nil>, feeCap: 0 baseFee: 765625000.

</details>
