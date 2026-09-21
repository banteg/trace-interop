# forks/replay-55

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x37",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-forks/observations.json).


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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "+": "0x0000000000000000000000000000000000000000000000000000000000000036"
            }
          }
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
            "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
            "value": "0x2"
          },
          "result": {
            "gasUsed": "0x6fa0",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
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
              "from": "0xc4f200cb8a873178d",
              "to": "0xc4f200cb8a873d9f5"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347fd92168049bb",
              "to": "0xc097ce7bc90715b347f9fa1fa3cba9"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x7d",
              "to": "0x7e"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x6c",
              "to": "0x6e"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000036",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000037"
              }
            },
            "0x8460e232c64e6cd9f816c02d855c892755984ebbb91592e683cda80aaba4ba22": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000036"
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
            "gas": "0x133d8",
            "input": "0xe62b8536019651e7656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

