# Raw state pending

`trace_rawTransaction` · raw-selector · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state and block environment an explicit third selector uses.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/raw-selector/manifest.json) |

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

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid number of params).

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid number of params).

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid params).

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid params).

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

</details>
