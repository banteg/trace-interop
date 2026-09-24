# Unsigned simulation fee probes

The `fee-policy` corpus tests the proposed [H15 policy](../reports/decisions/H15.md)
against the frozen `raw-validation` Prague chain. Its selected block has base fee
765,625,000 wei, number 2, timestamp 20 and gas limit 100,000,000. Both blocks
are empty. Independent RPC controls verify sender/beneficiary/empty-account
balances, nonces and code; the harness also verifies both selected and latest
block hashes and roots before interpreting results.

## Coverage

Every family runs all eight subsets of `trace`, `stateDiff` and `vmTrace`, including
the empty selection. Single-call families run through both `trace_call` and
one-element `trace_callMany`. Batch families add sequential execution.

| Requirement | Probes |
|---|---|
| Explicit zero-fee exemption | Legacy zero and EIP-1559 cap/tip both zero; an unfunded sender with zero value |
| Reject positive fees below base fee B | Legacy prices and typed caps at 1 and B−1 |
| Accept valid fee boundaries | Legacy B/B+1; typed B with zero tip, positive cap with zero tip, tip-limited and cap-limited effective prices |
| Validate typed fee relationships | Tip above cap, including zero cap with positive tip |
| Enforce value and upfront funding | Exactly funded and one-wei-short legacy/typed/free calls; typed funds sufficient at effective price but insufficient at fee cap; unfunded priced sender |
| Preserve environment | Exact GASPRICE, BASEFEE, NUMBER, TIMESTAMP and GASLIMIT in returned bytes |
| Apply upfront gas payment during execution | CALLER BALANCE in returned bytes, after gas purchase and value transfer |
| Settle fees and value | Exact sender debit, nonce, value credit, beneficiary tip and aggregate base-fee burn |
| Refund unused gas and refund-counter credit | Gas limit exceeds used gas; creation sets then resets a storage slot, with EIP-3529 refund cap |
| Charge failed execution | REVERT returns value but consumes gas; an unaffordable memory expansion exhausts the gas limit |
| Carry effects into later calls | Free/priced/free and priced/free/priced, both fee families; refund/REVERT/OOG followed by a balance/environment observer; second-call affordability after first-call fees |
| Separate unresolved defaults | Omitted fields and cap-only/tip-only zero/positive fields are captured without a policy pass/fail |

## Independent expectations

`scripts/build_fee_policy_fixtures.py` generates requests. `trace_interop/fee_policy.py`
computes expected values from the frozen header, controlled prestate, request and
small known programs. No client output or trace gas becomes an expected answer.

The environment creation program returns seven 32-byte words. The final two read
the sender's balance after upfront payment and the beneficiary's balance before
the current tip. Returning those values makes accounting observable even when no
state diff is requested, including settlement of preceding calls. Creation returns
224 bytes of runtime code and charges their exact code-deposit cost.

The independent charged-gas totals are 98,623 for the environment program,
60,320 for storage reset (75,400 before its capped 15,080 refund), 53,156 for
REVERT, 200,000 for out-of-gas and 21,000 for an empty-code transfer. All include
transaction intrinsic gas where applicable. Tests mutate environment words,
sender/beneficiary/value accounting, nonce and batch length to ensure the oracle
detects errors that schema checks alone would miss.

The scope is unsigned execution fees on a positive-base-fee Prague block. Blob
fees, block/state overrides and omitted/incomplete-field normalization remain
outside this policy assertion. Signed validation stays in H13's separate corpus.
These are proposed policy checks, not a claim of client-team agreement.

The [Fedora capture](../evidence/2026-09-24/current-matrix/README.md) retains all
6,804 responses across nine pinned builds. Generic/internal/crash errors never
prove validation; recognized errors must match the independent constraint and
any reported batch position. Unrecognized diagnostic wording remains blocked.

## Run current builds or reproduce history

```sh
uv run python scripts/build_fee_policy_fixtures.py
uv run python -m unittest discover -s tests -p test_fee_policy.py -v
uv run python scripts/run_matrix.py --corpora fee-policy --output runs/fee-policy-current
uv run trace-interop report --run runs/fee-policy-current/fee-policy --output runs/fee-policy-report
```

The matrix runner resolves latest published stable/development images and the current
Geth draft branch, then requires a live freshness preflight. Omit `--corpora` for the
full comparison. Use `--reproduce-lock` only to intentionally rerun a recorded snapshot;
see [usage](usage.md). Captures retain the actual image IDs and runtime versions.

## Reading the assessment status

Unresolved omitted/incomplete fee defaults are **Policy open** observations, not
missing tests. Geth's tested build passes all 664 defined-policy requests; its
80 default probes keep H15 policy-open. Nethermind's tested development build
has a separate coverage gap: 232 truncated JSON responses (216 defined-policy
requests and 16 unresolved-default probes), which prevent semantic assessment.
Its other 448 defined-policy requests match. A malformed response cannot establish
that the intended fee/funding validation occurred. Per-build report summaries
name blocked cases and distinguish them from unresolved policy.

The [Nethermind investigation](nethermind-streamed-errors.md) traces those malformed
responses to validation exceptions during deferred streaming and links the
existing, still-unmerged fix. Its server logs establish internal rejection, while
the malformed RPC responses remain blocked for H15 assessment.
