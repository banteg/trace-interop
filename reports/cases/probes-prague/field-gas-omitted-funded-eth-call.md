# Field gas omitted funded eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |

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

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Cap GAS word 0x0000000000000000000000000000000000000000000000000000000002fa20fc; got 0x0000000000000000000000000000000000000000000000000000000005f5117c

</details>
