# Call tree statediff

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. Assess the declared property. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Check accounting against independent gas.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-24/h15-call-compat/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/initial/manifest.json) |

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
      "gasPrice": "0x0",
      "data": "0x"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee=0.

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H16](../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee=0.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H16](../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee=0.
- Result shape at `output`: None is not of type 'string'

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H16](../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee=0.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H16](../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee=0.

</details>
