# a/filter-suicide-from

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x2d303c5b7911d87d594bf1b31fbb9aa187888893"
      ],
      "fromBlock": "0x2",
      "toBlock": "0x2"
    }
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H23: **change_needed** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": []
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

- H23: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
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
    }
  ]
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H23: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
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
    }
  ]
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H23: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
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
    }
  ]
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H23: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
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
    }
  ]
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H23: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
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
    }
  ]
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H23: **matches** — Address matching is OR within each list, AND across lists, with action-specific endpoints.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
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
    }
  ]
}
```

</details>

