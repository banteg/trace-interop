# forks/replay-60

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x3c",
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
- `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x08c379a000000000000000000000000000000000000000000000000000000000000000

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
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
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
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
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


Draft result schema: **invalid**.
- `4/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given s

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
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
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
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
      "output": "0x36156009575f355f555b305f525f5460205260405ff3",
      "stateDiff": {
        "0x0000000000000000000000000000000000000000": {
          "balance": {
            "*": {
              "from": "0xc4f200cb8a87c8295",
              "to": "0xc4f200cb8a87d6506"
            }
          },
          "code": "=",
          "nonce": "=",
          "storage": {}
        },
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
          "balance": {
            "*": {
              "from": "0xc097ce7bc90715b347db8921a7a37e",
              "to": "0xc097ce7bc90715b347d96308a8436d"
            }
          },
          "code": "=",
          "nonce": {
            "*": {
              "from": "0x8a",
              "to": "0x8b"
            }
          },
          "storage": {}
        },
        "0xfdb19a177ed1b386d141e392b7a27467469fabb2": {
          "balance": {
            "+": "0x0"
          },
          "code": {
            "+": "0x36156009575f355f555b305f525f5460205260405ff3"
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
            "gas": "0x4b0e",
            "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
            "value": "0x0"
          },
          "result": {
            "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
            "code": "0x36156009575f355f555b305f525f5460205260405ff3",
            "gasUsed": "0x114d"
          },
          "subtraces": 0,
          "traceAddress": [],
          "type": "create"
        }
      ],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "vmTrace": null
    },
    {
      "output": "0x",
      "stateDiff": {
        "0x00000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

