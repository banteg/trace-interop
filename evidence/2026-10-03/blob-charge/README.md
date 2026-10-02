# H15 blob fee charge — 2026-10-03

A focused recapture of `probes-prague` that adds the `-stateDiff` blob probes. It runs with the
[2026-10-02 eval](../../2026-10-02/eval/README.md)'s [build lock](../../2026-10-02/eval/clients.lock.json)
(`trace_interop run --lock`), so all eleven builds are that matrix's images. It resends every request of
that matrix's `probes-prague` run, so [reports.lock.json](../../../reports.lock.json) selects it in place of
that run. Captured on Fedora from harness commit `26f0413b` with disposable chains: Hive for the native
builds and the Geth draft, a [replica](../../../docs/usage.md#replica-captures) for Anvil. The manifest keeps
`source_dirty: true` only because the output folder was created first.

[probes-prague](probes-prague/summary.json) is complete: **880 responses**, and every build passed the setup
controls.

## Probe

`blob-fee-none-stateDiff` calls the genesis CREATE2 factory without blob fields at 2 gwei. The `defaulted`,
`zero` and `priced` twins add one blob hash and omit `maxFeePerBlobGas`, set it to 0 or set it to the head's
blob base fee of 1 wei. Each twin uses the same gas at the same price, so the sender's extra debit in
`stateDiff` is the blob fee alone. Under H15 it is 0 for an omitted or zero cap and 131072 blob gas × 1 wei
for the positive cap. [docs/assertion-models.md](../../../docs/assertion-models.md#executable-models) describes
these twins.

## Findings

Sender debit in wei. The reference is 119520000000000 (59760 gas at 2 gwei) wherever fees are charged.

| Build | none | defaulted | zero | priced |
| --- | --- | --- | --- | --- |
| Erigon development, Nethermind development, Geth draft | 119520000000000 | +0 ✓ | +0 ✓ | +131072 ✓ |
| Besu development | 119520000000000 | 131072 | 131072 | +131072 ✓ |
| Besu release | 119520000000000 | +131072 | -32603 Internal error | +131072 ✓ |
| Anvil (both builds) | 119520000000000 | +131072 | rejected | +131072 ✓ |
| Nethermind release | 119520000000000 | malformed JSON | rejected | +131072 ✓ |
| Reth (both builds) | 0 | +0 ✓ | rejected | +0 |
| Erigon release | 0 | +0 ✓ | +0 ✓ | +0 |

- **Besu development** inverts the charge: an unpriced blob call pays its blob fee but none of its gas, even
  with `maxFeePerGas` set. [besu#11432](https://github.com/besu-eth/besu/pull/11432) removes the
  shortcut that waived the balance check for unpriced blob calls and prices the blob fee on its own.
- **Reth and Erigon's release** charge no fees in `trace_call`, so a priced blob call misses its blob fee
  too. This is the open fee-charging question in [reth#27476](https://github.com/paradigmxyz/reth/issues/27476).
  Erigon's development build charges.
- **Anvil and Besu's release** charge the head's blob fee for an omitted cap, which matches their BLOBBASEFEE 1
  in `blob-fee-defaulted`.
