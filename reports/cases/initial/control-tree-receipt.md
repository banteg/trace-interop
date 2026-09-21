# initial/control-tree-receipt

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getTransactionReceipt",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
    "blockNumber": "0x2",
    "contractAddress": null,
    "cumulativeGasUsed": "0x2e0e8",
    "effectiveGasPrice": "0x2da9cd6e",
    "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "gasUsed": "0x28647",
    "logs": [
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x0000000000000000000000000000000000000000000000000000000000000000",
        "logIndex": "0x0",
        "removed": false,
        "topics": [
          "0x00000000000000000000000000000000000000000000000000000000656d6974",
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x1",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000006368696c64"
        ],
        "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
        "transactionIndex": "0x1"
      },
      {
        "address": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
        "blockHash": "0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2",
        "blockNumber": "0x2",
        "blockTimestamp": "0x14",
        "data": "0x",
        "logIndex": "0x2",
        "removed": false,
        "topics": [
          "0x0000000000000000000000000000000000000000000000000000
… preview truncated; use the full evidence link above.
```

</details>

