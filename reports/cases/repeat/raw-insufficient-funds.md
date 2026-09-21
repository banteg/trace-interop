# repeat/raw-insufficient-funds

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a80847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0aca7ebc30807b79807337959a904b47c9c067f725b99878e04064bbda2b253c3a03d83e51caa10aa91fc8422e47b95b7f8a2bbd409422f007a5bc93715e1de2b9e",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "insufficient funds for gas * price + value: address 0x5CbDd86a2FA8Dc4bDdd8a8f69dBa48572EeC07FB have 0 want 42000000000001"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- `trace/0`: {'action': {'callType': 'call', 'from': '0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb",
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

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- `trace/0`: {'action': {'callType': 'call', 'from': '0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb",
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

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
      "0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
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
          "callType": "call",
          "from": "0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb",
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

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

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
      "0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb": {
        "balance": {
          "+": "0x0"
        },
        "code": {
          "+": "0x"
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
          "callType": "call",
          "from": "0x5cbdd86a2fa8dc4bddd8a8f69dba48572eec07fb",
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

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **malformed_json**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **change_needed** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "raw_response": "{\"jsonrpc\":\"2.0\",\"result\":{\"vmTrace\":\"output\":null,\"stateDiff\":{},\"trace\":[]}",
  "status": "malformed_json"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **malformed_json**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **change_needed** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "raw_response": "{\"jsonrpc\":\"2.0\",\"result\":{\"vmTrace\":\"output\":null,\"stateDiff\":{},\"trace\":[]}",
  "status": "malformed_json"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32003,
    "message": "insufficient funds for gas * price + value: have 0 want 42000000000001"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32003,
    "message": "insufficient funds for gas * price + value: have 0 want 42000000000001"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

