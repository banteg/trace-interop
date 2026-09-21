# a/filter-page-1

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 4,
      "count": 4,
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "out of gas: write protection",
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "Illegal state change",
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x00000000",
        "to": "0x7dcd1743
… preview truncated; use the full evidence link above.
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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "out of gas: write protection",
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x000000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "out of gas: write protection",
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "Static call violation",
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x00000000",
        "to": "0x7dcd174
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "Static call violation",
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x00000000",
        "to": "0x7dcd174
… preview truncated; use the full evidence link above.
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
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "StateChangeDuringStaticCall",
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x0000000
… preview truncated; use the full evidence link above.
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
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "StateChangeDuringStaticCall",
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x0000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).


Draft result schema: **invalid**.
- `1`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d2",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "gasUsed": "0x7d",
        "output": "0x0000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000c72dd9d5e883e0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002da9cd6d00000000000000000000000000000000000000000000000000000000000000000000000000000000000000007435ed30a8b4aeb0877cef0c6e8cffe834eb865f0000000000000000000000000000000000000000000000000000000000000000"
      },
      "subtraces": 0,
      "traceAddress": [
        2
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "staticcall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "error": "Illegal state change",
      "subtraces": 0,
      "traceAddress": [
        3
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "delegatecall",
        "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "gas": "0xea60",
        "input": "0x00000000",
        "to": "0x7dcd1743
… preview truncated; use the full evidence link above.
```

</details>

