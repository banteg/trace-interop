# forks/filter-across-60

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x3b",
      "toBlock": "0x3c"
    }
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json).

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transact
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **change_needed** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0',
- `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x696e766f6b6564', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'ga
- `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb917cfdc0d25b72d55cf94db328e1629b7f4fde2c30cdacf873b664416f76a0c7f7cc50c9f72a3cb84be88144cde91250000000000000d80', 'to': '0x00000961ef480eb55e80d19ad83579a64c007002', 'value': '0x3b9aca00'}, 'blockHash'
- `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": null,
      "transactionPosition": null,
      "type": "reward"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **change_needed** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0',
- `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x696e766f6b6564', 'to': '0xeda8645ba6948855e3b3cd596bbb07596d59c603', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'ga
- `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb917cfdc0d25b72d55cf94db328e1629b7f4fde2c30cdacf873b664416f76a0c7f7cc50c9f72a3cb84be88144cde91250000000000000d80', 'to': '0x00000961ef480eb55e80d19ad83579a64c007002', 'value': '0x3b9aca00'}, 'blockHash'
- `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'result': {'gasUsed': '0x0

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": null,
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": null,
      "transactionPosition": null,
      "type": "reward"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transact
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transact
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- `8`: 'transactionHash' is a required property
- `8`: 'transactionPosition' is a required property

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A fork-crossing range equals the corresponding per-block traces.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property
- `7`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- `8`: 'transactionHash' is a required property
- `8`: 'transactionPosition' is a required property

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "subtraces": 0,
      "traceAddress": [],
      "type": "reward"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transact
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

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
        "gas": "0x0",
        "input": "0x",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x1"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x03a4bc78840db70e9b34ed52a9b17a34d4c72011731e9d7c36c962cda16c5b17",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xf85dd3506d5b50b3656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xd0f4ccca39ffd79d7c48147bafc9c46c839936205cd8bd01f62be5a3e3ed332b",
      "blockNumber": 59,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xfaf95f0248bf8587ba17feda97333e872894f94ab3b418bfab84287e76d89b79",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transact
… preview truncated; use the full evidence link above.
```

</details>

