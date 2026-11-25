# Combo auth type2 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000002a` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |

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
      "type": "0x2"
    },
    "latest"
  ]
}
```

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x']

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H14](../../decisions/H14.md): The call runs with type 2, which does not change execution, with its authorization applied, so the delegated marker returns word 42. eth_call parity control for combo-auth-type2-dynamic. Observed: Expected ['0x000000000000000000000000000000000000000000000000000000000000002a']; got ['0x000000000000000000000000000000000000000000000000000000000000002a']

</details>
