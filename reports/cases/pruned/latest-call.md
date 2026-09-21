# pruned/latest-call

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "to": "0x0000000000000000000000000000000000001002"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-pruned/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": null
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-pruned/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": null
  }
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-pruned-ready/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": null
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-pruned-ready/observations.json).

- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x000000000000000000000000000000000000000000000000000000000000002a",
    "stateDiff": null,
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x8d5b8",
          "input": "0x",
          "to": "0x0000000000000000000000000000000000001002",
          "value": "0x0"
        },
        "result": {
          "gasUsed": "0x12",
          "output": "0x000000000000000000000000000000000000000000000000000000000000002a"
        },
        "subtraces": 0,
        "traceAddress": [],
        "type": "call"
      }
    ],
    "vmTrace": null
  }
}
```

</details>

