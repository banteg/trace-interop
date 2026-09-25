I confirmed it. A top-level transaction to a precompile that fails, traced with Parity `vmTrace`, throws a `NullReferenceException` in the buffered `ParityLikeTxTracer`. Confidence is high. `trace_simulateV1` hits it with default config. The design checkout doesn't fix it; it just moves the crash to a different callback. I didn't run anything; all of this is from reading the code.

## The failing path on master (0ba8d5faee)

1. **Tracer setup:** `vmTrace` sets `IsTracingInstructions = true` (`ParityLikeTxTracer.cs:61-66`). That makes `TransactionProcessor.cs:427-429` and `:1447-1449` run the VM with instruction tracing on (`ExecuteTransaction<OnFlag>`).
2. **Top-level precompile frame:** `VirtualMachine.cs:253-259` calls `ExecutePrecompile`. That reports the action (`:958`) but never calls `StartOperation`, because a precompile has no opcodes.
   - The tracer's `ReportAction` → `PushAction` → `OnEnterVmFrame` (`ParityLikeTxTracer.cs:190-204`) opens an empty frame and leaves `_currentOperation` null. It was never set, or it was cleared at `:154`.
3. **Any precompile failure goes to `HandleFailure`:** both the out-of-gas check (`:1220-1222`) and a failed `Run` (`:1249`, `PrecompileFailure`) come back as exceptions. They become `PrecompileOutOfGasException` (`:979-982`), then `goto Failure` (`:259`) → `HandleFailure` (`:406`).
4. **The crash:** `VirtualMachine.cs:692-695` calls `ReportOperationRemainingGas(0)` whenever instruction tracing is on. `_gasAlreadySetForCurrentOp` is false, so `ParityLikeTxTracer.cs:313` runs `_currentOperation!.Cost -= …` on a null and throws.
   - `HandleFailure` sits after the `try`/`catch` (`:393-406`), and `TransactionProcessor` has no catch, so the exception leaves the VM.

## What reaches it

| Path | Tracer | Result |
|---|---|---|
| `trace_simulateV1` with `vmTrace` | `ParityStyleSimulateBlockTracerFactory.cs:15`, which is the buffered tracer | **Crashes with default config.** `SimulateBridgeHelper.cs:118-121` catches it and returns the NRE message as `Error`. |
| `trace_call`, `trace_rawTransaction`, `trace_callMany`, `trace_replayTransaction` in buffered mode | `runBuffered` → `new ParityLikeBlockTracer(...)` (`TraceRpcModule.cs:142,190,237`) | Crashes when `EnableTracingStreamMode=false` (default is true, `JsonRpcConfig.cs:53`), or when `MaterializeForInProcess` is used |
| `trace_replayBlockTransactions` through the parallel tracer | `PerTransaction` builds a buffered tracer (`TraceRpcModule.cs:546-549`) even in streaming mode | Probably crashes on a block with such a tx. I didn't verify when the parallel tracer covers a block. |
| Default streaming replay (`trace_call` and similar) | `StreamingParityLikeTxTracer`, with `_streamVmTrace` true | Safe: `if (_gasAlreadySetForCurrentOp \|\| !_hasPendingOp) return;` (`StreamingParityLikeTxTracer.cs:310`) |
| **Child** CALL to a failing precompile | buffered tracer | Safe. When the CALL suspends, `EndInstructionTrace` (`VirtualMachine.cs:1451`) already set `_gasAlreadySetForCurrentOp`, so the later call from `HandleFailure` does nothing. `ReportOperationError` then removes from the child's empty op list, which also does nothing. |
| Gas estimation | the estimate tracer never turns on instruction tracing | Not affected: with instruction tracing off, `HandleFailure` skips this branch at compile time |

Every other instruction tracer already ignores this call when no opcode is open: `GethLikeTxTracer.cs:139`, `GethLikeTxDirectStreamingTracer.cs:149`, `StateTestTxTracer.cs:101`, `ZkGasTxTracer.cs:78`, and the Parity streaming tracer. The buffered Parity tracer is the only one that doesn't.

## Recommended fix

Fix it in the tracer, matching `GethLikeTxTracer.cs:139`. It's a one-line change at `ParityLikeTxTracer.cs:309`:

```csharp
if (!_gasAlreadySetForCurrentOp && _currentOperation is not null)
```

Also drop the `!` on line 313. `ReportOperationError` is already fine with a null (`Ops.Remove(null)` does nothing). The trace then matches a successful top-level precompile: one root action with its error set, and `vmTrace` with empty `ops`.

I wouldn't gate `HandleFailure` in the VM on `!IsPrecompile`. That would change the child-precompile callbacks that the Geth, JS and ZkGas tracers see today, which is a behaviour change beyond this bug.

## Regression test

Add it to `ParityLikeTxTracerTests.cs`, next to `Can_trace_precompile_calls` (`:764`). It reuses two existing patterns: the tx sent straight to a precompile from `GethLikeTxFileTracerTests.cs:62-70`, and the empty-input Blake2F failure from `Eip8037RegressionTests.cs:196-205`.

```csharp
[Test]
public void Can_trace_failed_top_level_precompile_call()
{
    Transaction tx = Build.A.Transaction
        .WithTo(Blake2FPrecompile.Address)
        .WithGasLimit(100_000)
        .SignedAndResolved(TestItem.PrivateKeyA)
        .TestObject;
    (Block block, _) = PrepareTx(Activation, 100_000, transaction: tx);
    ParityLikeTxTracer tracer = new(block, tx, ParityTraceTypes.Trace | ParityTraceTypes.VmTrace);

    _processor.Execute(tx, new BlockExecutionContext(block.Header, Spec), tracer);

    ParityLikeTxTrace trace = tracer.BuildResult();
    using (Assert.EnterMultipleScope())
    {
        Assert.That(trace.Action!.Error, Is.EqualTo("Out of gas"));
        Assert.That(trace.VmTrace!.Operations, Is.Empty);
    }
}
```

On master this should throw the NRE, and it should pass with the fix. The error string is "Out of gas" because every failed precompile is reported as `PrecompileOutOfGasException`; `Eip8037RegressionTests.cs:218-220` asserts the same thing.

## Does the design checkout change the finding?

No, it only moves where the crash happens:
- `HandleFailure` now calls `EndInstructionTrace(0, errorType)` (design `VirtualMachine.cs:692-695`).
- With no opcode open, which is always the case for a top-level precompile (`_isInstructionTraceActive` is reset at `:224`), that goes to the branch at `:1555-1561`. It calls `ReportGasUpdateForVmTrace(0, 0)` and then `ReportOperationError`.
- The design's `ParityLikeTxTracer.ReportGasUpdateForVmTrace` does `_currentOperation!.Used = gasAvailable` (design `:500`), so it throws the same NRE. Its streaming version is guarded (`if (!_hasPendingOp) return;`, `:391`), so again only the buffered tracer breaks.

If that design lands, the buffered tracer needs a `_currentOperation is null` early return in `ReportGasUpdateForVmTrace` as well as `ReportOperationRemainingGas`. The same test covers both.

One more thing about the design, low severity: for a child precompile failure, that same branch sets the parent CALL op's `Used` to 0. The continuation at design `:1384` overwrites it with the right value, so the final trace looks fine. It's still worth knowing if the branch is kept.
