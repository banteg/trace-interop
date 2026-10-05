# Raw state pending

`trace_rawTransaction` · raw-selector · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state and block environment an explicit third selector uses.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/raw-selector/manifest.json) |

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

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid number of params).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid number of params).

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid params).

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: rejected as invalid params (-32602: Invalid params).

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector pending: honored: the latest (block 0x30) post-state in the pending block 0x31 environment.

</details>
