# initial/get-transfer-root

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    []
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x0",
      "input": "0x",
      "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
      "value": "0x1"
    },
    "blockHash": "0xc0324d9acd44e47557c69ccd5860ef02090301b272dff3f940972f2cf186e698",
    "blockNumber": 5,
    "result": {
      "gasUsed": "0x0",
      "output": "0x"
    },
    "subtraces": 0,
    "traceAddress": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x0",
      "input": "0x",
      "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
      "value": "0x1"
    },
    "blockHash": "0xc0324d9acd44e47557c69ccd5860ef02090301b272dff3f940972f2cf186e698",
    "blockNumber": 5,
    "result": {
      "gasUsed": "0x0",
      "output": "0x"
    },
    "subtraces": 0,
    "traceAddress": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x0",
      "input": "0x",
      "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
      "value": "0x1"
    },
    "blockHash": "0xc0324d9acd44e47557c69ccd5860ef02090301b272dff3f940972f2cf186e698",
    "blockNumber": 5,
    "result": {
      "gasUsed": "0x0",
      "output": "0x"
    },
    "subtraces": 0,
    "traceAddress": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **matches** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "action": {
      "callType": "call",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x0",
      "input": "0x",
      "to": "0xd803681e487e6ac18053afc5a6cd813c86ec3e4d",
      "value": "0x1"
    },
    "blockHash": "0xc0324d9acd44e47557c69ccd5860ef02090301b272dff3f940972f2cf186e698",
    "blockNumber": 5,
    "result": {
      "gasUsed": "0x0",
      "output": "0x"
    },
    "subtraces": 0,
    "traceAddress": [],
    "transactionHash": "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    "transactionPosition": 1,
    "type": "call"
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "method handler crashed"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

Draft result schema: **invalid**.
- ``: [] is not valid under any of the given schemas

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": []
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

Draft result schema: **invalid**.
- ``: [] is not valid under any of the given schemas

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": []
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": null
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H02: **change_needed** — Return one object whose traceAddress equals [].

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": null
}
```

</details>

