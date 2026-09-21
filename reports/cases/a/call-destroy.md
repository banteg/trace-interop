# a/call-destroy

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
      "to": "0x0000000000000000000000000000000000001007"
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
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
            "to": "0x616be8947699"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "+": "0x64"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x0"
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b346f44bd8acd496"
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suic
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
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
            "to": "0x616be8947699"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "+": "0x64"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x0"
        },
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suicide"
      }
    ],
    "vmTrace": {
      "code": "0x611008ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem"
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
            "to": "0x616be8947699"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "+": "0x64"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x0"
        },
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suicide"
      }
    ],
    "vmTrace": {
      "code": "0x611008ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem"
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
            "to": "0x616be8947699"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "+": "0x64"
        },
        "code": "=",
        "nonce": {
          "+": "0x0"
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b346f44bd8acd496"
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suicide"
      }
    ],
    "vmT
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
            "to": "0x616be8947699"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "+": "0x64"
        },
        "code": "=",
        "nonce": {
          "+": "0x0"
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b346f44bd8acd496"
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suicide"
      }
    ],
    "vmT
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "*": {
            "from": "0x0",
            "to": "0x64"
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suicide"
      }
    ],
    "vmTrace": {
      "code": "0x611008ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x1008"
            ],
            "store": null,
            "used": 579000
          },
          "op": "PUSH2",
          "pc": 0,
          "su
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": {
      "0x0000000000000000000000000000000000001007": {
        "balance": {
          "*": {
            "from": "0x64",
            "to": "0x0"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001008": {
        "balance": {
          "*": {
            "from": "0x0",
            "to": "0x64"
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
          "to": "0x0000000000000000000000000000000000001007",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x7f5b",
          "output": "0x"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "call"
      },
      {
        "action": {
          "address": "0x0000000000000000000000000000000000001007",
          "balance": "0x64",
          "refundAddress": "0x0000000000000000000000000000000000001008"
        },
        "result": null,
        "subtraces": 0,
        "traceAddress": [
          0
        ],
        "type": "suicide"
      }
    ],
    "vmTrace": {
      "code": "0x611008ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x1008"
            ],
            "store": null,
            "used": 579000
          },
          "op": "PUSH2",
          "pc": 0,
          "su
… preview truncated; use the full evidence link above.
```

</details>

