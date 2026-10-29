# Destroy trace 56

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Reward and SELFDESTRUCT records carry result null. Report the exact deleted balance, code and nonce before Cancun; optional slot deletions match the known zero pre-values. Preserve an existing account after EIP-6780.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 2 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/fork-followup/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/fork-followup/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'idx': '0', 'op': 'PUSH2', 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'idx': '1', 'op': 'SELFDESTRUCT', 'pc': 3, 'sub': None}

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x611008ff', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1008'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 32600, 'ex': {'mem': None, 'push': [], 'store': None, 'used': 546397}, 'pc': 3, 'sub': None}]} is not valid under any of the given schemas

</details>
