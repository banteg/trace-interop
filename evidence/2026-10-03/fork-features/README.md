# Fork activation of call-object features — 2026-10-03

A focused recapture of `probes-forks` that adds `fork-*` unsigned calls, each with an `eth_call` twin. It runs
with the [2026-10-02 eval](../../2026-10-02/eval/README.md)'s [build lock](../../2026-10-02/eval/clients.lock.json),
so the builds are that matrix's images, and it resends every request of that matrix's `probes-forks` run, so
[reports.lock.json](../../../reports.lock.json) selects it in place of that run. Anvil does not run this corpus.
Captured on Fedora from harness commit `1387ccc2`; the manifest keeps `source_dirty: true` only because the output
folder was created first.

[probes-forks](probes-forks/summary.json) is complete: **567 responses**.

## Probe

The forks chain activates Berlin at block 32, London at 36, Cancun at 56 and Prague at 60. Each feature's fields
(an access list, zero dynamic fees, one blob hash, one signed authorization) go one block before and at its
activation, and an explicit type with no feature fields goes one block before its fork. A `trace_call` at block N
runs under N's rules ([H12](../../../reports/decisions/H12.md)). Every call but the priced pair is unpriced and
reaches a code-free address, so a call that runs returns `0x`.

## Findings

`trace_call` outcomes; a code is a rejection. The `eth_call` twins agree except where a build's `trace_call` has
its own parameter handling (Erigon 3.7.1) or crashes (Besu 26.9.0).

| Case | Block | Besu dev | Besu 26.9 | Erigon dev | Erigon 3.7.1 | Nethermind dev | Nethermind 2.1 | Reth dev | Reth 2.7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `access-list-before` | 31 | `-32602` | `-32603` | `-32000` | `-32000` | `-32603` | malformed JSON | `-32003` | `-32003` |
| `access-list-at` | 32 | runs | runs | runs | runs | runs | runs | runs | runs |
| `type1-before` | 31 | runs | runs | runs | runs | `-32603` | malformed JSON | runs | runs |
| `dynamic-fees-before` | 35 | runs | runs | runs | runs | runs | runs | `-32003` | `-32003` |
| `dynamic-fees-at` | 36 | runs | `-32603` | runs | runs | runs | runs | runs | runs |
| `type2-before` | 35 | runs | runs | runs | runs | runs | runs | runs | runs |
| `blob-before` | 55 | `-32602` | `-32603` | `-32000` | runs | runs | malformed JSON | `-32003` | `-32003` |
| `blob-at` | 56 | runs | `-32603` | runs | runs | runs | malformed JSON | runs | runs |
| `type3-before` | 55 | runs | runs | runs | runs | `-32000` | `-32000` | runs | runs |
| `authorization-before` | 59 | `-32602` | `-32603` | `-32000` | runs | `-32603` | malformed JSON | `-32003` | `-32003` |
| `authorization-at` | 60 | runs | `-32603` | runs | runs | runs | runs | runs | runs |
| `type4-before` | 59 | runs | runs | runs | runs | `-32603` | malformed JSON | runs | runs |
| `dynamic-fees-priced-before` | 35 | runs at 0 gwei | runs at 0 gwei | runs at 0 gwei | runs at 1 gwei | runs at 1 gwei | runs at 1 gwei | `-32003` | `-32003` |
| `dynamic-fees-priced-at` | 36 | runs at 2 gwei | runs at 2 gwei | runs at 2 gwei | runs at 2 gwei | runs at 2 gwei | runs at 2 gwei | runs at 2 gwei | runs at 2 gwei |

- An access list, blob fields or an authorization list before its fork is rejected by Besu, Erigon, Reth and
  upstream Geth's `eth_call`. Nethermind fails the access list and the authorization list with -32603, and its
  development build runs blob fields before Cancun.
- An explicit type 1 to 4 with no feature fields runs before its fork everywhere but Nethermind, which fails
  types 1 and 4 with -32603 and requires a blob for type 3. The type is not a feature.
- Zero dynamic fees before London run everywhere but Reth. Priced ones (`dynamic-fees-priced-*`, a creation that
  returns GASPRICE with a 2 gwei cap and 1 gwei tip) split three ways before London: Besu, Erigon's development
  build and upstream Geth's `eth_call` run at GASPRICE 0, ignoring the fields; Nethermind runs at the 1 gwei tip;
  Reth rejects with -32003. At London every build runs at 2 gwei. This case is recorded, not judged.

[H14](../../../reports/decisions/H14.md) states the resulting rule: an access list, blob fields or an authorization
list before its fork is rejected (-32003 recommended), and `type` adds no requirement of its own. Dynamic fees
before London are still open.
