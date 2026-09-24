# Raw validation intrinsic gas statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. Reject a signed transaction that fails execution validity at the selected state before EVM execution. Proposed transaction-validation error code: -32003 (Transaction rejected). Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/raw-validation/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520794000000000000000000000000000000000000100201808718e5bb3abd10a0a03e2bb48ffdc3a7718afc598d928b473e31cb4f1757a33a884d91d0e2bacc3eb7a00ff33e7901b8f83ce9451b3a94d395953062ce98020698dea332741bd49e596c",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. gas limit below 21000 intrinsic gas

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution. gas limit below 21000 intrinsic gas

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Proposed transaction-validation error code: -32003 (Transaction rejected). Error-code alignment is separate from whether validation occurred; current clients also use -32000.

</details>
