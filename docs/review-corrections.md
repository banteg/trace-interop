# Measurement and draft review corrections

The September 23 review corrections preserve all earlier wire observations. Reports
now reassess 4,071 observations against the pinned draft and record incomplete
assertion coverage explicitly. See the [technical appendix](../reports/technical.md)
and [assessment provenance](../reports/assessment.json).

- Pruning eligibility uses the retained header/receipt, latest execution and independent
  historical nonce query. Trace responses cannot exclude themselves from H06. Original
  `capture_eligible` values are retained alongside recomputed eligibility.
- Request shapes are checked against the pinned schema, including integer paths,
  address-list types, negative counts, null selections and mode arguments. Unknown
  selected blocks are assessed separately. Nested JSON-RPC error envelopes are failures,
  and zero-fee callMany is covered alongside single calls.
- Response-shape guards prevent malformed trace/result/error/VM fields from crashing
  assessment. Known fixture REVERT paths are identified without error-message matching;
  frame assertions apply only when `trace` was selected. The current draft already
  required explicit failed-frame results; refreshing the stale spec pin resolves the
  earlier schema/rule mismatch.
- Address matching compares bytes, missing transactions have one H06 check, the dead
  nonce-case name is removed, and missing reference trees produce an explicit unassessed
  result. The report inventory and ledger verifier now share `reports.lock.json`.
- Unchecked declared cases produce “Partially assessed” rather than agreement. Entirely
  unassessed eligible trace observations remain listed in machine-readable coverage;
  these fixes do not claim to implement every recommendation in the ledger.

The draft now accepts null address lists as unrestricted, allows standard call fields
and ignores unknown call-object fields. Unknown blocks propose `-32001`, distinct from
missing transactions (`null`) and unavailable pruned state (`4444`). Integer trace_get
paths remain invalid (`-32602`); the conversion from output traceAddress integers is
explicit. These are draft compatibility choices, not adopted client requirements.

H29 already described inherited value as a compatibility choice. Its explanation now
separates CALL/CALLCODE operands from DELEGATECALL inheritance, and the new fixtures
actually distinguish outer and child values. A simulated transfer funds the future
creation address before a zero-value creation calls the precompile with one wei. The
constructor returns the opcode success bit; independent state controls establish the
nonce and empty target. See [scenario details](scenarios.md#crossed-precompile-values).

## Validation

- 63 Python tests pass, including assertions over the published counterexamples and
  current report-source hashes. Request/result schemas and recursive negative vectors pass.
- Execution-apis uncached Go tests, go vet, generated schema build and speccheck
  fixture checks pass. All five renderer tests and the documentation production build
  pass; nullable filter fields are explicitly checked for visibility.
- [Native crossed-value capture](../evidence/2026-09-23/precompile-values-native/summary.json):
  112 responses across eight pinned builds, all setup checks passed.
- [Geth draft capture](../evidence/2026-09-23/precompile-values-geth/summary.json):
  14 responses, setup passed. This fork is evaluated separately from upstream Geth.
- [Fresh pruning capture](../evidence/2026-09-23/pruned-review/summary.json):
  24 responses across both pinned Reth builds, independent setup passed. Their trace
  error codes still differ from the proposed 4444.

The crossed-value captures support explicit child-value selection in Erigon, Nethermind
and Reth. Besu still omits nonzero-value precompile children and propagates precompile
failure to the successful parent; these are separate H29 and H24 findings. All nine
builds return the expected success/failure bit. Passing capture setup is not client
conformance: Hive placeholder mismatches intentionally retain actual responses.

Earlier corpora were reassessed without rerunning unchanged client binaries. Fresh runs
cover the new discriminator fixtures and the corrected pruning setup. Reports are
regenerated deterministically and retain source, schema and evidence hashes.

## H13 policy correction

The temporary nonce-permissive recommendation is superseded by selected-state execution
validation. This restores the original direction while distinguishing execution validity
from local transaction-pool admission policy. It is a compatibility change, not evidence
that legacy diagnostic workflows are illegitimate. Rejection and the proposed `-32003`
code are assessed separately; malformed JSON does not prove permissive execution.

The [H13 validation study](h13-validation.md) records the Erigon/gist timing and a fresh
560-response capture with nonce, funds, chain-ID, intrinsic-gas, base-fee and sender-code
discriminators. Successful output, storage changes and CREATE addresses distinguish
execution from empty result envelopes. Valid EIP-7702 delegation and execution-OOG
controls protect the boundary between validation failure and an EVM halt.
