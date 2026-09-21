# forks/filter-35

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x23",
      "toBlock": "0x23"
    }
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": null,
      "transactionPosition": null,
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": null,
      "transactionPosition": null,
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber":
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber":
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property

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
        "gas": "0x133d8",
        "input": "0x95297b6a5c01e24f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x38287a4cde4cb8f1b78c6c29880a5721ddda573f6d15413753a1e0546b996c1d",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "value": "0x1"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0c68db54417efe088e4000b2c274e0ae72f58d3fb80be5274f4dde231fb0b53d",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
      "blockNumber": 35,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "uncle",
        "value": "0x18493fba64ef0000"
      },
      "blockHash": "0x652135e6008aa5a27ab49a5236608117fb6bfe518fd606df0e3cd83fafa8834f",
… preview truncated; use the full evidence link above.
```

</details>

