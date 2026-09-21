# Constructor

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Creation vmTrace.code is executing initcode. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-repeat/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; nonempty output | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x60016000526001601ff3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x01'], 'store': None, 'used': 546847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 546844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x60016000526001601ff3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x01'], 'store': None, 'used': 546847}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 546844}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H19](../../decisions/H19.md): Creation vmTrace.code is executing initcode.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H19](../../decisions/H19.md): Creation vmTrace.code is executing initcode.

</details>
