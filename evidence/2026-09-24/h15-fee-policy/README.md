# H15 unsigned simulation fee-policy capture

Captured on Fedora from clean harness commit `5b152d12780eb780483e63a756c6b9a87a944685`.
The [manifest](h15-matrix/manifest.json) records all requests, immutable image IDs,
source/runner hashes and timestamps. The [summary](h15-matrix/summary.json) records
**6,804 complete responses**, no missing exchanges, and successful chain/state
controls for all nine builds. Raw [observations](h15-matrix/observations.json.gz) and
Hive logs are authenticated by [checksums](h15-matrix/checksums.json).

Each build received 744 trace requests (664 proposed-policy requests and 80
unresolved-default observations), plus twelve independent controls. The
[probe guide](../../../docs/h15-fee-policy.md) maps requirements to fixtures and
documents the independent gas/balance models. Tests use disposable Hive chains;
the production node is not used.

## Tested builds

These are the same pinned native images as the previous coverage matrix, not
new builds of the September 24 source-review revisions in H15.

| Build | Runtime version |
|---|---|
| Besu release | `26.8.1` |
| Besu development | `26.9-develop-d997aad` |
| Erigon release | `3.6.1-0c4d9c91` |
| Erigon development | `3.8.0-dev-c25b8e47` |
| Nethermind release | `1.39.3+28cbe2a0` |
| Nethermind development | `2.1.0-unstable+a404c4f0` |
| Reth release | `2.6.0+73a3a008` |
| Reth development | `2.5.2+03cb186c` |
| Geth draft fork | `1.17.6-unstable-c36ee43e-2026-09-23` |

The Geth Docker image was rebuilt after cache cleanup. Its binary SHA-256 is
identical to the prior lock (`09221759120b5309160772458954b24bbc43849424cb0e1cbc4e6ed33d1ea871`),
with the same source snapshot, toolchain and base-image digest. The new Docker
image ID is retained in [clients.lock.json](clients.lock.json); it is not silently
substituted for the old image ID in historical captures.

## Findings

- **Geth draft:** matches all 664 proposed-policy requests, including exact
  upfront/final accounting, the capped storage refund, failed-execution charges,
  funding boundaries and selection-independent mixed batches.
- **Nethermind, both builds:** the successful observable executions match the
  environment/accounting model. Empty trace selections return an internal error;
  stateDiff-only responses return `output: null`. Many invalid fee/funding
  requests produce malformed JSON, so those responses cannot establish a valid
  validation rejection. Tip-above-cap requests do produce a proper error.
- **Besu, both builds:** the priced environment, upfront payment and settlement
  probes match, including refund/REVERT/OOG. Explicit zero fees fail. Invalid
  fee/funding requests return generic internal errors, sometimes wrapped as a
  successful result; these do not prove the intended validation behavior.
- **Erigon, both builds:** legacy zero is rejected; typed zero is repriced to B.
  Positive underpriced fees are rejected. Successful priced simulations omit the
  upfront sender debit and retain the beneficiary credit; underfunded requests
  can execute. Environment differences remain, including `trace_call` GASLIMIT.
  The release build also reports `method handler crashed` for some empty-selection
  calls where development returns a result.
- **Reth, both builds:** explicit zero rewrites BASEFEE to zero. Positive legacy
  prices below B execute while positive typed caps below B are rejected. Priced
  calls omit gas-fee charging, and the funding/batch witnesses expose the effects.

These are bounded observations, not client rankings or client-team agreement.
Release and development are regression comparisons, not independent votes.
See [the generated H15 report](../../../reports/decisions/H15.md) for individual
requests and checks, including the unresolved-default observations.

## Assessment corrections after capture

Original responses are unchanged. The current oracle additionally requires a
recognizable fee/funding validation diagnostic for an invalid request to match.
It checks the independently violated constraint and, when the error names a
batch position, that position too. A generic/internal/crash error stays blocked;
rejecting an insufficient-value zero-fee call merely because its price is below
B is a mismatch. This avoids crediting Erigon's `-32000` handler crash or a
zero-fee rejection as successful funding validation. Unknown diagnostic wording
is conservatively blocked; the model does not prescribe exact error text.

Regression tests cover these distinctions. Assessment code hashes are recorded
in `reports/assessment.json`, separately from immutable capture provenance.

## Erigon empty-selection crash investigation

All **26** `method handler crashed` responses in Erigon release are `trace_call`
requests with `traceTypes: []`. The development build has zero such responses.
For example, [legacy-at-base/call/none](../../../reports/cases/fee-policy/legacy-at-base/call/none.md)
supplies a valid price exactly equal to B and reaches the same panic.

In release commit `0c4d9c91`, [Call initializes `ot.r` only when a trace type is
selected](https://github.com/erigontech/erigon/blob/0c4d9c91dbaffd52890235f7ea395b0231738501/rpc/jsonrpc/trace_adhoc.go#L1172-L1175),
but [attaches its hooks unconditionally](https://github.com/erigontech/erigon/blob/0c4d9c91dbaffd52890235f7ea395b0231738501/rpc/jsonrpc/trace_adhoc.go#L1209).
The first `OnEnter` reaches `captureStartOrEnter`, which [dereferences
`ot.r.VmTrace`](https://github.com/erigontech/erigon/blob/0c4d9c91dbaffd52890235f7ea395b0231738501/rpc/jsonrpc/trace_adhoc.go#L375-L376).
The retained [client log](h15-matrix/hive/erigon_release/client-188c6445660347e875ba09ce9d830ef1b394c6f5e5c00fc8f5ec7b0510b89e93.log)
records that exact nil-pointer stack at lines 313–315. The RPC callback's
[recovery handler](https://github.com/erigontech/erigon/blob/0c4d9c91dbaffd52890235f7ea395b0231738501/rpc/service.go#L228-L233)
turns it into the error response; the client process continues serving requests.
Fee validation can reject a request before it reaches this hook, explaining why
some other empty-selection requests return validation errors instead.

Upstream [PR #23572](https://github.com/erigontech/erigon/pull/23572), merged on
2026-08-27 as `d0514ffdaea1abb3214f5d2d3ec2af5765b247ee`, already fixes this by
attaching the tracer only for `trace` or `vmTrace`. It includes regression tests
for empty-selection `trace_call` and `trace_rawTransaction`. The tested development
commit `c25b8e47` contains the fix; tested release `0c4d9c91` does not.
The release's `callMany` path already guards hook installation separately and
does not share this nil-result initialization defect. No new client patch is needed.
