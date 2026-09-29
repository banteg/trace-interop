# Block 4

`trace_block` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. SELFDESTRUCT emits one suicide frame under the call. The suicide frame records the contract’s whole balance transferred to itself. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 9 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 8 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 8 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 8 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x4"
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x000000000000000000000000000000000000de57', 'value': '0x0'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'result':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x000000000000000000000000000000000000de57', 'value': '0x0'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'result':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x000000000000000000000000000000000000de57', 'value': '0x0'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'result':

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H26](../../decisions/H26.md): The suicide frame records the contract’s whole balance transferred to itself. suicide [0]: action.address 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57; action.balance 0x0 != 0x3e8; action.refundAddress 0x0000000000000000000000000000000000000000 != 0x000000000000000000000000000000000000de57

</details>
