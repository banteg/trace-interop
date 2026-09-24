# Raw nonce high vmtrace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | RPC error `2` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8186847735940082520894000000000000000000000000000000000000123401808718e5bb3abd109fa07088ff5b782a62ee95e868e0cb949f05a4fa52e5dff86136e2d3f5eaa9cfb34ba053f2145a9d3b1d5f726bef1e95aa15db4ab7f50099330d2bbe31dae1e73698ce",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_high; code -32000; accepted [-32003, 2].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_high; code -32000; accepted [-32003, 2].

</details>
