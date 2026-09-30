# Field gas zero eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32003` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32003` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32000` | ❔ Policy open | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x0",
      "input": "0x5a60005260206000f3"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too high -- CallGasCostMoreThanGasLimit (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too high -- CallGasCostMoreThanGasLimit (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32003: Intrinsic gas exceeds gas limit (intrinsic gas cost 53122 exceeds gas limit 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32003: Intrinsic gas exceeds gas limit (intrinsic gas cost 53122 exceeds gas limit 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 923b4d31** (`3.8.0-dev-923b4d31`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed result with output 0x0000000000000000000000000000000000000000000000000000000002fa20fc
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed result with output 0x0000000000000000000000000000000000000000000000000000000002fa20fc
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · ec1cec0b** (`Geth/v1.17.7-unstable-ec1cec0b-2026-09-30/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too low (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too low (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
