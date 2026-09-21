# initial/raw-valid

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a80847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a04c833abdb116ad76fc98610ae0e626d7e35154f1fba38ce6bfdaf69a31eec42ca035ecfb996cc68a2a03df0e1087194e25180b01bf0469f69b4f1d330eea9d027a",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x0"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid number of params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid number of params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "too many arguments, want at most 2"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "too many arguments, want at most 2"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H12: **change_needed** — The two-argument baseline rejects an extra block selector (extension policy remains open).

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
            "from": "0x0",
            "to": "0x1319718a5000"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
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
            "from": "0xc097ce7bc90715b34b9f1000000000",
            "to": "0xc097ce7bc90715b34b78dd1ceb5fff"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
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
          "gas": "0x0",
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
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H12: **change_needed** — The two-argument baseline rejects an extra block selector (extension policy remains open).

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
            "from": "0x0",
            "to": "0x1319718a5000"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
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
            "from": "0xc097ce7bc90715b34b9f1000000000",
            "to": "0xc097ce7bc90715b34b78dd1ceb5fff"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
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
          "gas": "0x0",
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
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid number of params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid number of params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "too many arguments, want at most 2"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "too many arguments, want at most 2"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H12: **matches** — The two-argument baseline rejects an extra block selector (extension policy remains open).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H12: **change_needed** — The two-argument baseline rejects an extra block selector (extension policy remains open).

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
            "from": "0x0",
            "to": "0x1319718a5000"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
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
            "from": "0xc097ce7bc90715b34b9f1000000000",
            "to": "0xc097ce7bc90715b34b78dd1ceb5fff"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
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
          "gas": "0x0",
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
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.
- H12: **change_needed** — The two-argument baseline rejects an extra block selector (extension policy remains open).

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
            "from": "0x0",
            "to": "0x1319718a5000"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
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
            "from": "0xc097ce7bc90715b34b9f1000000000",
            "to": "0xc097ce7bc90715b34b78dd1ceb5fff"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x0",
            "to": "0x1"
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
          "gas": "0x0",
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
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

