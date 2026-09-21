# initial/call-tree-trace-priced

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **change_needed** — Successful creation uses address, code and gasUsed.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- `trace/7`: {'action': {'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0xe5f841427f4e0c33bb76fd34499298a93916ba51', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [6], 'type': 'creat

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "output": "0x0000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000c72dd9d5e883e000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **change_needed** — Successful creation uses address, code and gasUsed.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- `trace/7`: {'action': {'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0xe5f841427f4e0c33bb76fd34499298a93916ba51', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceAddress': [6], 'type': 'creat

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "output": "0x0000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000c72dd9d5e883e000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "gas": "0xea60",
          "input": "0x",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
          "value":
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "gas": "0xea60",
          "input": "0x",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
          "value":
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "output": "0x0000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000c72dd9d5e883e000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "output": "0x0000000000000000000000000000000000000000000000000000000000000030000000000000000000000000000000000000000000000000000c72dd9d5e883e000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "gas": "0xea60",
          "input": "0x",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
          "value":
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
          "gas": "0xea60",
          "input": "0x",
          "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
          "value":
… preview truncated; use the full evidence link above.
```

</details>

