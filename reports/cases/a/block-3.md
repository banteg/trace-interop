# a/block-3

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x3"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-a/observations.json).

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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.

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
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.

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
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).

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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).

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
        "gas": "0x11ba0",
        "input": "0xdc4c8669df128318656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x54ac",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x4845366f3ccc487743b759a1d23f430b405e5e56cd50e1a77ce6c2124dcfe842",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x3f446a7c4145b1f0656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc02888b29321d89ffec6d3796f1e0d5b182999c26cd6a8e49ccad72db305ae7",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x96fd14b8fdcbd4a9656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0x01ba2f0e16a94e375a460eb303af615daf77ddfac7cc9d9cef96f22a6a095364",
      "blockNumber": 3,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xf02ed84381c81d780bc5a5198252284fe9e1cbd6b108573049a35957cc
… preview truncated; use the full evidence link above.
```

</details>

