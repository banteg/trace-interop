# Raw wrong chain trace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86481858477359400825208940000000000000000000000000000000000001234018026a0680e20ade3f3bfbbb3d8e2246c26a13efb3a8e886c182c159cd240b4636342b8a027a25d70c994f869fa5abe6b841ddfff0ab32944d6e9719c830ace909c024a3b",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
