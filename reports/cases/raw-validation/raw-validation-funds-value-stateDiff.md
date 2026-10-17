# Raw validation funds value statediff

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | RPC error `809` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8730a842da282a9830186a0940000000000000000000000000000000000001002880de0b6b3a7640001808718e5bb3abd109fa045db63de254132f2e3ef3e798472b6afc3a97624aec0b0537f25f82a5b3585a4a03edc2ad5855f1d765a1ccc90d6326a3723bdd2c41b103b04bda7baeab5a5bae3",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. insufficient balance for value alone

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. insufficient balance for value alone

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. insufficient balance for value alone

</details>
