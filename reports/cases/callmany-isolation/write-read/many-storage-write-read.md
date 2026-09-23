# Write read/many storage write read

`trace_callMany` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. The second call reads the first call’s simulated write. Each call reports its own sender nonce transition, including a reverted call. Only the first call writes slot zero; reverted writes and later reads add no storage transition. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Besu · 🛠️ Development](../../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Erigon · 📦 Release](../../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Erigon · 🛠️ Development](../../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Nethermind · 📦 Release](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Nethermind · 🛠️ Development](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Reth · 📦 Release](../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |
| [Reth · 🛠️ Development](../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "0x30"
  ]
}
```

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

</details>
