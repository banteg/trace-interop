# Filter omitted fromblock

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "toBlock": "0x48"
    }
  ]
}
```

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
