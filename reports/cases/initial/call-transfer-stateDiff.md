# Call transfer statediff

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 0 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 0 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 0 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-23/geth-40eecf3-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

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
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001234",
      "value": "0x1"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H08](../../decisions/H08.md): Unrequested trace is an empty array.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `output`: None is not of type 'string'

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `output`: None is not of type 'string'

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-40eecf36-2026-09-23/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
