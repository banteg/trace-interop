# Fee and type field combinations — 2026-10-03

A focused recapture of `probes-prague` that adds 20 `combo-*` unsigned calls, each with an `eth_call` twin. It
runs with the [2026-10-02 eval](../../2026-10-02/eval/README.md)'s [build lock](../../2026-10-02/eval/clients.lock.json),
so all eleven builds are that matrix's images, and it resends every request of that matrix's `probes-prague` run
(and of the [blob-charge](../blob-charge/README.md) recapture it supersedes), so
[reports.lock.json](../../../reports.lock.json) selects it in place of those runs. Captured on Fedora from harness
commit `eaf2f72d` with disposable chains: Hive for the native builds and the Geth draft, a
[replica](../../../docs/usage.md#replica-captures) for Anvil. The manifest keeps `source_dirty: true` only because
the output folder was created first.

[probes-prague](probes-prague/summary.json) is complete: **1320 responses**, and every build passed the setup controls.

## Probe

Each call mixes fee and type fields that no signed transaction carries. The legacy price P is 2 gwei and the
dynamic caps D are 3 gwei, both above the head's base fee of about 0.77 gwei, so the GASPRICE a call sees names
the fee that priced it. A creation returns GASPRICE; an authorization call to key 1 returns the delegated
marker's 42 when the authorization applied; a blob call goes through the genesis CREATE2 factory, whose child
deploys GASPRICE (BLOBBASEFEE is H15's, under the `blob-fee-*` probes).

## Findings

`trace_call` outcomes: P or D is the GASPRICE observed, `42` an applied authorization, `no auth` a call that ran
without it, and a code is a rejection. The Geth draft follows the profile
and is not a precedent.

| Case | Fields | Besu dev | Besu 26.9 | Erigon dev | Erigon 3.7.1 | Nethermind dev | Nethermind 2.1 | Reth dev | Reth 2.7 | Anvil dev |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `gasprice-maxfee` | gasPrice P, maxFee D | 2765625000 | 2765625000 | `-32000` | P | `-32000` | `-32000` | `-32602` | `-32602` | D |
| `gasprice-tip` | gasPrice P, tip D | `-32000` | `-32603` | `-32000` | P | `-32000` | `-32000` | `-32602` | `-32602` | `-32602` |
| `gasprice-dynamic` | gasPrice P, maxFee D, tip D | D | D | `-32000` | P | `-32000` | `-32000` | `-32602` | `-32602` | D |
| `gasprice-dynamic-equal` | gasPrice P, maxFee P, tip P | P | P | `-32000` | P | `-32000` | `-32000` | `-32602` | `-32602` | P |
| `untyped-dynamic` | maxFee D, tip D | D | D | D | D | D | D | D | D | D |
| `type0-gasprice` | gasPrice P, type 0 | P | P | P | P | P | P | P | P | P |
| `type0-dynamic` | maxFee D, tip D, type 0 | D | D | D | D | 0 | 0 | D | D | D |
| `type1-gasprice` | gasPrice P, type 1 | P | P | P | P | P | P | P | P | P |
| `type1-dynamic` | maxFee D, tip D, type 1 | D | D | D | D | 0 | 0 | D | D | D |
| `type2-gasprice` | gasPrice P, type 2 | P | P | P | P | P | P | P | P | P |
| `type2-dynamic` | maxFee D, tip D, type 2 | D | D | D | D | D | D | D | D | D |
| `auth-type4-dynamic` | maxFee D, tip D, type 4 + auth | 42 | 42 | 42 | no auth | 42 | 42 | 42 | 42 | 42 |
| `auth-type4-gasprice` | gasPrice P, type 4 + auth | `-32603` | `-32603` | 42 | no auth | 42 | 42 | 42 | 42 | 42 |
| `auth-gasprice-dynamic` | gasPrice P, maxFee D, tip D + auth | 42 | 42 | `-32000` | no auth | `-32000` | `-32000` | `-32602` | `-32602` | 42 |
| `auth-type2-dynamic` | maxFee D, tip D, type 2 + auth | 42 | 42 | 42 | no auth | no auth | no auth | 42 | 42 | 42 |
| `blob-type3-dynamic` | blob cap 1, maxFee D, tip D, type 3 + blob | D | D | D | D | D | D | D | D | D |
| `blob-gasprice` | gasPrice P + blob | 0 | P | P | P | P | malformed JSON | P | P | P |
| `blob-gasprice-capped` | gasPrice P, blob cap 1 + blob | P | P | P | P | P | P | `-32602` | `-32602` | 0 |
| `blob-type3-gasprice` | gasPrice P, blob cap 1, type 3 + blob | P | P | P | P | P | P | `-32602` | `-32602` | 0 |
| `blob-type2-dynamic` | blob cap 1, maxFee D, tip D, type 2 + blob | D | D | D | D | D | D | D | D | D |

Source reading at the measured commits (see [H14](../../../reports/decisions/H14.md)) explains each row:

- Upstream Geth, Erigon's development build, Nethermind and Reth reject gasPrice with dynamic fee fields. Besu
  fills a missing dynamic field from gasPrice (2765625000 is the 2 gwei gasPrice as the tip plus the base fee,
  under the 3 gwei cap), Anvil drops gasPrice, and Erigon 3.7.1's own `trace_call` parameter type lets it win.
- Every client but Nethermind ignores `type`. Nethermind lets an explicit type choose the transaction class and
  silently drops the fields that class lacks, so type 0 or 1 with dynamic fees runs at GASPRICE 0 and type 2 with
  an authorization list ignores it.
- Besu's -32603 for gasPrice with an authorization is a `NoSuchElementException` on the missing max fee. Its
  development build runs an uncapped blob call unpriced (GASPRICE 0), which besu#11432 changes.
- Reth rejects gasPrice with `maxFeePerBlobGas` through the dynamic-fee check, with its misleading message, and
  Anvil drops gasPrice when a blob fee cap is present (GASPRICE 0).
- Erigon 3.7.1's `trace_call` drops authorization lists and blob fields entirely; its development build applies them.
