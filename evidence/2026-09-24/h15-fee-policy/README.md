# H15 unsigned simulation fee-policy capture

Captured on Fedora from clean harness commit `5b152d12780eb780483e63a756c6b9a87a944685`.
The [manifest](h15-matrix/manifest.json) records all requests, immutable image IDs,
source/runner hashes and timestamps. The [summary](h15-matrix/summary.json) records
**6,804 complete responses**, no missing exchanges, and successful chain/state
controls for all nine builds. Raw [observations](h15-matrix/observations.json) and
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
