# Nethermind truncated validation responses

The 2026-09-24 H15 capture exposes a deferred execution error in Nethermind's
streamed trace responses. Fee/funding validation rejects the request internally,
but its exception escapes after the writer has started a success envelope. The
captured response therefore lacks its request ID and outer closing brace.

## Fresh confirmation

The [12:56 UTC matrix](../evidence/2026-09-24/h15-call-compat/README.md)
reproduces the same 203 release / 232 development malformed responses in
`fee-policy`, now with development `641592d2`. The paired `fee-compat` corpus
adds 84 / 96 malformed trace responses. Its identical `eth_call` requests return
complete fee/funding errors, locating the observable discrepancy in the trace
path. The source investigation below remains pinned to the original capture.

## Captured evidence

Counts below use the immutable [fee-policy responses](../evidence/2026-09-24/current-matrix/fee-policy/observations.json.gz)
and the corresponding client logs. The number of malformed responses equals
the number of unhandled `InvalidTransactionException` entries in each build's log.

| Tested build | Malformed responses | Base-fee exceptions | Funding exceptions |
|---|---:|---:|---:|
| 2.0.0 · bec830cd | 203 | 112 | 91 |
| 2.1.0-unstable · 2a3b2531 | 232 | 128 | 104 |

The 29 additional malformed development responses all have empty trace selections.
The release build fails those same requests earlier with `Sequence contains no
elements`; the development build fixes that failure and reaches fee/funding
validation. This explains the increase without implying a new fee-policy regression.

For example, [legacy-one/call/none](../reports/cases/fee-policy/legacy-one/call/none.md)
supplies `gasPrice: 1` against a block base fee of 765,625,000 wei. Development
returns this exact incomplete body:

```text
{"jsonrpc":"2.0","result":{"vmTrace":null,"output":null,"stateDiff":null,"trace":[]}
```

The equivalent `trace_callMany` body closes its inner array but still omits the
outer envelope's ID and closing brace. Other affected cases include insufficient
funds and a later call becoming invalid in a sequential batch. These failures
occur with all eight trace selections in the development build.

The [development log](../evidence/2026-09-24/current-matrix/fee-policy/hive/nethermind_development/client-f81f721dc18c9bed67e9fdbf4df01b4e9ae4b729bc7d2dea80935759d5b5f66a.log.gz) (line 603)
records the rejected fee/funding condition, followed by a stack through trace
execution, `StreamingResultBase.WriteJsonToAsync`,
`JsonRpcResponseWriter.WriteStreamableAsync` and the HTTP response sink.
The log's two error descriptions are `max fee per gas less than block base fee`
and `insufficient funds for gas * price + value`.

As a control, `typed-tip-over-cap/call/none` returns a complete `-32000` error
including `id: 1`. That fee-field relationship is rejected before deferred trace
execution. The failure depends on where validation occurs.

## Source path in the tested development revision

All source links below pin `2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e`.

1. [`BuildStreamingSingleResult` and `BuildStreamingMultiResult`][builders]
   return a successful wrapper containing a deferred trace operation. The trace
   has not run when the RPC service accepts that wrapper.
2. [`JsonRpcResponseWriter.WriteStreamableAsync`][writer] writes
   `{"jsonrpc":"2.0","result":` before awaiting the deferred operation. It writes
   the ID and closing brace only after that operation returns.
3. [`BlockValidationTransactionsExecutor`][executor] throws
   `InvalidTransactionException` when transaction processing reports failure.
   [`StreamingResultBase`][streaming] only catches cancellation here; it does not
   recover this validation exception. The RPC service's normal
   [validation-error mapper][mapper] is outside this deferred execution path.
4. [`Startup`][startup] completes the HTTP sink in `finally` as the exception
   escapes. The [sink][sink] completes the writer and HTTP response, including
   copying any buffered bytes. It has no recovery that replaces the partial
   success envelope with a JSON-RPC error.

This code path explains both the server exception and the exact missing suffix.
The H15 response remains blocked for semantic assessment: server logs establish
an internal rejection, but the caller did not receive the required valid error.
The broken JSON-RPC envelope is separately a conformance failure under H25.

## Existing fix and scope

[Nethermind PR #13666](https://github.com/NethermindEth/nethermind/pull/13666),
**fix(rpc): preserve error responses for streamed traces**, addresses this path.
It remains open and unmerged as checked on 2026-09-24, at head
`77e9a88fa2fcd11d136a8cc917c39c313f4900bc`.

The inspected patch stages the first 16 KiB on unbuffered transports and rewinds
the current response on buffered HTTP. Before transport commitment it can map
the deferred exception to a complete error response; after commitment it aborts
instead of completing a success response. The patch is absent from the tested
development revision. This investigation inspected its source; it did not run
the H15 matrix against the PR build.

Disabling `JsonRpc.EnableTracingStreamMode` takes the eager execution branch in
the tested source, bringing validation back inside the normal service error
handler. That is a source-derived workaround, not a captured alternate-config
result. The matrix retains the tested build's original behavior.

[builders]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L643-L692
[writer]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/JsonRpcResponseWriter.cs#L89-L123
[executor]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Consensus/Processing/BlockProcessor.BlockValidationTransactionsExecutor.cs#L67-L81
[streaming]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/StreamingResultBase.cs#L25-L47
[mapper]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/JsonRpcService.cs#L621-L622
[startup]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Runner/JsonRpc/Startup.cs#L489-L540
[sink]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Runner/JsonRpc/HttpJsonRpcResponseSink.cs#L134-L192
