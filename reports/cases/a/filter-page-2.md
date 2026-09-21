# a/filter-page-2

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": 8,
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


Draft result schema: **invalid**.
- `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

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
        "gasUsed": "0x1682",
        "output": "0x"
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287d
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb839e77eb05b37b34ce5eb2
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb839e77eb05b37b34ce5eb2
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287dbb
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).


Draft result schema: **invalid**.
- `0`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

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
        "gasUsed": "0x1682",
        "output": "0x"
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
        "address": "0x2d303c5b7911d87d594bf1b31fbb9aa187888893",
        "balance": "0x0",
        "refundAddress": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": null,
      "subtraces": 0,
      "traceAddress": [
        6,
        0
      ],
      "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
      "transactionPosition": 1,
      "type": "suicide"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "blockNumber": 2,
      "result": {
        "address": "0x4055cae5c7d838cda10d40f9d07106c7f5f3be1c",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x512b5deddff16d21ebba7b730d935b4287d
… preview truncated; use the full evidence link above.
```

</details>

