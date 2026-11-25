# Create code deposit oog

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Failed frames have an error string; an exceptional halt carries result null. The failed creation frame has an error and no result; the caller continues. Code whose deposit costs more than the child's remaining gas fails the creation with "Out of gas". The caller sees CREATE push 0.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x65615dc06000f36000526006601a6000f060005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x14a67e",
      "gasPrice": "0x77359400"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [0]: error 'Out of gas', result null.
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x130ba5', 'init': '0x615dc06000f3', 'value': '0x0'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [0]: error 'Out of gas', result null.
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x130ba5', 'init': '0x615dc06000f3', 'value': '0x0'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [0]: error 'Out of gas', result null.
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x130ba5', 'init': '0x615dc06000f3', 'value': '0x0'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

</details>
