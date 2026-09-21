# pruned/old-transaction

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738"
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

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-pruned-ready/observations.json).

- H06: **change_needed** — Unavailable historical state uses the proposed pruned-history error (4444).

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

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-pruned-ready/observations.json).

- H06: **change_needed** — Unavailable historical state uses the proposed pruned-history error (4444).

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

