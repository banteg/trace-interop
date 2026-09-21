# forks/replay-35

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x23",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
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
              "from": "0xa688906bd8b27ba39",
              "to": "0xa688906bd8b287ca1"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f0fffd84562",
              "to": "0xc097ce7bc90715b34b9f0fffd782f8"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x47",
              "to": "0x48"
            }
          },
          "storage": {}
        },
        "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df": {
          "balance": {
            "*": {
              "from": "0x44",
              "to": "0x46"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000022",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000023"
              }
            },
            "0x2acfc92a1cc51397c95e434631e449d83a81de91964ed735a8c8b71b35e1a626": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x0000000000000000000000000000000000000000000000000000000000000022"
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
            "input": "0x95297b6a5c01e24f656d6974",
            "to": "0x7dcd17433742f4c0c
… preview truncated; use the full evidence link above.
```

</details>

