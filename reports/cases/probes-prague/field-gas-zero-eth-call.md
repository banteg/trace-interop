# Field gas zero eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fee-combos/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fee-combos/probes-prague/manifest.json) |

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

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too high -- CallGasCostMoreThanGasLimit (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too high -- CallGasCostMoreThanGasLimit (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32003: Intrinsic gas exceeds gas limit (intrinsic gas cost 53122 exceeds gas limit 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32003: Intrinsic gas exceeds gas limit (intrinsic gas cost 53122 exceeds gas limit 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed result with output 0x0000000000000000000000000000000000000000000000000000000002fa20fc
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed result with output 0x0000000000000000000000000000000000000000000000000000000002fa20fc
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too low (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too low (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
