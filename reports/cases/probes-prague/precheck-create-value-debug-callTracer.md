# Precheck create value debug calltracer

`debug_traceCall` · probes-prague · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "debug_traceCall",
  "params": [
    {
      "data": "0x6460006000f36000526005601b6001f06020526005601b6000f060405260406020f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400"
    },
    "latest",
    {
      "tracer": "callTracer"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
