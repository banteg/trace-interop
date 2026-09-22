# Besu VM trace regression probes

Prepared 2026-09-22. The [fix summary](../../../docs/next-fixes.md) explains the two proposed patches.

## Reproduce

The patches apply to Besu upstream `caab45ca02a3edf38d85a1d11842c8cc77e0d2b1`.
Apply `regressions.patch` first, then run the three new tests:

```sh
./gradlew :ethereum:api:test --tests '*.bonsai.TraceJsonRpcHttpBySpecTest.nextWave*'
```

`frame-bookkeeping.patch` addresses the first two cases below;
`root-out-of-gas.patch` addresses the third. These are candidate diffs, not final upstream submissions.

| Test | Bytecode / setup | Failing observation |
| --- | --- | --- |
| Parent resumes after INVALID child | Creation input `0x60fe600053600160006000f050602a60005260206000f3`, gas 1,000,000 | Parent returns 42, but its RETURN at PC 22 is under the failed child instead of the root. |
| Repeated failed calls | A 64-iteration loop calls the genesis contract `0x00c0000000000000000000000000000000000000`, whose code is `0x60011f`. Gas 1,000,000. Complete loop bytecode is in the probe. | On call 17, `ex.used` is 918,572. The immediately following POP establishes that CALL resumed with 916,823. |
| Root out of gas | Creation input `0x6001600201`, gas 53,086 under the suite's Istanbul configuration | Intrinsic gas is 53,080. Two PUSHes consume the remaining six; ADD still reports `push: ["0x3"]` and `used: -3`. |

The probes use `trace_call` through the actual HTTP service and EVM, with sender
`0x627306090abab3a6e1400e9345bc60c78a8bef57`, selectors `["vmTrace", "trace"]`, and `latest`.
The two short failing responses are preserved alongside the patches.

## Validation

The executed build uses upstream `caab45ca` plus the already-submitted
[CALL-memory correction #11350](https://github.com/besu-eth/besu/pull/11350), at commit
`4839f5a480c43e23513f7e9111378b49e7d36662`. All three probes fail before these candidate
changes. Both production diffs and the regression diff also apply together to clean
upstream `caab45ca`; independent upstream validation is recorded below.

The regression patch here contains only the three new probes, excluding #11350's tests.
Tests ran with Java 25. No fresh cross-client matrix has been run for these candidates.

With both final candidate patches, **816 trace HTTP tests and 400 debug-trace HTTP tests
pass**, including the three regressions. One upstream Forest trace suite remains skipped.
No existing response fixtures were changed by these candidate patches.

## Upstream submissions

Both PRs were validated independently on upstream `caab45ca`, without #11350:

| PR | Regressions before the fix | After the fix |
| --- | --- | --- |
| [#11352](https://github.com/besu-eth/besu/pull/11352) | INVALID and stack-underflow child halts, and repeated failed calls: all three fail. | 812 trace HTTP tests and 400 debug-trace HTTP tests pass. |
| [#11353](https://github.com/besu-eth/besu/pull/11353) | Out-of-gas ADD fails; the sufficient-gas control passes. | 811 trace HTTP tests and 400 debug-trace HTTP tests pass. |

Both pass module Spotless checks. The upstream Forest trace suite remains skipped.
The PRs contain the final tests and changelog entries; the probe diffs above preserve
the initial reproduction. No fresh cross-client matrix has been run.

The #11352 child-halt regressions also verify bytecode retention: the same `0xfe`
or `0x50` program reports its code at the root but loses it as a child before the
follow-up. Both cases fail at the bytecode comparison on `b58a5299`; after the
follow-up, all 812 trace and 400 debug-trace HTTP tests pass. See
[`bytecode-validation.json`](bytecode-validation.json) for the recorded failures and suite results.
