# a/get-path-wrong-type

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "0x6"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid trace numbers params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **not_observed**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "invalid argument 1: json: cannot unmarshal string into Go value of type []hexutil.Uint64"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "invalid argument 1: json: cannot unmarshal string into Go value of type []hexutil.Uint64"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

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

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

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

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "invalid type: string \"0x6\", expected a sequence at line 1 column 6",
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H14: **matches** — Malformed input returns invalid params (-32602).

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "invalid type: string \"0x6\", expected a sequence at line 1 column 6",
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

