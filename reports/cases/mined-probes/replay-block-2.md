# Replay block 2

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. Block-level system writes belong to no transaction’s stateDiff. The reader makes one STATICCALL to the system contract. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x2",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)
- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Expected 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e, got 0x0000000000000000000000000000000000000000000000000000000000000014.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. 0x0000000000000000000000000000000000004788: expected {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}}, '0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}, got {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000014'}}}}.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: unexpected error 'Reverted'; result.output None != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000014 != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Expected 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d, got 0x0000000000000000000000000000000000000000000000000000000000000000.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. 0x0000000000000000000000000000000000002935: expected {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d'}}, '0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}, got {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=72160 (independent receipt), price=2765670938, expected tip=2000000000/gas, burn=765670938/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=70071 (independent receipt), price=2765670938, expected tip=2000000000/gas, burn=765670938/gas, blob fee and destroyed wei=0.
- Result shape at `0/trace/1`: {'action': {'callType': 'staticcall', 'from': '0x0000000000000000000000000000000000004788', 'gas': '0x2a634', 'input': '0x0000000000000000000000000000000000000000000000000000000000000014', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'trac

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Expected 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e, got 0x0000000000000000000000000000000000000000000000000000000000000014.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. 0x0000000000000000000000000000000000004788: expected {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e'}}, '0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}, got {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000014'}}}}.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: unexpected error 'Reverted'; result.output None != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000014 != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Expected 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d, got 0x0000000000000000000000000000000000000000000000000000000000000000.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. The reader records STATICCALL success and the word in slots 1 and 0. 0x0000000000000000000000000000000000002935: expected {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000000': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d'}}, '0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}, got {'balance': '=', 'code': '=', 'nonce': '=', 'storage': {'0x0000000000000000000000000000000000000000000000000000000000000001': {'*': {'from': '0x0000000000000000000000000000000000000000000000000000000000000000', 'to': '0x0000000000000000000000000000000000000000000000000000000000000001'}}}}.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=72160 (independent receipt), price=2765670938, expected tip=2000000000/gas, burn=765670938/gas, blob fee and destroyed wei=0.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=70071 (independent receipt), price=2765670938, expected tip=2000000000/gas, burn=765670938/gas, blob fee and destroyed wei=0.
- Result shape at `0/trace/1`: {'action': {'callType': 'staticcall', 'from': '0x0000000000000000000000000000000000004788', 'gas': '0x2a634', 'input': '0x0000000000000000000000000000000000000000000000000000000000000014', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'trac

</details>
