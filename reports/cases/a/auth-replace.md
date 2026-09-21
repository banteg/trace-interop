# a/auth-replace

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0x04f8d4870c72dd9d5e883e818501847735940083030d409419e7e376e7c213b7e7e7e46cc70a5dd086daff2a8080c0f863f861870c72dd9d5e883e9400000000000000000000000000000000000010038080a032b48971f74add2ebe91ce111113ff37b7f8d272ed23134e89aa7658b677ca45a05bc973423f88f2644a49fa4509864691835ff138f284a233ecba072e79dfb5f580a0d69accc0eaf71c8a02bf2b11adb6644f9b694243463e8300fc88feeff61f8884a02f3f0627d55d5268f16db3cef6ef2636ee568713e5a631e7f73656f3c0d26d76",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 153997
          },
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cos
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

Draft result schema: **invalid**.
- `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid unde

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "revertReason": "0x",
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 153997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [

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

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

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
            "to": "0x6739f1"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 153997
          },
          "idx": "0",
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "stor
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

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
            "to": "0x6739f1"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 153997
          },
          "idx": "0",
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "stor
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

Draft result schema: **invalid**.
- `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given sch
- `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 153997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

Draft result schema: **invalid**.
- `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given sch
- `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 153997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],

… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **change_needed** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0xef01000000000000000000000000000000000000001002",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 154000
          },
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",

… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **change_needed** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "result": {
          "gasUsed": "0x6",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0xef01000000000000000000000000000000000000001002",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 154000
          },
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
- H18: **matches** — EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.

Draft result schema: **invalid**.
- `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid unde

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
            "to": "0x671600"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a": {
        "balance": "=",
        "code": {
          "*": {
            "from": "0xef01000000000000000000000000000000000000001002",
            "to": "0xef01000000000000000000000000000000000000001003"
          }
        },
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
          }
        },
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34755be505c4403"
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
          "gas": "0x25990",
          "input": "0x",
          "to": "0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a",
          "value": "0x0"
        },
        "error": "Reverted",
        "revertReason": "0x",
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x60006000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 153997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [

… preview truncated; use the full evidence link above.
```

</details>

