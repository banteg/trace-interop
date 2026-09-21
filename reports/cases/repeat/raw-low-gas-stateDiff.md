# repeat/raw-low-gas-stateDiff

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b81858477359400824e2094000000000000000000000000000000000000123401808718e5bb3abd10a0a038e0b48a1022d5c55eea7e525942547d2009224ffa7ab6d1b40a5a16cb70a590a0279569cdb60041c1eac5043486547bdf086c64543c7e2d07870a288096213d33",
    [
      "stateDiff"
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
    "message": "intrinsic gas too low: have 20000, want 21000"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
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
    "stateDiff": null,
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
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
    "stateDiff": null,
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "intrinsic gas too low: have 20000, want 21000"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "intrinsic gas too low: have 20000, want 21000"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **malformed_json**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **change_needed** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "raw_response": "{\"jsonrpc\":\"2.0\",\"result\":{\"vmTrace\":null,\"output\":null,\"stateDiff\":{},\"trace\":[]}",
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
  "raw_response": "{\"jsonrpc\":\"2.0\",\"result\":{\"vmTrace\":null,\"output\":null,\"stateDiff\":{},\"trace\":[]}",
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
    "code": -32000,
    "message": "intrinsic gas too low"
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
    "code": -32000,
    "message": "intrinsic gas too low"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

