# Write revert read/many storage write revert read

`trace_callMany` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Sequential calls retain prior writes and roll back reverted writes. Each call reports its own sender nonce transition, including a reverted call. Only the first call writes slot zero; reverted writes and later reads add no storage transition. Failed frames have an error string and an explicit object or null result. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Check accounting against independent gas.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../../clients/go-ethereum_trace.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../../clients/nethermind_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/observations.json) · [Build/run](../../../../evidence/2026-09-24/h15-call-compat/callmany-isolation/manifest.json) |

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
          "data": "0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001",
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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. No receipt gas or execution-gas witness was captured.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. No receipt gas or execution-gas witness was captured.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=26335 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=52625824880950, burn=44175119050.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=26335 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=52625824880950, burn=44175119050.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H16](../../../decisions/H16.md): Only the first call writes slot zero; reverted writes and later reads add no storage transition.

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. No receipt gas or execution-gas witness was captured.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. No receipt gas or execution-gas witness was captured.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=26335 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=52625824880950, burn=44175119050.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=86998971407520, burn=73028592480.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=26335 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=52625824880950, burn=44175119050.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=46235189302090, burn=38810697910.

</details>
