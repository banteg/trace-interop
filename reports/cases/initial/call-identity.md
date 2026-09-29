# Call identity

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. The identity precompile call frame preserves its input as return bytes. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000000004",
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "value": "0x0",
      "data": "0x11223344"
    },
    [
      "trace",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H22](../../decisions/H22.md): The identity precompile call frame preserves its input as return bytes.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H22](../../decisions/H22.md): The identity precompile call frame preserves its input as return bytes.

</details>
