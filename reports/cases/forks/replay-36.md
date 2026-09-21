# forks/replay-36

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x24",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x",
      "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "to": "0xa9d71bf4a7958ef8f"

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000
- `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under an
- `1/trace/7`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'result': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'gasUsed': '0x1682', 'output': '0x'}, 'subtraces': 1, 'traceA

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x",
      "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "revertReason": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "to": "0xa9d71bf4a7958ef8f"

… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s
- `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "to": "0xa9d71bf4a7958ef8f"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "f
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s
- `1/trace/2`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddres
- `1/trace/4`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'error': 'Static call violation', 'subtraces': 0, 'traceAddress': [3], 'type': 'call'} is not valid under a

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "to": "0xa9d71bf4a7958ef8f"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "f
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a79560ea9",
              "to": "0xa9d71bf4a7956694a"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd730f0",
              "to": "0xc097ce7bc90715b34b89f61879cc4f"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x49",
              "to": "0x4a"
            }
          },
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x13488",
            "input": "0x01",
            "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
            "value": "0x0"
          },
          "error": "Reverted",
          "result": {
            "gasUsed": "0x889",
            "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x894d679a5f0efe3beb6fa7e13b7c92c6c223c815f625a77be692533f73e21eb2",
      "vmTrace": null
    },
    {
      "output": "0xffee",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xa9d71bf4a7956694a",
              "
… preview truncated; use the full evidence link above.
```

</details>

