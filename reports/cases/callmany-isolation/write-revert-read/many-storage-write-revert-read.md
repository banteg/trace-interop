# Write revert read/many storage write revert read

`trace_callMany` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Sequential calls retain prior writes and roll back reverted writes. Each call reports its own sender nonce transition, including a reverted call. Only the first call writes slot zero; reverted writes and later reads add no storage transition. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Check accounting against independent gas.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../clients/reth_release.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../clients/reth_development.md) | 3 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/callmany-isolation/manifest.json) |

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

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H15](../../../decisions/H15.md): Check accounting against independent gas. No receipt gas or execution-gas witness was captured.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H09](../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H15](../../../decisions/H15.md): Check accounting against independent gas. No receipt gas or execution-gas witness was captured.
- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=26335 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=26335 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
