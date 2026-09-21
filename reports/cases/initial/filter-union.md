# initial/filter-union

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "fromBlock": "0x2",
      "mode": "union",
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "toBlock": "0x2"
    }
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid filter params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid filter params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
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
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
      "type": "call"
    },
    {
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
    },
    {
      "action": {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
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
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
      "type": "call"
    },
    {
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
    },
    {
      "action": {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
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
  ]
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
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
  ]
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
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
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
      "type": "call"
    },
    {
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
    },
    {
      "action": {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x13488",
        "input": "0x01",
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
      "traceAddress": [],
      "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
      "transactionPosition": 0,
      "type": "call"
    },
    {
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
    },
    {
      "action": {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e
… preview truncated; use the full evidence link above.
```

</details>

