# Explicit zero and null gas — 2026-10-01

A focused recapture of the `probes-prague` corpus with the H15 explicit-zero gas cases added:
`field-gas-zero` (trace_call), `field-gas-zero-many` (one-item trace_callMany), their eth_call
control `field-gas-zero-eth-call`, and the H14 twin `field-gas-null`. It reuses the
[2026-09-30 eval](../../2026-09-30/eval/README.md)'s [build lock](clients.lock.json) byte for byte
(`--reproduce-lock`, hence the `historical-reproduction` [preflight](preflight.json)), so all
eleven builds are the eval's images. The run resends every request of the eval's `probes-prague`
run, and every one of those responses is unchanged, so [reports.lock.json](../../../reports.lock.json)
selects it in place of `eval/probes-prague`. Captured on Fedora from harness commit `4b10bbf7`
with disposable chains: Hive for the native builds and the Geth draft, a
[replica](../../../docs/usage.md#replica-captures) for Anvil. The manifest keeps
`source_dirty: true` only because the matrix runner created this untracked output folder and its
log first.

[probes-prague](probes-prague/summary.json) is complete: **836 responses**, and every build passed
the setup controls.

## Cases

Each case sends the `field-gas-omitted` GAS program (a creation from fixture key 1 with no fee
fields) with an explicit gas member. Under the 2026-10-01 rule an explicit `"gas": "0x0"` is a
supplied zero limit: it fails the intrinsic-gas check (53,122 gas for this initcode) and must be
rejected, with -38013 recommended; only omitted or null gas takes the eth_call default under the
RPC cap. The eth_call control is observed, never scored. `field-gas-null` must return the GAS word
of its omitted twin from the same build.

## Findings

✅ marks a response that matches the recommendation.

| Build | eth_call, gas 0 (control) | trace_call, gas 0 | trace_callMany, gas 0 | trace_call, gas null |
| --- | --- | --- | --- | --- |
| Geth draft | rejected -32000 | ✅ rejected -38013 | ✅ rejected -38013 | ✅ as omitted |
| Nethermind 2.2.0-preview | rejected -32000 | ✅ rejected -32000 | ✅ rejected -32000 | ✅ as omitted |
| Nethermind 2.0.0 | rejected -32000 | malformed response (H25) | malformed response (H25) | ✅ as omitted |
| Besu develop, 26.9.0 | rejected -32003 | internal error -32603 | -32603 wrapped as a result (H25) | ✅ as omitted |
| Reth nightly, 2.7.0 | rejected -32000 | ✅ rejected -32000 | ✅ rejected -32000 | ✅ as omitted |
| Anvil nightly, 1.8.3 | rejected -32000 | ✅ rejected -32000 | ✅ rejected -32000 | ✅ as omitted |
| Erigon 3.8.0-dev | **result**: the default budget's GAS word | ✅ rejected -38013 | ✅ rejected -38013 | ✅ as omitted |
| Erigon 3.7.0 | **result**: the default budget's GAS word | ✅ rejected -32000 | ✅ rejected -32000 | ✅ as omitted (runs empty `input`, as its omitted twin does) |

Every trace method rejects the zero limit for its intrinsic gas; none returns a result with the
default budget or an out-of-gas frame. Erigon's development build returns -38013 for trace_call
(`intrinsic gas too low: have 0, want 53122`), as reading its main branch predicted, while its
eth_call alone runs the call with the default budget (GAS 0x2fa20fc, the omitted-gas word). Besu's
eth_call rejects the zero limit (-32003), but its trace methods fail with an internal error, which
the draft does not accept as the required rejection; trace_callMany also wraps that error as a
result. Nethermind 2.0.0's malformed responses are the known streamed-error defect, fixed in the
development build. See [the H15 report](../../../reports/decisions/H15.md).
