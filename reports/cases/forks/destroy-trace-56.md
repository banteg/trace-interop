# Destroy trace 56

`trace_call` · forks · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Reward and SELFDESTRUCT records carry result null. Report the exact deleted balance, code and nonce before Cancun; optional slot deletions match the known zero pre-values. Preserve an existing account after EIP-6780.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/forks/manifest.json) |

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
    "0x38"
  ]
}
```

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'idx': '0', 'op': 'PUSH2', 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'idx': '1', 'op': 'SELFDESTRUCT', 'pc': 3, 'sub': None}

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

</details>
