# forks/block-55

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x37"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json).

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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
      "transactionPosition": 1,
      "type": "call"
    }
  ]
}
```

</details>

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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "author": "0x0000000000000000000000000000000000000000",
        "rewardType": "block",
        "value": "0x0"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
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
        "gas": "0x133d8",
        "input": "0xe62b8536019651e7656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xa7a765e9f45b0ddcc07a023677846e2bfeb53f68ebb3deb3bcbfda3a6754f803",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c",
        "value": "0x1"
      },
      "blockHash": "0x5dc7c1de0ff322c333c1423839ad72ee157f2c8c21bd61ec57cd7a44288fa7ee",
      "blockNumber": 55,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xe4c4e6a9105669372c4eb7fe40af9f521ee1f58d6b0f73d85f32af95189c3876",
      "transactionPosition": 1,
      "type": "call"
    }
  ]
}
```

</details>

