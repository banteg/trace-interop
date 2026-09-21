# initial/call-identity

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x11223344",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000000004",
      "value": "0x0"
    },
    [
      "trace",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **change_needed** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **change_needed** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H22: **matches** — The identity precompile call frame preserves its input as return bytes.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x11223344",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x13458",
          "input": "0x11223344",
          "to": "0x0000000000000000000000000000000000000004",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x11223344"
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

