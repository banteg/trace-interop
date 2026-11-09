# Raw state pending

`trace_rawTransaction` · raw-selector · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state and block environment an explicit third selector uses.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-selector/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf87d80847735940083030d408080a643600052734a0f1452281bcec5bd90c3dce6162a5995bfe9df316020524860405260606000f38718e5bb3abd109fa0379dd8d06b2adb0b1c56d2112a5d9be3ce05b49d06ff57de79c26da3d879ea3da0020894ecc2d5844a5e7cd262bcb0190889f17d549a8b230cfa3e10f646e852cf",
    [
      "trace"
    ],
    "pending"
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid number of params).

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid number of params).

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid params).

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

</details>
