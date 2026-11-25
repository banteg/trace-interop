# Debug siblings revert ok

`debug_traceCall` · repeat · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | Object returned | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |

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

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H24](../../decisions/H24.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
