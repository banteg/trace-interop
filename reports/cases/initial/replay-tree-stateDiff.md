# Replay tree statediff

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. A deleted account reports storage {}; its account deletion implies every slot is wiped. The method responds without Method not found (-32601). An account created and destroyed within the transaction is absent at both endpoints and has no account diff. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · a1ce80fb](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 45912ba3](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "stateDiff"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738.
- [H26](../../decisions/H26.md): An account created and destroyed within the transaction is absent at both endpoints and has no account diff. 0x2d303c5b7911d87d594bf1b31fbb9aa187888893: {'balance': {'-': '0x0'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'storage': {}}
- Result shape at `/`: {'output': '0xffee', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x3b002', 'to': '0x63649'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x2d303c5b7911d87d594bf1b31fbb9aa187888893': {'balance': {'-': '0x0'}, 'code': {'-': '0x'}, 'nonce': {'-': '0x0'}, 'st

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x3b002', 'to': '0x63649'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34ae10a685853b1', 'to': '0xc

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H08](../../decisions/H08.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H08](../../decisions/H08.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H16](../../decisions/H16.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H17](../../decisions/H17.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- Result shape at `/`: {'output': None, 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x3b002', 'to': '0x63649'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34ae10a685853b1', 'to': '0xc097c

</details>
