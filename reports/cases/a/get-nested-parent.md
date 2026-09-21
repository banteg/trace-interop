# a/get-nested-parent

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "0x6"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-a/observations.json).

- H02: **matches** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H02: **matches** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **invalid**.
- ``: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
  }
}
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

- H02: **matches** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H02: **matches** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
  }
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **invalid**.
- ``: [{'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d

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
    }
  ]
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **invalid**.
- ``: [{'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d

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
    }
  ]
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "callcode",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xea60",
      "input": "0xff01",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
      "value": "0x0"
    },
    "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
    "blockNumber": 2,
    "result": {
      "gasUsed": "0x48",
      "output": "0xffee"
    },
    "subtraces": 0,
    "traceAddress": [
      5
    ],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H02: **change_needed** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "callcode",
      "from": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0xea60",
      "input": "0xff01",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1",
      "value": "0x0"
    },
    "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
    "blockNumber": 2,
    "result": {
      "gasUsed": "0x48",
      "output": "0xffee"
    },
    "subtraces": 0,
    "traceAddress": [
      5
    ],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).

- H02: **matches** — Return the transaction-tree record at [6], or null if absent.

Draft result schema: **invalid**.
- ``: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a00f', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result': {'address': '0x2d3

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
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
  }
}
```

</details>

