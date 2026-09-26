# Field authorization

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. A valid authorization delegates key 1 to the marker contract, which returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32603` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1 call frames; nonempty output | ❔ Policy open | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "authorizationList": [
        {
          "address": "0x0000000000000000000000000000000000001002",
          "chainId": "0xc72dd9d5e883e",
          "nonce": "0xa",
          "r": "0x4e9c1a2430ff1f88a19f6567e51648c181b00616b4adcff8548b9785e3898814",
          "s": "0x707840665ae678f4933987814326a609a2ddb271ed461970ad744c0aae11779f",
          "yParity": "0x0"
        }
      ],
      "data": "0x",
      "from": "0x0c2c51a0990aee1d73c1228de158688341557508",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "to": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected a result; observed rpc_error -32603 Internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected a result; observed rpc_error -32603 Internal error

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x']

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected a result; observed rpc_error -32602 gasPrice conflicts with blob or authorization fields

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x']

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): A valid authorization delegates key 1 to the marker contract, which returns word 42. Mixing legacy gasPrice with an authorizationList is an open input policy, since no signed transaction type carries both; the response does not isolate the authorization field, which field-authorization-1559 asserts with EIP-1559 fees. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

</details>
