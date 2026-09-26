# Raw validation create valid statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. Requested stateDiff records the signed execution state changes. Creation stateDiff installs the constructor ADDRESS bytes at the signed creation address.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600a842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0371d5f6be359abfc8aa07862de5609e2374dea339665f9fcfe54ebfeef4e5d53a00de19f45781c0c3903dca51e8da7bf4ac28cc805e9a63e27c4bf1ef1d00f951a",
    [
      "stateDiff"
    ]
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H13](../../decisions/H13.md): The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection.
- Result shape at `output`: None is not of type 'string'
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xe893'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x1'}, 'code': {'+': '0x00000000000000000000000000de48310d77a4d56aa400248b0b1613508f5b73'}, 'nonce': {'+':

</details>
