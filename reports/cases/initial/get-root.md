# initial/get-root

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    []
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x8d5b8",
      "input": "0x",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "result": {
      "gasUsed": "0x2343f",
      "output": "0xffee"
    },
    "subtraces": 7,
    "traceAddress": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x8d5b8",
      "input": "0x",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "result": {
      "gasUsed": "0x2343f",
      "output": "0xffee"
    },
    "subtraces": 7,
    "traceAddress": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x8d5b8",
      "input": "0x",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "result": {
      "gasUsed": "0x2343f",
      "output": "0xffee"
    },
    "subtraces": 7,
    "traceAddress": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "method handler crashed"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

Draft result schema: **invalid**.
- ``: [] is not valid under any of the given schemas

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": []
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

Draft result schema: **invalid**.
- ``: [] is not valid under any of the given schemas

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": []
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

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

