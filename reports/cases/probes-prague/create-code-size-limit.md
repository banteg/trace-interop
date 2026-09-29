# Create code size limit

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Failed frames have an error string; an exceptional halt omits result or sets it to null. The failed creation frame has an error and no result; the caller continues. Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. The caller sees CREATE push 0.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x656160016000f36000526006601a6000f060005260206000f3",
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

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'CreateContractSizeLimit', 'result': None, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'CreateContractSizeLimit', 'result': None, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'Code is too large', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x4b7ae2', 'init': '0x6160016000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'Code is too large', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'Code is too large', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x4b7ae2', 'init': '0x6160016000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'Code is too large', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'max code size exceeded: size 24577 limit 24576', 'result': None, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'CreateContractSizeLimit', 'result': None, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H09](../../decisions/H09.md): Code above the EIP-170 size limit fails the creation with "Out of gas", as Parity and EIP-170 report it. Expected {'error': 'Out of gas'}; got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d1d4', 'init': '0x6160016000f3', 'value': '0x0'}, 'error': 'CreateContractSizeLimit', 'result': None, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

</details>
