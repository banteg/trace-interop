# Raw below basefee statediff

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `806` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86681850182520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a6525c23fcea9e006fece50614f7aaf6172e8bcc4cd6226480c174bbc055351c9fc17630ea66fe9c6ebfe8f96bb98c2433c16b43fc260cbd2530add6931d551a",
    [
      "stateDiff"
    ]
  ]
}
```

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

</details>
