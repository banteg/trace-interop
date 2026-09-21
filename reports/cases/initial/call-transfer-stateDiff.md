# initial/call-transfer-stateDiff

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001234",
      "value": "0x1"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).

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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
            "to": "0xc097ce7bc90715b3472f99cd247095"
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
            "to": "0xc097ce7bc90715b3472f99cd247095"
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
            "to": "0xc097ce7bc90715b3472f99cd247095"
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **change_needed** — Unrequested trace is an empty array.
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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
      }
    },
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13498",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001234",
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
    "vmTrace": null
  }
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **change_needed** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- `output`: None is not of type 'string'

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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
            "to": "0xc097ce7bc90715b3472f99cd247095"
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **change_needed** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- `output`: None is not of type 'string'

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
            "from": "0x66863b",
            "to": "0x262aafd8968b"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x0000000000000000000000000000000000001234": {
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
            "to": "0xc097ce7bc90715b3472f99cd247095"
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
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

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
      "0x0000000000000000000000000000000000001234": {
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
      "0x0000000000000000000000000000000000001234": {
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
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

