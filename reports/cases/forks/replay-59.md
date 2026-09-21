# forks/replay-59

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x3b",
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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

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
              "from": "0xc4f200cb8a87b65f1",
              "to": "0xc4f200cb8a87bb7f9"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347de9f5073f34a",
              "to": "0xc097ce7bc90715b347ddbb96f2aa39"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x88",
              "to": "0x89"
            }
          },
          "storage": {}
        },
        "0xeda8645ba6948855e3b3cd596bbb07596d59c603": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b34b9f1000000000",
              "to": "0xc097ce7bc90715b34b9f1000000001"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        }
      },
      "trace": [
        {
          "action": {
            "callType": "call",
            "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
            "gas": "0x0",
            "input": "0x",
            "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
            "value": "0x1"
          },
          "result": {
            "gasUsed": "0x0",
            "output": "0x"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "call"
        }
      ],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87bb7f9",
              "to": "0xc4f200cb8a87c8295"

… preview truncated; use the full evidence link above.
```

</details>

