# Field gas omitted funded eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gasPrice": "0x77359400",
      "input": "0x5a60005260206000f3"
    },
    "latest"
  ]
}
```

</details>
