# Raw state hash object

`trace_rawTransaction` · raw-selector · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state and block environment an explicit third selector uses.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/raw-selector/manifest.json) |

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
    {
      "blockHash": "0x55445029cff2a6e61d40e9bd8c5db22aeef3da108734b872b64aec7ffbf44733"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: honored: the block 0x19 post-state in the block 0x19 environment.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: honored: the block 0x19 post-state in the block 0x19 environment.

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: Invalid number of params).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: Invalid number of params).

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: too many arguments, want at most 2).

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: too many arguments, want at most 2).

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: too many arguments, want at most 2).

**Nethermind · 2.2.0-preview · 759efed7** (`2.2.0-preview+759efed7`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: Invalid params).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: rejected as invalid params (-32602: Invalid params).

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: honored: the block 0x19 post-state in the block 0x19 environment.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H12](../../decisions/H12.md): Record which state and block environment an explicit third selector uses. Selector block 0x19 as an EIP-1898 object: honored: the block 0x19 post-state in the block 0x19 environment.

</details>
