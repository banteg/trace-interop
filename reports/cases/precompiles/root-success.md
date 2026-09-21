# precompiles/root-success

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "to": "0x0000000000000000000000000000000000000006"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-precompiles/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x143ac445f88b"
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
            "to": "0xc097ce7bc90715b347418938bcc096"
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
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

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x143ac445f88b"
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
            "to": "0xc097ce7bc90715b347418938bcc096"
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x143ac445f88b"
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
            "to": "0xc097ce7bc90715b347418938bcc096"
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x13ab1e646167"
          }
        },
        "code": "=",
        "nonce": "=",
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x13ab1e646167"
          }
        },
        "code": "=",
        "nonce": "=",
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x143ac445f88b"
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
            "to": "0xc097ce7bc90715b347418938bcc096"
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x143ac445f88b"
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
            "to": "0xc097ce7bc90715b347418938bcc096"
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/precompiles-final/observations.json).

- H08: **matches** — Output remains a byte string under every trace selection.
- H29: **matches** — Retain the root precompile frame, even with zero value.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
    "stateDiff": {
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
          "gas": "0xfabf8",
          "input": "0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
          "to": "0x0000000000000000000000000000000000000006",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x96",
          "output": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

