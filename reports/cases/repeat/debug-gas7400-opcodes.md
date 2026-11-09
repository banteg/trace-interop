# Debug gas7400 opcodes

`debug_traceCall` · repeat · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "debug_traceCall",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001009",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    "0x30",
    {
      "disableMemory": true,
      "disableStorage": true,
      "disableStack": true
    }
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
