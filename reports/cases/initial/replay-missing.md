# initial/replay-missing

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe",
    [
      "trace"
    ]
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

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

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": null
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": null
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe receipt could not be found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe receipt could not be found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32001,
    "message": "transaction not found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32001,
    "message": "transaction not found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

