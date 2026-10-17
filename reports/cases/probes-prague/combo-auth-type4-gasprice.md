# Combo auth type4 gasprice

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |

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
      "gasPrice": "0x77359400",
      "to": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "type": "0x4"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x']

</details>
