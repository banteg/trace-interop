# a/many-storage-write-read

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "0x30"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0x66863b",
              "to": "0x4f20072fe2db"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34755ccb0391096",
              "to": "0xc097ce7bc90715b347069ba897d096"
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAd
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


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0x66863b",
              "to": "0x4f20072fe2db"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "vmTrace": null
    },
    {
      "output": "0x0000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0x66863b",
              "to": "0x4f20072fe2db"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "vmTrace": null
    },
    {
      "output": "0x0000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0x66863b",
              "to": "0x4f20072fe2db"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34755ccb0391096",
              "to": "0xc097ce7bc90715b347069ba897d096"
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAd
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0x66863b",
              "to": "0x4f20072fe2db"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34755ccb0391096",
              "to": "0xc097ce7bc90715b347069ba897d096"
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAd
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "vmTrace": null
    },
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": "=",
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x86",
              "to": "0x87"
            }
          },

… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "vmTrace": null
    },
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": "=",
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x86",
              "to": "0x87"
            }
          },

… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0x66863b",
              "to": "0x4f20072fe2db"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x0000000000000000000000000000000000001001": {
          "balance": "=",
          "code": "=",
          "nonce": "=",
          "storage": {
            "0x0000000000000000000000000000000000000000000000000000000000000000": {
              "*": {
                "from": "0x0000000000000000000000000000000000000000000000000000000000000000",
                "to": "0x000000000000000000000000000000000000000000000000000000000000002a"
              }
            }
          }
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34755ccb0391096",
              "to": "0xc097ce7bc90715b347069ba897d096"
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
            "gas": "0x8d4ac",
            "input": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
            "to": "0x0000000000000000000000000000000000001001",
            "value": "0x0"
          },
          "result": {
            "gasUsed": "0x56fc",
            "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
          },
          "subtraces": 0,
          "traceAd
… preview truncated; use the full evidence link above.
```

</details>

