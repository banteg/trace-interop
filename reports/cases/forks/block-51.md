# forks/block-51

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x33"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- `9`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'address': '0x30

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash"
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- `9`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70d', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'result': {'address': '0x30

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash"
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- `11`: 'transactionHash' is a required property
- `11`: 'transactionPosition' is a required property

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x76430fba1b629206573ad53847b0bc7e9f80161b0e79750803715a8fb1bc5955",
      "transactionPosition": 2,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'error':
- `4`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b
- `6`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9', 'blockNumber': 51, 'erro
- `11`: 'transactionHash' is a required property
- `11`: 'transactionPosition' is a required property

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x76430fba1b629206573ad53847b0bc7e9f80161b0e79750803715a8fb1bc5955",
      "transactionPosition": 2,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",

… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa23373d1e4fa559fc33ffb791665855530831c83d0c241ef6b2d3f46a5f448f4",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x8d5b8",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "value": "0x0"
      },
      "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
      "blockNumber": 51,
      "result": {
        "gasUsed": "0x1fc61",
        "output": "0xffee"
      },
      "subtraces": 7,
… preview truncated; use the full evidence link above.
```

</details>

