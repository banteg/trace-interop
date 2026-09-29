# Field gas cap eth call

`eth_call` · probes-prague · [All reports](../../README.md)

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000ffffffffffff307b` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000ffffffffffff307b` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0xffffffffffffffff",
      "gasPrice": "0x0",
      "input": "0x5a60005260206000f3"
    },
    "latest"
  ]
}
```

</details>
