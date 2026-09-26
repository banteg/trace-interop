# Call number pending

`trace_call` · h30 · [All reports](../../README.md)

**What this checks:** Record pending behavior without assuming a settled state or localization policy. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ❔ Policy open; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; nonempty output | ❔ Policy open; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x4360005260206000f3"
    },
    [
      "trace"
    ],
    "pending"
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8583e', 'init': '0x4360005260206000f3', 'value': '0x0'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x0000000000000000000000000000000000000000000000000000000000000030', 'gasUsed': '0x1911'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8583e', 'init': '0x4360005260206000f3', 'value': '0x0'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x0000000000000000000000000000000000000000000000000000000000000030', 'gasUsed': '0x1911'},

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: RPC error -32000.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: RPC error -32000.

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: RPC error -32602.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 48.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. call-number-pending: NUMBER 49.

</details>
