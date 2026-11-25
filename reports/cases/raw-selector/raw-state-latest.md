# Raw state latest

`trace_rawTransaction` · raw-selector · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state and block environment an explicit third selector uses.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/raw-selector/manifest.json) |

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
    "latest"
  ]
}
```

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: honored: the latest (block 0x30) post-state in the head (block 0x30) environment.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: honored: the latest (block 0x30) post-state in the head (block 0x30) environment.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: Invalid number of params).

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: Invalid number of params).

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: too many arguments, want at most 2).

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: too many arguments, want at most 2).

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: rejected as invalid params (-32602: Invalid params).

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: honored: the latest (block 0x30) post-state in the head (block 0x30) environment.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector latest: honored: the latest (block 0x30) post-state in the head (block 0x30) environment.

</details>
