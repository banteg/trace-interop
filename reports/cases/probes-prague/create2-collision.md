# Create2 collision

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Failed frames have an error string; an exceptional halt carries result null. A CREATE2 address collision emits a failed create frame with no result; the caller continues with a later sibling at [2]. A CREATE2 address collision frame has error "Contract address collision". The collision pushes 0 and the caller continues to a successful CALL.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 4 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 4 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 4 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6460006000f3600052602a6005601b6000f5602052602a6005601b6000f5604052600060006000600060006110025af160605260606020f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x4c4b40",
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

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}
- Result shape at `trace/2`: {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}
- Result shape at `trace/2`: {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [1]: error 'Contract address collision', result null.
- Result shape at `trace/2`: {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Contract address collision', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'} is not valid under any of the given schemas

</details>
