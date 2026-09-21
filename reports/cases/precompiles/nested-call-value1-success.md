# precompiles/nested-call-value1-success

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6000600052604060006080600060016006620186a0f15060006000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-precompiles/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b347082612dc7c95"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **change_needed** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b347082612dc7c95"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "create"
      }
    ],
    "vmTrace": {
      "code": "0x6000600052604060006080600060016006620186a0f15060006000f3",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 995195

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **change_needed** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b347082612dc7c95"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "create"
      }
    ],
    "vmTrace": {
      "code": "0x6000600052604060006080600060016006620186a0f15060006000f3",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 995195

… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b34755ccb0391095"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b34755ccb0391095"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- `vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f15060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995195}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995192}, 'pc': 2, 'sub': None}, {'cost': 6,

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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b347082612dc7c95"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": "=",
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- `vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f15060006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995195}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995192}, 'pc': 2, 'sub': None}, {'cost': 6,

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
            "to": "0x4d854572304f"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "+": "0x1"
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
            "to": "0xc097ce7bc90715b347082612dc7c95"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": "=",
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "*": {
            "from": "0x0",
            "to": "0x1"
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
            "to": "0xc097ce7bc90715b34755ccb0391095"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- H24: **matches** — A handled precompile failure must not mark the successful parent as failed.
- H10: **matches** — Successful creation uses address, code and gasUsed.
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
      "0x0000000000000000000000000000000000000006": {
        "balance": {
          "*": {
            "from": "0x0",
            "to": "0x1"
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
            "to": "0xc097ce7bc90715b34755ccb0391095"
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
      },
      "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
        },
        "nonce": {
          "+": "0x1"
        },
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "creationMethod": "create",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0xf2f7e",
          "init": "0x6000600052604060006080600060016006620186a0f15060006000f3",
          "value": "0x1"
        },
        "result": {
          "address": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "code": "0x",
          "gasUsed": "0x7d00"
        },
        "subtraces": 1,
        "traceAddress": [],
        "type": "create"
      },
      {
        "action": {
          "callType": "call",
          "from": "0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41",
          "gas": "0x18f9c",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x
… preview truncated; use the full evidence link above.
```

</details>

