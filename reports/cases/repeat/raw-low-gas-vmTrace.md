# Raw low gas vmtrace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `800` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b81858477359400824e2094000000000000000000000000000000000000123401808718e5bb3abd10a0a038e0b48a1022d5c55eea7e525942547d2009224ffa7ab6d1b40a5a16cb70a590a0279569cdb60041c1eac5043486547bdf086c64543c7e2d07870a288096213d33",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
