# initial/call-empty-types

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x0",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
    },
    [],
    "0x30"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H11: **matches** — An empty trace-type selection executes successfully.
- H15: **matches** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H11: **change_needed** — An empty trace-type selection executes successfully.
- H15: **change_needed** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32603,
    "message": "Internal error"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H11: **change_needed** — An empty trace-type selection executes successfully.
- H15: **change_needed** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32603,
    "message": "Internal error"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H11: **change_needed** — An empty trace-type selection executes successfully.
- H15: **change_needed** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, feeCap: 0 baseFee: 1677430"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H11: **change_needed** — An empty trace-type selection executes successfully.
- H15: **change_needed** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, feeCap: 0 baseFee: 1677430"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H11: **change_needed** — An empty trace-type selection executes successfully.
- H15: **change_needed** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32603,
    "data": "System.InvalidOperationException: Sequence contains no elements",
    "message": "Internal error"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H11: **change_needed** — An empty trace-type selection executes successfully.
- H15: **change_needed** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32603,
    "data": "System.InvalidOperationException: Sequence contains no elements\n   at System.Linq.ThrowHelper.ThrowNoElementsException()\n   at System.Linq.Enumerable.Aggregate[TSource](IEnumerable`1 source, Func`3 func)\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.GetParityTypes(String[] types) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 60\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.TraceTx(Transaction tx, String[] traceTypes, BlockParameter blockParameter, Dictionary`2 stateOverride) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 163\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.trace_call(TransactionForRpc call, String[] traceTypes, BlockParameter blockParameter, Dictionary`2 stateOverride) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 74\n   at Nethermind.JsonRpc.Modules.RpcModuleProvider.ResolvedMethodInfo.<>c__DisplayClass82_0`6.<CreateTypedDirectFourParameterInvoker>b__0(IRpcModule module, Object[] parameters) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/RpcModuleProvider.cs:line 608\n   at Nethermind.JsonRpc.JsonRpcService.ExecuteAsync(JsonRpcRequest request, String methodName, ResolvedMethodInfo method, JsonRpcContext context) in /nethermind/src/Nethermind/Nethermind.JsonRpc/JsonRpcService.cs:line 120",
    "message": "Internal error"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H11: **matches** — An empty trace-type selection executes successfully.
- H15: **matches** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H11: **matches** — An empty trace-type selection executes successfully.
- H15: **matches** — Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

