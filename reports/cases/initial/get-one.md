# initial/get-one

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x1"
    ]
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **invalid**.
- ``: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xea60",
      "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "error": "Reverted",
    "subtraces": 0,
    "traceAddress": [
      1
    ],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **invalid**.
- ``: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xea60",
      "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "error": "Reverted",
    "subtraces": 0,
    "traceAddress": [
      1
    ],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xea60",
      "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "error": "Reverted",
    "result": {
      "gasUsed": "0x889",
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
    },
    "subtraces": 0,
    "traceAddress": [
      1
    ],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xea60",
      "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
      "value": "0x0"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": 2,
    "error": "Reverted",
    "result": {
      "gasUsed": "0x889",
      "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72"
    },
    "subtraces": 0,
    "traceAddress": [
      1
    ],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **invalid**.
- ``: [{'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "subtraces": 0,
      "traceAddress": [
        1
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    }
  ]
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **invalid**.
- ``: [{'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x0000000000000000000000000000000000000000000000000000000000000001",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3",
        "value": "0x0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "error": "Reverted",
      "subtraces": 0,
      "traceAddress": [
        1
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xf35c",
      "input": "0xff01",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
      "value": "0x1"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
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
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [1], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xf35c",
      "input": "0xff01",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
      "value": "0x1"
    },
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
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
}
```

</details>

