# Debug mixed create

`debug_traceCall` · repeat · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Anvil · 1.8.6-nightly · 32624734](../../clients/anvil_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Besu · 26.10-develop · d05d8e74](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 1d3ebbf2](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · 204457ad](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 1a4dbbe1](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-11/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-11/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "debug_traceCall",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001006",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    "0x30",
    {
      "tracer": "callTracer"
    }
  ]
}
```

**Anvil · 1.8.6-nightly · 32624734** (`anvil Version: 1.8.6-nightly+32624734`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · d05d8e74** (`besu/v26.10-develop-d05d8e7/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 1d3ebbf2** (`3.8.0-dev-1d3ebbf2`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 204457ad** (`2.2.0-preview+204457ad`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 1a4dbbe1** (`Reth Version: 2.7.0+1a4dbbe1`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H10](../../decisions/H10.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
