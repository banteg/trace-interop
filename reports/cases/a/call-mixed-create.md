# Call mixed create

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001006",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x83739', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xea91ad16d2b6ec90fe255a49dfd6e2f47304de88', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,
- Result shape at `trace/2`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x7b44f', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x30b44c7249bb3959e686a86b65ccdb4c643c2750', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x83739', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xea91ad16d2b6ec90fe255a49dfd6e2f47304de88', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,
- Result shape at `trace/2`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x7b44f', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x30b44c7249bb3959e686a86b65ccdb4c643c2750', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x601761001b600039601760006000f050607b601760006000f55000600a61000d600039600a6000f3602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x17'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x001b'], 'store': None, 'used

</details>
