# Filter omitted fromblock

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 3 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 355 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | 🔎 Control / not applicable; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 2 records | 🔎 Control / not applicable | [Response](../../../evidence/2026-09-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-forks/manifest.json) |

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

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 558586f0** (`3.8.0-dev-558586f0`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: 'transactionHash' is a required property
- Result shape at `0`: 'transactionPosition' is a required property
- Result shape at `4`: 'transactionHash' is a required property
- Result shape at `4`: 'transactionPosition' is a required property
- Result shape at `8`: 'transactionHash' is a required property
- Result shape at `8`: 'transactionPosition' is a required property
- Result shape at `10`: 'transactionHash' is a required property
- Result shape at `10`: 'transactionPosition' is a required property

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · 82516987** (`2.1.0-preview+82516987`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
