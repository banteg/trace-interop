# Nested callcode value1 success

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. Successful creation uses address, code and gasUsed. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/precompiles/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6000600052604060006080600060016006620186a0f25060006000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1"
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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f25060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995195}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995192}, 'pc': 2, 'sub': None}, {'cost': 6,

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f25060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995195}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995192}, 'pc': 2, 'sub': None}, {'cost': 6,

</details>
