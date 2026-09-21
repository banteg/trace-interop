# initial/filter-all

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtr
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **invalid**.
- `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':
- `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b
- `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error
- `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result': {'address': '0x2d3

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtraces": 0,
      "traceAddress": [
        0

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **invalid**.
- `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':
- `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b
- `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error
- `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result': {'address': '0x2d3

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtraces": 0,
      "traceAddress": [
        0

… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtr
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtr
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **invalid**.
- `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':
- `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b
- `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error
- `13`: 'transactionHash' is a required property
- `13`: 'transactionPosition' is a required property

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtraces": 0,
      "traceAddress": [
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **invalid**.
- `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':
- `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b
- `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error
- `13`: 'transactionHash' is a required property
- `13`: 'transactionPosition' is a required property

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtraces": 0,
      "traceAddress": [
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {

… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtr
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H03: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

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
        "gas": "0x13488",
        "input": "0x01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "result": {
        "gasUsed": "0x889",
        "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
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
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x2343f",
        "output": "0xffee"
      },
      "subtraces": 7,
      "traceAddress": [],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtr
… preview truncated; use the full evidence link above.
```

</details>

