# forks/filter-56

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x38",
      "toBlock": "0x38"
    }
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json).

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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H27: **matches** — A single-block filter agrees with trace_block at the same fork.

Draft result schema: **invalid**.
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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

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
        "gas": "0x11ba0",
        "input": "0x74fb911b03a9f447656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x485156c6fb5117ef740b7f2fd07fa3b59aaa8f63268e2f6b55663a5e532bd2d5",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x0e3c9c409810ef1d656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x49771ec1756a3196f6302d643791d97e345923ecb628472fe369a7895e3d9ef3",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x133d8",
        "input": "0xaea813e13a3d0897656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xf3be11c8f8d9b2ba562c673badb50687e003b8d747b7054e57503a2d1d4b7cc3",
      "blockNumber": 56,
      "result": {
        "gasUsed": "0x6fa0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x3af8b2d42d7d74bb5ce1c5e9043f767d0808e4a269784db66f09ede
… preview truncated; use the full evidence link above.
```

</details>

