# Raw validation nonce low vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `1` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b09842da282a9830186a094000000000000000000000000000000000000100201808718e5bb3abd10a0a066622bd38bd8d2faf53fa011186688398c2035e1c6bc94c794a9331b79f37114a05369dcea2f88bced916b7e2729242b74c46574348380e5dcf7fd3be2bde48fbd",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. nonce below selected state

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. nonce below selected state

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. nonce below selected state

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. nonce below selected state

</details>
