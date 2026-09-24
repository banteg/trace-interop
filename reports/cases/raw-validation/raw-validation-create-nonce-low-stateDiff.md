# Raw validation create nonce low statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | RPC error `1` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86009842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0f79bc81b54de5c56b99760bc92863bb4742e555f6f81ff00d3d2b6b7e53fadcea055a3935137685afe3b9738bb7563deede6b29147ecb36f00519df0f94b08127b",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce below selected state

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce below selected state

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce below selected state

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce below selected state

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce below selected state

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. creation nonce below selected state
- Result shape at `output`: None is not of type 'string'
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0xe893'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77a4d56aa400248b0b1613508f5b73': {'balance': {'+': '0x1'}, 'code': {'+': '0x00000000000000000000000000de48310d77a4d56aa400248b0b1613508f5b73'}, 'nonce': {'+':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_low; code -32000; accepted [-32003, 1].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_low; code -32000; accepted [-32003, 1].

</details>
