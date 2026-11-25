# Transaction create destroy absent

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. The creation and its SELFDESTRUCT both appear. The factory call returns the created address word. The creation succeeds with empty code before destroying itself. The suicide frame transfers the new contract’s whole balance, including any prefunded wei, to itself. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284"
  ]
}
```

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [0, 0]: error None, result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x2bb18', 'input': '0x30ff', 'to': '0x000000000000000000000000000000000000fac0', 'value': '0x100'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'res

</details>
