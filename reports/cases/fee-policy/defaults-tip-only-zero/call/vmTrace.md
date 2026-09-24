# Defaults tip only zero/call/vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Observe unresolved fee defaults. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | RPC error `-32603` | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../../clients/besu_development.md) | RPC error `-32603` | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../../clients/erigon_development.md) | 0 call frames; nonempty output | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 0 call frames; nonempty output | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 0 call frames; nonempty output | ❔ Policy open | [Response](../../../../../evidence/2026-09-24/current-matrix/fee-policy/observations.json) · [Build/run](../../../../../evidence/2026-09-24/current-matrix/fee-policy/manifest.json) |

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
      "maxPriorityFeePerGas": "0x0",
      "value": "0x7"
    },
    [
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../../../decisions/H08.md): Unrequested trace is an empty array.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H21](../../../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.
- Result shape at `vmTrace`: {'code': '0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3', 'ops': [{'cost': 2, 'ex': {'mem': None, 'push': ['0x0000000000000000000000000000000000000000000000000000000000000000'], 'store': None, 'used': 146458}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H15](../../../../decisions/H15.md): Observe unresolved fee defaults. Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict.

</details>
