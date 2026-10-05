# Combo auth type4 gasprice eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
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
      "to": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "type": "0x4"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected a result; observed rpc_error -32603 Internal error (Internal Error in Besu - java.util.NoSuchElementException: No value present
	at java.base/java.util.Opti

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected a result; observed rpc_error -32603 Internal error (Internal Error in Besu - java.util.NoSuchElementException: No value present
	at java.base/java.util.Opti

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-gasprice. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

</details>
