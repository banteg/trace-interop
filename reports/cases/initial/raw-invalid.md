# initial/raw-invalid

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0x00",
    [
      "trace"
    ]
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid transaction params (missing or incorrect)"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid transaction params (missing or incorrect)"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **change_needed** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "short input: 1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **change_needed** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "short input: 1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **change_needed** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "Invalid RLP."
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **change_needed** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "Invalid RLP."
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "failed to decode signed transaction"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "failed to decode signed transaction"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

