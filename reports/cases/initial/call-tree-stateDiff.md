# Call tree statediff

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

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
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- Result shape at `output`: None is not of type 'string'

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- Result shape at `output`: None is not of type 'string'

</details>
