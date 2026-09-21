# forks/replay-48

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x30",
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
- `2/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `2/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
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
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
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
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `2/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `2/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
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
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
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
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a8636459",
              "to": "0xc4f200cb8a8642ef5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b3487fa74fd56b6c",
              "to": "0xc097ce7bc90715b34876215b74acba"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x69",
              "to": "0x6a"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x5e",
              "to": "0x60"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x000000000000000000000000000000000000000000000000000000000000002f",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000030"
              }
            },
            "0xe4a5343defd03edb2197eb9f1cd10054aca57136763f2184634c37c60bb4d21b": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002f"
              }
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x11ba0",
            "input": "0xed74cd51ab28e765656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

