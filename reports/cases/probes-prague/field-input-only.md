# Field input only

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. input alone supplies the initcode, which returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "input": "0x602a60005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000000000000000000000000000002a', 'gasUsed': '0x1912'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000000000000000000000000000002a', 'gasUsed': '0x1912'

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): input alone supplies the initcode, which returns word 42. Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x']

</details>
