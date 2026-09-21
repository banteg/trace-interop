# a/call-siblings-revert-ok

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
      "to": "0x0000000000000000000000000000000000001005"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **change_needed** — The successful second sibling retains its output and has no error.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x2fc00f38b405"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34726025e8efc96"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [
          1
        ],
        "type": "call"

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **not_observed**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **matches** — The successful second sibling retains its output and has no error.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x2fc00f38b405"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
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
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAd
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **matches** — The successful second sibling retains its output and has no error.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x2fc00f38b405"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
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
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAd
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **matches** — The successful second sibling retains its output and has no error.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub':

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x2fc00f38b405"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34726025e8efc96"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x0000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **matches** — The successful second sibling retains its output and has no error.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub':

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x2fc00f38b405"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34726025e8efc96"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x0000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **matches** — The successful second sibling retains its output and has no error.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
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
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAddress": [
          1
        ],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000",
      "ops": [
        {
          "cost": 3,
          "ex": {

… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **matches** — The successful second sibling retains its output and has no error.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
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
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAddress": [
          1
        ],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000",
      "ops": [
        {
          "cost": 3,
          "ex": {

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H24: **change_needed** — The successful second sibling retains its output and has no error.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x2fc00f38b405"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34726025e8efc96"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
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
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001005",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x1499",
          "output": "0x"
        },
        "subtraces": 2,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001003",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "call"
      },
      {
        "action": {
          "callType": "call",
          "from": "0x0000000000000000000000000000000000001005",
          "gas": "0xea60",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [
          1
        ],
        "type": "call"

… preview truncated; use the full evidence link above.
```

</details>

