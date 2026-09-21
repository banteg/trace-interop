# forks/replay-56

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x38",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json).


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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "+": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
            "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
            "value": "0x3"
          },
          "result": {
            "gasUsed": "0x5f9c",
            "
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
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
              "from": "0xc4f200cb8a8742bfd",
              "to": "0xc4f200cb8a874f699"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347f875eff99958",
              "to": "0xc097ce7bc90715b347f52eeae14655"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7f",
              "to": "0x80"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6e",
              "to": "0x71"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000037",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000038"
              }
            },
            "0xfa29cff134420b6526f434ab690a9c3a140aa27b8479ae3d8d83b6c799acbc23": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
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
            "input": "0x74fb911b03a9f447656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

