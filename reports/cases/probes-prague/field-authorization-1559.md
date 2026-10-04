# Field authorization 1559

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. A valid authorization on an EIP-1559-priced call delegates key 1 to the marker contract, which returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "authorizationList": [
        {
          "address": "0x0000000000000000000000000000000000001002",
          "chainId": "0xc72dd9d5e883e",
          "nonce": "0xa",
          "r": "0x4e9c1a2430ff1f88a19f6567e51648c181b00616b4adcff8548b9785e3898814",
          "s": "0x707840665ae678f4933987814326a609a2ddb271ed461970ad744c0aae11779f",
          "yParity": "0x0"
        }
      ],
      "data": "0x",
      "from": "0x0c2c51a0990aee1d73c1228de158688341557508",
      "gas": "0x493e0",
      "maxFeePerGas": "0x77359400",
      "maxPriorityFeePerGas": "0x77359400",
      "to": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): A valid authorization on an EIP-1559-priced call delegates key 1 to the marker contract, which returns word 42. Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x']

</details>
