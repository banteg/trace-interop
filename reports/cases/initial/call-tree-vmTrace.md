# Call tree vmtrace

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-geth-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-geth-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; nonempty output | Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; nonempty output | Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x0",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
    },
    [
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-40eecf36-2026-09-23/linux-amd64/go1.26.1`)

- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H21](../../decisions/H21.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H20](../../decisions/H20.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
