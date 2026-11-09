# Field gas zero eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000002fa20fc` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |

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

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too high -- CallGasCostMoreThanGasLimit (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too high -- CallGasCostMoreThanGasLimit (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32003: Intrinsic gas exceeds gas limit (intrinsic gas cost 53122 exceeds gas limit 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32003: Intrinsic gas exceeds gas limit (intrinsic gas cost 53122 exceeds gas limit 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed result with output 0x0000000000000000000000000000000000000000000000000000000002fa20fc
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed result with output 0x0000000000000000000000000000000000000000000000000000000002fa20fc
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: err: intrinsic gas too low: have 0, want 53122 (supplied gas 0) (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too low (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H15](../../decisions/H15.md): An explicit gas of 0 is a zero limit that fails the intrinsic-gas check: the call is rejected (-38013 recommended) with no trace, never run with the default budget or traced out of gas. eth_call parity control for field-gas-zero; the rule follows eth_simulateV1 and eth_call in every client but Erigon, whose eth_call treats 0 as omitted. Observed: Observed rpc_error -32000: intrinsic gas too low (-38013 recommended)
- [H15](../../decisions/H15.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
