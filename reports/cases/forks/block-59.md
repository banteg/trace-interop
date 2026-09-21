# forks/block-59

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x3b"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.

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
    }
  ]
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.

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
    }
  ]
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.

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
    }
  ]
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.

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
    }
  ]
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property

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
    }
  ]
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.

Draft result schema: **invalid**.
- `2`: 'transactionHash' is a required property
- `2`: 'transactionPosition' is a required property

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
    }
  ]
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.

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
    }
  ]
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.

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
    }
  ]
}
```

</details>

