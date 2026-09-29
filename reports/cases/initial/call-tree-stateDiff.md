# Call tree statediff

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. An account created and destroyed within the transaction is absent at both endpoints and has no account diff. Check accounting against independent gas. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 0 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H26](../../decisions/H26.md): An account created and destroyed within the transaction is absent at both endpoints and has no account diff. 0xe5f841427f4e0c33bb76fd34499298a93916ba51: {'balance': {'-': '0x0'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'storage': {}}
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.
- Result shape at `output`: None is not of type 'string'

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=120918..151147 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=0, expected tip=0/gas, burn=0/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Assess the declared property. For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15.

</details>
