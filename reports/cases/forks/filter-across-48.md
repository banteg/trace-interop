# forks/filter-across-48

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2f",
      "toBlock": "0x30"
    }
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property
- `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':
- `7`: 'transactionHash' is a required property
- `7`: 'transactionPosition' is a required property

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber":
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property
- `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':
- `7`: 'transactionHash' is a required property
- `7`: 'transactionPosition' is a required property

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber":
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

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
        "input": "0xea41c6626bd2d71a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4ba8c63a6eb76028beb54b621d0aebcb4408b53cfe3221a03426c5d5940d5107",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
        "value": "0x1"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa263812c1fe6b84efc195c1762cb0f4fccb198b1b5657df7b435e3343bcab1fa",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x1c9f78d2893e4000"
      },
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
      "blockNumber": 47,
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
      "blockHash": "0x7ba4b92a97028c329d74e5d99aa0abbe4d3c62af083d8f8847e4a84fe4d34826",
… preview truncated; use the full evidence link above.
```

</details>

