# Call number pending

`trace_call` · h30 · [All reports](../../README.md)

**What this checks:** Record pending behavior without assuming a settled state or localization policy. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-24/current-matrix/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x4360005260206000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400"
    },
    [
      "trace"
    ],
    "pending"
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: RPC error -32000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: RPC error -32602.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

</details>
