# Call number pending

`trace_call` · h30 · [All reports](../../README.md)

**What this checks:** Record pending behavior without assuming a settled state or localization policy. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; nonempty output | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |

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

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: RPC error -32000.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

</details>
