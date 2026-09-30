# Replay block 4

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. A pre-existing contract survives SELFDESTRUCT after Cancun with its balance, code and storage, so it has no account diff. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. An account created and destroyed in one transaction is absent at both endpoints and has no account diff. The factory forwards the value it received, so only its nonce changes. A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x4",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x1ea8d660b1000', 'to': '0x219d985fd7800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac483d103a4b8c0', 'to': '0x8a

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x1ea8d660b1000', 'to': '0x219d985fd7800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac483d103a4b8c0', 'to': '0x8a

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H26](../../decisions/H26.md): A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. 0xedd09273eb6f5c2fcfb36f667405c3869a71bebb: expected {'balance': {'-': '0x1388'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x1388', 'to': None}}, 'code': '=', 'nonce': {'*': {'from': '0x0', 'to': None}}, 'storage': {}}.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=58067 (independent receipt), price=2586633408, expected tip=2000000000/gas, burn=586633408/gas, blob fee and destroyed wei=5256.
- Result shape at `/`: [{'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x1ea8d660b1000', 'to': '0x219d985fd7800'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': {'*': {'from': '0x8ac483d103a4b8c0', 'to': '0x8a

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

</details>
