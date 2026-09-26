# Transaction create destroy absent

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284"
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H26](../../decisions/H26.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb18', 'input': '0x30ff', 'to': '0x000000000000000000000000000000000000fac0', 'value': '0x100'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'res

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb18', 'input': '0x30ff', 'to': '0x000000000000000000000000000000000000fac0', 'value': '0x100'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'res

</details>
