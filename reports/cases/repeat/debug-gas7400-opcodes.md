# Debug gas7400 opcodes

`debug_traceCall` · repeat · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-26/anvil/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/repeat/manifest.json) |

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

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
