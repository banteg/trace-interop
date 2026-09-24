# Raw valid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Observe the explicit block-selector extension separately from the two-argument baseline. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ❔ Policy open | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |

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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Geth draft fork · 1.17.7-unstable · bb5c4682** (`Geth/v1.17.7-unstable-bb5c4682-2026-09-24/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request returned a result; this does not prove which block state was used.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request returned a result; this does not prove which block state was used.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

</details>
