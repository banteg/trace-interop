# pruned/old-nonce

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getTransactionCount",
  "params": [
    "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
    "0x2"
  ]
}
```

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-pruned/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32603,
    "message": "insufficient changesets to revert to block #2. Available changeset range: 43..=48"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-pruned/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32603,
    "message": "insufficient changesets to revert to block #2. Available changeset range: 43..=48"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

