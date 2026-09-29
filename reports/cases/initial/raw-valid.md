# Raw valid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state an explicit third selector uses. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a80847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a04c833abdb116ad76fc98610ae0e626d7e35154f1fba38ce6bfdaf69a31eec42ca035ecfb996cc68a2a03df0e1087194e25180b01bf0469f69b4f1d330eea9d027a",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x0"
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.8.0-dev · a2a19253** (`3.8.0-dev-a2a19253`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.2.0-preview · 287f54f0** (`2.2.0-preview+287f54f0`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

</details>
