# Call transfer statediff

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001234",
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "value": "0x1",
      "data": "0x"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

</details>
