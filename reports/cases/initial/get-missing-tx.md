# initial/get-missing-tx

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_get",
  "params": [
    "0xfefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefefe",
    []
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).

- H06: **matches** — A missing transaction or tree path returns null.
- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

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

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **matches** — A missing transaction or tree path returns null.
- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

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

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **matches** — A missing transaction or tree path returns null.
- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

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

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **matches** — A missing transaction or tree path returns null.
- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

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

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **change_needed** — A missing transaction or tree path returns null.
- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

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

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **change_needed** — A missing transaction or tree path returns null.
- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "System.ArgumentNullException: Value cannot be null. (Parameter 'source')",
    "message": "Value cannot be null. (Parameter 'source')"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **change_needed** — A missing transaction or tree path returns null.
- H06: **change_needed** — Unknown transaction returns null, not an empty collection or RPC error.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "System.ArgumentNullException: Value cannot be null. (Parameter 'source')\n   at System.Linq.ThrowHelper.ThrowArgumentNullException(ExceptionArgument argument)\n   at System.Linq.Enumerable.<ToArray>g__EnumerableToArray|324_0[TSource](IEnumerable`1 source)\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.ExtractPositionsFromTxTrace(Int64[] positions, ResultWrapper`1 traceTransaction) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 403\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.trace_get(Hash256 txHash, Int64[] positions) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 396\n   at Nethermind.JsonRpc.Modules.RpcModuleProvider.ResolvedMethodInfo.<>c__DisplayClass80_0`4.<CreateTypedDirectTwoParameterInvoker>b__0(IRpcModule module, Object[] parameters) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/RpcModuleProvider.cs:line 596\n   at Nethermind.JsonRpc.JsonRpcService.ExecuteAsync(JsonRpcRequest request, String methodName, ResolvedMethodInfo method, JsonRpcContext context) in /nethermind/src/Nethermind/Nethermind.JsonRpc/JsonRpcService.cs:line 120",
    "message": "Value cannot be null. (Parameter 'source')"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H06: **matches** — A missing transaction or tree path returns null.
- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

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

- H06: **matches** — A missing transaction or tree path returns null.
- H06: **matches** — Unknown transaction returns null, not an empty collection or RPC error.

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

