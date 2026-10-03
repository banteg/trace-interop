# Blob fee cap on an unpriced call — 2026-10-04

A focused recapture of `probes-prague` that adds a blob call with a positive `maxFeePerBlobGas` and no execution fee
fields. It runs with the [2026-10-02 eval](../../2026-10-02/eval/README.md)'s [build lock](../../2026-10-02/eval/clients.lock.json),
so all eleven builds are that matrix's images. It resends every request of the [fee-combos](../../2026-10-03/fee-combos/README.md)
recapture, and [reports.lock.json](../../../reports.lock.json) selects it in place of that run. It was captured on Fedora
from harness commit `261534f0` with disposable chains: Hive for the native builds and the Geth draft, and a
[replica](../../../docs/usage.md#replica-captures) for Anvil.

[probes-prague](probes-prague/summary.json) is complete: **1364 responses**, and every build passed the setup controls.

## Probe

H15 prices the blob fee on its own, and only the execution fees decide whether execution is priced. A call that names
blob hashes and a covering `maxFeePerBlobGas`, but no `gasPrice`, `maxFeePerGas` or `maxPriorityFeePerGas`, therefore
pays no gas, keeps the block's BLOBBASEFEE and pays the blob fee. The call goes through the genesis CREATE2 factory,
whose child deploys the BLOBBASEFEE it read. The head's blob base fee is the minimum, 1, so the blob fee is one blob's
131072 blob gas.

- `blob-fee-cap-unpriced` checks the deployed word. `blob-fee-cap-unpriced-eth-call` is its eth_call twin, recorded only.
- `blob-fee-cap-unpriced-stateDiff` checks that the sender pays 131072 wei more than `blob-fee-none-unpriced-stateDiff`,
  the same unpriced call without blob fields.

## Results

| Build | BLOBBASEFEE | Blob fee charged |
| --- | --- | --- |
| Anvil dev, 1.8.4 | 1 | 131072 |
| Besu dev | 1 | 131072 |
| Besu 26.9 | 1 | 131072, beside a gas charge it also takes from the unpriced twin |
| Erigon dev | 1 | 131072 |
| Erigon 3.7.1 | 1 | none |
| Geth draft | 1 | 131072 |
| Nethermind dev, 2.1 | 1 | 131072 |
| Reth dev, 2.7 | 1 | none |

Every build runs the call, and its eth_call twin returns the factory's child address everywhere. Reth and Erigon 3.7.1
report no sender balance change, the same gap they show on the priced `blob-fee-priced-stateDiff`; Erigon's development
build already charges it.

This answered a question from the Nethermind fork-rule work: Nethermind's unit test chain returned "insufficient funds
… required balance exceeds 256 bits" for this call shape. On a real chain both Nethermind builds run it and charge
the blob fee, so that error belongs to the test chain's header, not to the RPC path, and no Nethermind fix follows.
