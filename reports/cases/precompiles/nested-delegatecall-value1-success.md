# Nested delegatecall value1 success

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1",
      "data": "0x600060005260406000608060006006620186a0f45060006000f3"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f9e', 'init': '0x600060005260406000608060006006620186a0f45060006000f3', 'value': '0x1'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x', 'gasUsed': '0x129'}, 'subtraces': 0, 'traceAddress'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f9e', 'init': '0x600060005260406000608060006006620186a0f45060006000f3', 'value': '0x1'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x', 'gasUsed': '0x129'}, 'subtraces': 0, 'traceAddress'

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: ex {"mem": null, "push": ["0x00"], "store": null, "used": 995227} (9 in total).
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x30b4c8fe1629'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34755ccb0391096', 'to': '0xc097ce7bc90715b3472502f4436
- Result shape at `vmTrace`: {'code': '0x600060005260406000608060006006620186a0f45060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995227}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995224}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex

</details>
