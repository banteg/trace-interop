# Field gas omitted eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | `0x0000000000000000000000000000000000000000000000000000000005f5117c` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "input": "0x5a60005260206000f3"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 759efed7** (`2.2.0-preview+759efed7`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
