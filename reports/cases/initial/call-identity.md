# Call identity

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. The identity precompile call frame preserves its input as return bytes. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |

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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H22](../../decisions/H22.md): The identity precompile call frame preserves its input as return bytes.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H22](../../decisions/H22.md): The identity precompile call frame preserves its input as return bytes.

</details>
