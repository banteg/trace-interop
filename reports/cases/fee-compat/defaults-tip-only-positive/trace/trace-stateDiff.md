# Defaults tip only positive/trace/trace statediff

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. Observe unresolved fee defaults. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | RPC error `-32603` | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../../clients/besu_development.md) | RPC error `-32603` | 🟡 Partially assessed | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../../clients/erigon_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../../clients/go-ethereum_trace.md) | RPC error `-32003` | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/observations.json) · [Build/run](../../../../../evidence/2026-09-24/h15-call-compat/fee-compat/manifest.json) |

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
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: base_fee rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: base_fee rejection; trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: priority rejection; trace_call: priority rejection. Omitted/incomplete fee normalization remains open.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: priority rejection; trace_call: priority rejection. Omitted/incomplete fee normalization remains open.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: priority rejection; trace_call: priority rejection. Omitted/incomplete fee normalization remains open.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: base_fee rejection; trace_call: malformed_json.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: base_fee rejection; trace_call: malformed_json.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Output bytes agree. Omitted/incomplete fee normalization remains open.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Output bytes agree. Omitted/incomplete fee normalization remains open.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

</details>
