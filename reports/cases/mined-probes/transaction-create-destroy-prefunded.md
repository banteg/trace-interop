# Transaction create destroy prefunded

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x39a96f08f95087d62771192efeea4c13841e76d88ff6c7dea89f12fa1358114b"
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb18', 'input': '0x30ff', 'to': '0x000000000000000000000000000000000000fac0', 'value': '0x100'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'res

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H26](../../decisions/H26.md): The creation succeeds with empty code before destroying itself. create [0]: result {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'gasUsed': '0x138a', 'output': '0x'} != {'address': '0xedd09273eb6f5c2fcfb36f667405c3869a71bebb', 'code': '0x', 'gasUsed': '0x138a'}
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb18', 'input': '0x30ff', 'to': '0x000000000000000000000000000000000000fac0', 'value': '0x100'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'res

</details>
