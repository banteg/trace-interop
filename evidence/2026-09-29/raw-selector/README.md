# H12 raw-transaction state selection — 2026-09-29

A focused capture of the `raw-selector` corpus, which the
[2026-09-29 refresh](../refresh/README.md) did not yet contain. It reuses that matrix's
[build lock](clients.lock.json) byte for byte (`--reproduce-lock`, hence the
`historical-reproduction` [preflight](preflight.json)), so all eleven builds are the refresh's
images and [reports.lock.json](../../../reports.lock.json) selects the run beside the matrix.
Captured on Fedora from harness commit `76d826bb` with disposable chains: Hive for the native
builds and the Geth draft, a [replica](../../../docs/usage.md#replica-captures) for Anvil. The
manifest keeps `source_dirty: true` only because the matrix runner created this untracked output
folder first.

[raw-selector](raw-selector/summary.json) is complete: **176 responses**, and every build passed
the setup controls (head identity, the witness balance at blocks 0x18, 0x19 and latest, the
sender's nonce and balance, block 0x19's hash and base fee).

## Probe

One signed legacy creation from hivechain's public account `0x84e7…cc46`, which never transacts
on chain a, so its nonce is 0 and the transaction is valid at every block. The initcode returns
NUMBER, `BALANCE(0x4a0f…e9df)` and BASEFEE. The witness account receives one wei in blocks 0x19
and 0x29 (among others), so block 0x19's post-state, block 0x18's post-state and latest (0x30)
each give a different balance. [docs/assertion-models.md](../../../docs/assertion-models.md#executable-models)
describes the derivation and the H12 probe kind.

## Findings

| Request | Reth, Anvil (both builds) | Besu, Erigon, Nethermind (both builds), Geth draft |
| --- | --- | --- |
| two arguments | latest post-state, head environment (NUMBER 0x30, BASEFEE 0x199876) | the same |
| `latest` | the same as two arguments | -32602 |
| block 0x19 by number, hash, EIP-1898 object | block 0x19 post-state, block 0x19 environment (BASEFEE 0x22337ae) | -32602 |
| `pending` | latest post-state, next-block environment (NUMBER 0x31, BASEFEE 0x166670) | -32602 |

Every build runs the two-argument baseline against latest. No build ignores an explicit selector:
Reth and Anvil honor it with the selected block's post-state and header environment, and the
rest reject it as invalid params. See [the H12 report](../../../reports/decisions/H12.md).
