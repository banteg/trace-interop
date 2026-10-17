# Call mixed create

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/a/manifest.json) |

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

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0]: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [1]: creationMethod null
- Result shape at `trace/1`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x83739', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xea91ad16d2b6ec90fe255a49dfd6e2f47304de88', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,
- Result shape at `trace/2`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x7b44f', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x30b44c7249bb3959e686a86b65ccdb4c643c2750', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0]: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [1]: creationMethod null
- Result shape at `trace/1`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x83739', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xea91ad16d2b6ec90fe255a49dfd6e2f47304de88', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,
- Result shape at `trace/2`: {'action': {'from': '0x0000000000000000000000000000000000001006', 'gas': '0x7b44f', 'init': '0x600a61000d600039600a6000f3602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x30b44c7249bb3959e686a86b65ccdb4c643c2750', 'code': '0x602a60005260206000f3', 'gasUsed': '0x7e8'}, 'subtraces': 0,

</details>
