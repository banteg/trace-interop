# a/get-integer-path

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      6,
      0
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "invalid argument 1: json: cannot unmarshal non-string into Go value of type hexutil.Uint64"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


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


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "invalid argument 1: json: cannot unmarshal non-string into Go value of type hexutil.Uint64"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "invalid argument 1: json: cannot unmarshal non-string into Go value of type hexutil.Uint64"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **invalid**.
- ``: [{'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0x6a00f",
        "init": "0x5b646368696c6460006000a133ff",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "code": "0x",
        "gasUsed": "0x1682"
      },
      "subtraces": 1,
      "traceAddress": [
        6
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xf35c",
        "input": "0xff01",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
        "value": "0x1"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x48",
        "output": "0xffee"
      },
      "subtraces": 0,
      "traceAddress": [
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    }
  ]
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


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

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


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

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).


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

