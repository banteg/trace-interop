# H17 inspector fix: Fedora regression evidence

[revm-inspectors PR #526](https://github.com/paradigmxyz/revm-inspectors/pull/526)
fixes account-birth classification in the state-diff builder used by Reth.

- Base: `940b411227de2ca7e11898016672b34733769c47`.
- Fix: `af80e453820ffeaf1fefd59c77f3f0be51895ffb`.
- Environment: Fedora Linux x86_64, Rust/Cargo 1.96.0.
- [Manifest](manifest.json): source hashes, commands, exit codes and retained-file hashes.
- [Dependency lock](Cargo.lock): exact resolved dependencies for both runs.

The same final regression tests ran with the base implementation and the fixed
implementation. Both use real EVM execution and the Parity state-diff builder.

| Run | Command | Result |
| --- | --- | --- |
| Before | `cargo test --test it state_diff_birth` | 1 passed, 2 failed; [log](red.log) |
| After | `cargo test --test it parity` | 34 passed, 0 failed; [log](green.log) |

The failures are a first transfer to an absent account (balance changed from zero
instead of added) and CREATE into an existing empty account (balance added instead
of unchanged). The fixed tests also check newly funded fee recipients, subsequent
transfers, zero-value calls, and empty/nonempty runtime creation into absent,
existing empty and prefunded accounts. Existing Parity EIP-7702 and selfdestruct
tests pass in the same run.

The change retains the database's `Some`/`None` existence result before defaulting
field values. Absent nonempty accounts receive birth markers even without CREATE;
an already existing account retains ordinary changed/unchanged fields. Empty
non-created accounts remain omitted. This does not extend historical empty-account
clearing support.

This is an inspector integration test, not a patched Reth RPC capture. Published
Reth release/development results remain independent observations in the
[fresh matrix](../h17-retest/README.md); their status must not be changed to agree
until a containing build passes the RPC probes.
