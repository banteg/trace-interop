# Call destroy

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Reward and SELFDESTRUCT records carry result null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001007",
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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'idx': '0', 'op': 'PUSH2', 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'idx': '1', 'op': 'SELFDESTRUCT', 'pc': 3, 'sub': None}

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'idx': '0', 'op': 'PUSH2', 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'idx': '1', 'op': 'SELFDESTRUCT', 'pc': 3, 'sub': {'cod

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

</details>
