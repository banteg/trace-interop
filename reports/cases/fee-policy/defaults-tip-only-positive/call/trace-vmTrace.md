# Defaults tip only positive/call/trace vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Reject the independently invalid call for its fee/funding violation; a defect invalid regardless of state takes precedence. The eth_simulateV1 code is recommended. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Reject this independently invalid fee/funding request before execution.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../../../clients/besu_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../../clients/besu_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "maxPriorityFeePerGas": "0x1",
      "value": "0x7"
    },
    [
      "trace",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. The omitted fee cap defaults to zero, below the supplied priority fee.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H15](../../../../decisions/H15.md): Reject this independently invalid fee/funding request before execution. The omitted fee cap defaults to zero, below the supplied priority fee.

</details>
