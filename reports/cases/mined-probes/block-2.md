# Block 2

`trace_block` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The reader makes one STATICCALL to the system contract. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 5 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 4 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x2"
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: unexpected error 'Reverted'; result.output None != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000014 != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x0000000000000000000000000000000000004788', 'value': '0x0'}, 'blockHash': '0xd049e8e91a6e93a831bb365b753bc82b734e712ec6bf1a3d9be44f8289f790d5', 'blockNumber': 2, 'result':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: unexpected error 'Reverted'; result.output None != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000014 != 0x2c809fbc7e3991c8ab560d1431fa8b6f25be4ab50977f0294dfeca9677866b6e
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x0000000000000000000000000000000000004788', 'value': '0x0'}, 'blockHash': '0xd049e8e91a6e93a831bb365b753bc82b734e712ec6bf1a3d9be44f8289f790d5', 'blockNumber': 2, 'result':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb38', 'input': '0x', 'to': '0x0000000000000000000000000000000000004788', 'value': '0x0'}, 'blockHash': '0xd049e8e91a6e93a831bb365b753bc82b734e712ec6bf1a3d9be44f8289f790d5', 'blockNumber': 2, 'result':

</details>
