# Combo auth type4 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-prague/manifest.json) |

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
      "maxFeePerGas": "0xb2d05e00",
      "maxPriorityFeePerGas": "0xb2d05e00",
      "to": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "type": "0x4"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.7-nightly · 4e8874b2** (`anvil Version: 1.8.7-nightly+4e8874b2`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Erigon · 3.9.0-dev · 598ba625** (`3.9.0-dev-598ba625`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.3.0-preview · 7192e7f3** (`2.3.0-preview+7192e7f3`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H14](../../decisions/H14.md): The call runs with type 4, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type4-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

</details>
