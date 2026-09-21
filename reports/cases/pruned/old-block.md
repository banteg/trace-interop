# pruned/old-block

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
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
    "message": "failed to apply blockhash contract call: database error: Database error: insufficient changesets to revert to block #1. Available changeset range: 43..=48"
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
    "message": "failed to apply blockhash contract call: database error: Database error: insufficient changesets to revert to block #1. Available changeset range: 43..=48"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

