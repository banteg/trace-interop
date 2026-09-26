# Call mixed create

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |

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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x83739', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xea91ad16d2b6ec90fe255a49dfd6e2f47304de88', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,
- Result shape at `trace/2`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x7b44f', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x30b44c7249bb3959e686a86b65ccdb4c643c2750', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x83739', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xea91ad16d2b6ec90fe255a49dfd6e2f47304de88', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,
- Result shape at `trace/2`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x7b44f', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x30b44c7249bb3959e686a86b65ccdb4c643c2750', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 2: ex {"mem": null, "push": ["0x001b"], "store": null, "used": 578994} (16 in total).
- Result shape at `vmTrace`: {'code': '0x601761001b600039601760006000f050607b601760006000f55000600a61000d600039600a6000f3602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x17'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x001b'], 'store': None, 'used

</details>
