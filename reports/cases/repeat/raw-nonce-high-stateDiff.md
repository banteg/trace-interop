# Raw nonce high statediff

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 0 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 0 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 0 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 0 call frames; output `0x` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-23/geth-40eecf3-repeat/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-repeat/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; output `null` | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32000` | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8186847735940082520894000000000000000000000000000000000000123401808718e5bb3abd109fa07088ff5b782a62ee95e868e0cb949f05a4fa52e5dff86136e2d3f5eaa9cfb34ba053f2145a9d3b1d5f726bef1e95aa15db4ab7f50099330d2bbe31dae1e73698ce",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `output`: None is not of type 'string'

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `output`: None is not of type 'string'

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-40eecf36-2026-09-23/linux-amd64/go1.26.1`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

</details>
