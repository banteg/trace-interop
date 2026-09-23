# Raw valid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Observe the explicit block-selector extension separately from the two-argument baseline. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | RPC error `-32602` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ❔ Policy open | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
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

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request was rejected as invalid params.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request returned a result; this does not prove which block state was used.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H12](../../decisions/H12.md): Observe the explicit block-selector extension separately from the two-argument baseline. The third-argument request returned a result; this does not prove which block state was used.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior.

</details>
