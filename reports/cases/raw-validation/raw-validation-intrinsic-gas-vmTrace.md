# Raw validation intrinsic gas vmtrace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | RPC error `800` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520794000000000000000000000000000000000000100201808718e5bb3abd10a0a03e2bb48ffdc3a7718afc598d928b473e31cb4f1757a33a884d91d0e2bacc3eb7a00ff33e7901b8f83ce9451b3a94d395953062ce98020698dea332741bd49e596c",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. gas limit below 21000 intrinsic gas

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. gas limit below 21000 intrinsic gas

</details>
