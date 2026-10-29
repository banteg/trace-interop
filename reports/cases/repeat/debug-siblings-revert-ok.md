# Debug siblings revert ok

`debug_traceCall` · repeat · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "debug_traceCall",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001005",
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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
