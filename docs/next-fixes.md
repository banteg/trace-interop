# Next client fixes

Two Besu patches are worth pursuing next. Three real-EVM HTTP regressions reproduce
incorrect `vmTrace` output; none requires choosing between competing API contracts.

| Proposed patch | What goes wrong | Least surprising behavior |
| --- | --- | --- |
| Keep frame bookkeeping aligned when an opcode is omitted | A child that immediately executes `INVALID` absorbs its parent's subsequent instructions. Separately, after enough failed calls in a loop, CALL gas is taken from an earlier iteration. | Parent instructions stay in the parent trace, and each CALL uses its own resumption frame. |
| Suppress execution effects for root out-of-gas steps | With six execution gas, `PUSH1 1; PUSH1 2; ADD` reports a successful ADD push and **−3 remaining gas**, despite an out-of-gas error. | Use `ex: null`, as Besu already does for nested out-of-gas steps. |

## Why these are bugs

**Frame ownership and gas:** the parent successfully returns 42 after a failed CREATE,
but its RETURN is missing from the root VM trace and appears under the failed child.
A separate 64-call loop first misreports resumption gas on call 17: **918,572 instead
of 916,823**. Both arise because bookkeeping advances only for operations emitted in
`vmTrace`, even though call-resumption lookup walks the complete raw frame list.
Synthetic frames still need their existing depth treatment; they do not necessarily
have a corresponding child VM trace.

The patch preserves Besu's existing choice to omit certain halted opcodes. Whether to
include those opcodes is a separate question. It also leaves precompile inclusion and
CALL gas-cost conventions alone.

**Root out of gas:** the execution already reports failure. A negative remaining-gas
value and a successful stack result cannot describe that failed step. Removing the
root-only exception makes the existing nested-frame behavior consistent at depth zero;
no new error wording or result format is needed.

Both fixes are in
[`VmTraceGenerator`](https://github.com/besu-eth/besu/blob/caab45ca02a3edf38d85a1d11842c8cc77e0d2b1/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/vm/VmTraceGenerator.java#L87).

## Preparation

[Regression probes and candidate patches](../evidence/2026-09-22/besu-next-fixes/README.md)
include minimal bytecode, failing responses and the proposed implementation changes.
All three new probes fail before the fixes; afterward, 816 trace HTTP tests and 400
debug-trace HTTP tests pass. One upstream suite remains skipped. No existing response
fixtures needed changes. These are preparation artifacts, not submitted PRs. Split the three probes between the
two patches and apply the project's formatting and changelog requirements before submission.
The patches can target upstream independently of the existing CALL-memory fix.

## Existing work to validate

Avoid duplicating these upstream patches:

| Client | Existing patch | Useful follow-through |
| --- | --- | --- |
| Besu | [#10953: block pre-execution before tracing](https://github.com/besu-eth/besu/pull/10953) | Run our fork-context and system-contract cases against the patch. |
| Nethermind | [#13551: pair instruction completions with starts](https://github.com/NethermindEth/nethermind/pull/13551) | Retest VM traces around CALL/CREATE failure and resumption. |
| Nethermind | [#13622: terminal output for top-level action traces](https://github.com/NethermindEth/nethermind/pull/13622) | Retest direct and nested precompile output, returns and reverts. |
| Reth / revm-inspectors | [#511: executed bytecode](https://github.com/paradigmxyz/revm-inspectors/pull/511) | Retest constructor and delegated-code cases after dependency uptake. |

These checks could supply useful review evidence without another competing implementation.
