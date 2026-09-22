# Call many transfers

`trace_callMany` · initial · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-23/geth-40eecf3-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 2 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

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
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001234",
          "value": "0x1"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001234",
          "value": "0x1"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "0x30"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-40eecf36-2026-09-23/linux-amd64/go1.26.1`)

- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H15](../../decisions/H15.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
