# Replay block 4

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. A pre-existing contract survives SELFDESTRUCT after Cancun with its balance, code and storage, so it has no account diff. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. An account created and destroyed in one transaction is absent at both endpoints and has no account diff. The factory forwards the value it received, so only its nonce changes. A prefunded address destroyed in its creating transaction is a deletion: - markers for its pre-state and storage {}. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `1/trace/1`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x23509', 'init': '0x30ff', 'value': '0x100'}, 'result': {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [0], 'type':
- Result shape at `2/trace/1`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x23509', 'init': '0x30ff', 'value': '0x100'}, 'result': {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [0], 'type':

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `1/trace/1`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x23509', 'init': '0x30ff', 'value': '0x100'}, 'result': {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [0], 'type':
- Result shape at `2/trace/1`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x23509', 'init': '0x30ff', 'value': '0x100'}, 'result': {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [0], 'type':

</details>
