# Precheck create value debug calltracer

`debug_traceCall` · probes-prague · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | nonempty output | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |

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

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H29](../../decisions/H29.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
