# initial/replay-transfer-stateDiff

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    [
      "stateDiff"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

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
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "vmTrace": null
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H01: **unsupported** — trace_replayTransaction

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H01: **unsupported** — trace_replayTransaction

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

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
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "vmTrace": null
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

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
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "vmTrace": null
  }
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **change_needed** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- ``: {'output': None, 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xe1f93', 'to': '0xe719b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b349381db4bf5a19', 'to': '0xc097c

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": null,
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "vmTrace": null
  }
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **change_needed** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- ``: {'output': None, 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xe1f93', 'to': '0xe719b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b349381db4bf5a19', 'to': '0xc097c

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": null,
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "vmTrace": null
  }
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **change_needed** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- ``: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xe1f93', 'to': '0xe719b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b349381db4bf5a19', 'to': '0xc097c

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
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **change_needed** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- ``: {'output': '0x', 'stateDiff': {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xe1f93', 'to': '0xe719b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b349381db4bf5a19', 'to': '0xc097c

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
            "from": "0xe1f93",
            "to": "0xe719b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b349381db4bf5a19",
            "to": "0xc097ce7bc90715b3492e4b610902b0"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xf",
            "to": "0x10"
          }
        },
        "storage": {}
      },
      "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d": {
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

