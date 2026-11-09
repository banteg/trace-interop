# Call tree statediff priced

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. An account created and destroyed within the transaction is absent at both endpoints and has no account diff. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the traced refund 0 (from the vmTrace SSTOREs and the state diff)), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the traced refund 0 (from the vmTrace SSTOREs and the state diff)), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

</details>
