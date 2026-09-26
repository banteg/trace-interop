# Depth limit

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. Under the deepest executed frame, at depth 1024, the CALL and CREATE that fail the depth precheck each emit a failed frame with no result and no subtraces. A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1027 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1027 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1028 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1028 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 1028 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1026 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 1026 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1028 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 1028 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x60296022600039602960006000f060006000600060006000856102005a03f1505000601e80600b6000396000f360006000600060006000306102005a03f1601c57600060006000f0505b00",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x200000",
      "gasPrice": "0x0"
    },
    [
      "trace"
    ],
    "0x3"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Under the deepest executed frame, at depth 1024, the CALL and CREATE that fail the depth precheck each emit a failed frame with no result and no subtraces. Deepest executed frame at depth 1025 with subtraces 0; attempts beyond it (type, error, result, subtraces): [].
- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". No failed attempts ['call', 'create'] under the deepest executed frame at depth 1025.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x1f228c', 'init': '0x60296022600039602960006000f060006000600060006000856102005a03f1505000601e80600b6000396000f360006000600060006000306102005a03f1601c57600060006000f0505b00', 'value': '0x0'}, 'result': {'address': '0x3cf2e7052
- Result shape at `trace/1`: {'action': {'from': '0x3cf2e7052ebd484a8d6fbca579ddb3cf920de9d3', 'gas': '0x1e2ad6', 'init': '0x601e80600b6000396000f360006000600060006000306102005a03f1601c57600060006000f0505b00', 'value': '0x0'}, 'result': {'address': '0xb56c1cce8dc86e312b79166e061a8398544480b4', 'code': '0x60006000600060006000306
- Result shape at `trace/1026`: {'action': {'from': '0x3cf2e7052ebd484a8d6fbca579ddb3cf920de9d3', 'gas': '0x1561a9', 'init': '0x60006000600060006000306102005a03f1601c57600060006000f0505b00', 'value': '0x0'}, 'result': {'address': '0xb56c1cce8dc86e312b79166e061a8398544480b4', 'code': '0x', 'gasUsed': '0xffffffffffffa921'}, 'subtrac

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Under the deepest executed frame, at depth 1024, the CALL and CREATE that fail the depth precheck each emit a failed frame with no result and no subtraces. Deepest executed frame at depth 1025 with subtraces 0; attempts beyond it (type, error, result, subtraces): [].
- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". No failed attempts ['call', 'create'] under the deepest executed frame at depth 1025.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x1f228c', 'init': '0x60296022600039602960006000f060006000600060006000856102005a03f1505000601e80600b6000396000f360006000600060006000306102005a03f1601c57600060006000f0505b00', 'value': '0x0'}, 'result': {'address': '0x3cf2e7052
- Result shape at `trace/1`: {'action': {'from': '0x3cf2e7052ebd484a8d6fbca579ddb3cf920de9d3', 'gas': '0x1e2ad6', 'init': '0x601e80600b6000396000f360006000600060006000306102005a03f1601c57600060006000f0505b00', 'value': '0x0'}, 'result': {'address': '0xb56c1cce8dc86e312b79166e061a8398544480b4', 'code': '0x60006000600060006000306
- Result shape at `trace/1026`: {'action': {'from': '0x3cf2e7052ebd484a8d6fbca579ddb3cf920de9d3', 'gas': '0x1561a9', 'init': '0x60006000600060006000306102005a03f1601c57600060006000f0505b00', 'value': '0x0'}, 'result': {'address': '0xb56c1cce8dc86e312b79166e061a8398544480b4', 'code': '0x', 'gasUsed': '0xffffffffffffa921'}, 'subtrac

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". Expected labels ['Max call depth exceeded', 'Max call depth exceeded']; got ['max call depth exceeded', 'max call depth exceeded'].

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". Expected labels ['Max call depth exceeded', 'Max call depth exceeded']; got ['max call depth exceeded', 'max call depth exceeded'].

**Nethermind · 2.1.0-preview · b4211ad9** (`2.1.0-preview+b4211ad9`)

- [H29](../../decisions/H29.md): Under the deepest executed frame, at depth 1024, the CALL and CREATE that fail the depth precheck each emit a failed frame with no result and no subtraces. Deepest executed frame at depth 1024 with subtraces 0; attempts beyond it (type, error, result, subtraces): [].
- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". No failed attempts ['call', 'create'] under the deepest executed frame at depth 1024.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H29](../../decisions/H29.md): Under the deepest executed frame, at depth 1024, the CALL and CREATE that fail the depth precheck each emit a failed frame with no result and no subtraces. Deepest executed frame at depth 1024 with subtraces 0; attempts beyond it (type, error, result, subtraces): [].
- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". No failed attempts ['call', 'create'] under the deepest executed frame at depth 1024.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". Expected labels ['Max call depth exceeded', 'Max call depth exceeded']; got ['CallTooDeep', 'CallTooDeep'].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): A CALL or CREATE that fails the depth precheck has error "Max call depth exceeded". Expected labels ['Max call depth exceeded', 'Max call depth exceeded']; got ['CallTooDeep', 'CallTooDeep'].

</details>
