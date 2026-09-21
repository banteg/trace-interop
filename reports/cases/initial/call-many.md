# initial/call-many

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x0",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
        },
        [
          "trace"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x0",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
        },
        [
          "trace"
        ]
      ]
    ],
    "0x30"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0xffee",
      "stateDiff": null,
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x8d5b8",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x1fc63",
            "output": "0xffee"
          },
          "subtraces": 7,
          "traceAddress": [],
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
          "result": {
            "gasUsed": "0x48",
            "output": "0xffee"
          },
          "subtraces": 0,
          "traceAddress": [
            0
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "call",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [
            1
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "staticcall",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",

… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **invalid**.
- ``: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "error": {
      "code": -32603,
      "message": "Internal error"
    },
    "id": 1,
    "jsonrpc": "2.0"
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **invalid**.
- ``: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "error": {
      "code": -32603,
      "message": "Internal error"
    },
    "id": 1,
    "jsonrpc": "2.0"
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "first run for txIndex 0 error: fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, feeCap: 0 baseFee: 1677430"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "first run for txIndex 0 error: fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, feeCap: 0 baseFee: 1677430"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **invalid**.
- `0/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `0/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a
- `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0xffee",
      "stateDiff": null,
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x8d5b8",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x1fc63",
            "output": "0xffee"
          },
          "subtraces": 7,
          "traceAddress": [],
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
          "result": {
            "gasUsed": "0x48",
            "output": "0xffee"
          },
          "subtraces": 0,
          "traceAddress": [
            0
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "call",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "subtraces": 0,
          "traceAddress": [
            1
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "staticcall",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x7d",
            "output": "0x000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **invalid**.
- `0/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `0/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a
- `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0xffee",
      "stateDiff": null,
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x8d5b8",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x1fc63",
            "output": "0xffee"
          },
          "subtraces": 7,
          "traceAddress": [],
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
          "result": {
            "gasUsed": "0x48",
            "output": "0xffee"
          },
          "subtraces": 0,
          "traceAddress": [
            0
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "call",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "subtraces": 0,
          "traceAddress": [
            1
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "staticcall",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x7d",
            "output": "0x000000000000
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0xffee",
      "stateDiff": null,
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x8d5b8",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x1fc63",
            "output": "0xffee"
          },
          "subtraces": 7,
          "traceAddress": [],
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
          "result": {
            "gasUsed": "0x48",
            "output": "0xffee"
          },
          "subtraces": 0,
          "traceAddress": [
            0
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "call",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [
            1
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "staticcall",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",

… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0xffee",
      "stateDiff": null,
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x8d5b8",
            "input": "0x",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x1fc63",
            "output": "0xffee"
          },
          "subtraces": 7,
          "traceAddress": [],
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
          "result": {
            "gasUsed": "0x48",
            "output": "0xffee"
          },
          "subtraces": 0,
          "traceAddress": [
            0
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "call",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
            "gas": "0xea60",
            "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [
            1
          ],
          "type": "call"
        },
        {
          "action": {
            "callType": "staticcall",
            "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",

… preview truncated; use the full evidence link above.
```

</details>

