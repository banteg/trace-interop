# Combo type0 dynamic

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/blob-cap/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/blob-cap/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "maxFeePerGas": "0xb2d05e00",
      "maxPriorityFeePerGas": "0xb2d05e00",
      "type": "0x0"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c45e', 'init': '0x3a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000b2d05e00', 'gasUsed': '0x1911'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c45e', 'init': '0x3a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000b2d05e00', 'gasUsed': '0x1911'},

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. Expected a result; observed rpc_error -32602 dynamic fee fields require transaction type 2 or later

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x0000000000000000000000000000000000000000000000000000000000000000']

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The call runs with type 0, which does not change execution, at GASPRICE 3000000000, from its dynamic fee caps. Expected ['0x00000000000000000000000000000000000000000000000000000000b2d05e00']; got ['0x0000000000000000000000000000000000000000000000000000000000000000']

</details>
