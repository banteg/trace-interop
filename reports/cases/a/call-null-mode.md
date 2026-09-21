# a/call-null-mode

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
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001002"
    },
    null,
    "0x30"
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "missing value for required argument 1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid trace type params"
  },
  "id": 1,
  "jsonrpc": "2.0"
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

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "missing value for required argument 1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


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

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "missing value for required argument 1"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "System.ArgumentNullException: Value cannot be null. (Parameter 'source')\n   at System.Linq.ThrowHelper.ThrowArgumentNullException(ExceptionArgument argument)\n   at System.Linq.Enumerable.Select[TSource,TResult](IEnumerable`1 source, Func`2 selector)\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.GetParityTypes(String[] types) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 60\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.TraceTx(Transaction tx, String[] traceTypes, BlockParameter blockParameter, Dictionary`2 stateOverride) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 163\n   at Nethermind.JsonRpc.Modules.Trace.TraceRpcModule.trace_call(TransactionForRpc call, String[] traceTypes, BlockParameter blockParameter, Dictionary`2 stateOverride) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs:line 74\n   at Nethermind.JsonRpc.Modules.RpcModuleProvider.ResolvedMethodInfo.<>c__DisplayClass82_0`6.<CreateTypedDirectFourParameterInvoker>b__0(IRpcModule module, Object[] parameters) in /nethermind/src/Nethermind/Nethermind.JsonRpc/Modules/RpcModuleProvider.cs:line 608\n   at Nethermind.JsonRpc.JsonRpcService.ExecuteAsync(JsonRpcRequest request, String methodName, ResolvedMethodInfo method, JsonRpcContext context) in /nethermind/src/Nethermind/Nethermind.JsonRpc/JsonRpcService.cs:line 120",
    "message": "Value cannot be null. (Parameter 'source')"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "invalid type: null, expected a sequence at line 1 column 5",
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "data": "invalid type: null, expected a sequence at line 1 column 5",
    "message": "Invalid params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json).


<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32602,
    "message": "Invalid trace type params"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

