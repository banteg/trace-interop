# Block-selector disagreements: live capture

Captured on Fedora on 2026-09-23 against the eight pinned release and development
images in `locks/clients-2026-09-21.json`. Hive imported fixture chain `a`, with
head `0x30` (48). The 13 discriminator requests are in the committed
[h30 corpus](../../../fixtures/corpora/h30.json) and the original [cases.json](cases.json).
The runner adds independent `eth_getBlockByNumber` controls for the numbered
head and `latest`, plus `web3_clientVersion`.
Both controlled runs had complete setup, four eligible clients and 64/64
transport exchanges. The copied
run files match every SHA-256 entry in their `checksums.json` files.

| Capture | Responses | Builds |
| --- | ---: | --- |
| [Development](h30-dev-controlled-20260923/summary.json) | 64 | Besu `d997aad`, Erigon `c25b8e47`, Nethermind `a404c4f0`, Reth `03cb186c` |
| [Release](h30-release-controlled-20260923/summary.json) | 64 | Besu 26.8.1, Erigon 3.6.1, Nethermind 1.39.3, Reth 2.6.0 |

The [initial development](h30-dev-20260923/summary.json) and
[initial release](h30-release-20260923/summary.json) captures lacked that
`latest` control, so the report inventory uses the controlled reruns. Their 13
discriminator responses are identical to the corresponding controlled runs.

## Results

`trace_filter({"count":3})` returns its first three records from block **48** on
Besu and Nethermind, and from block **1** on Erigon and Reth, in both build sets.
When only `toBlock: "0x2"` is supplied, Besu and Nethermind return range errors;
Erigon and Reth return three block-1 records. Explicit block-48 filtering is a
successful control for every client. This is a difference in the omitted
`fromBlock` default, not address-filter composition.

The constructor `0x4360005260206000f3` returns `NUMBER` as a 32-byte output.
All four clients return **48** for `trace_call` at `latest`. With an omitted
`trace_callMany` block, Erigon and Nethermind return **48**, Reth returns **49**,
and Besu rejects the one-argument request with `-32602`. Supplying `latest`
explicitly makes all four return **48**. Both build sets show this result. The
Reth difference is therefore visible in the block environment even without
pending mempool transactions.

For `trace_filter` with `safe` bounds, Erigon and Nethermind return block-48
records, Reth rejects the tag with `-32602`, and Besu returns `-32603`. With
`pending` bounds, Reth and Besu still error, Nethermind returns block-48
records, Erigon release returns block-48 records, and Erigon development
rejects pending with `-32000`. For `trace_call` and `trace_callMany` at explicit
`pending`, Reth returns **49**, Besu and Nethermind return **48**, and Erigon
development rejects the request; Erigon release returns **48**. This fixture
distinguishes block environment but does not prove which pending transactions
each client would include.

## Decisions recorded

1. **[H30](../../../reports/decisions/H30.md): `trace_filter` omitted bounds.** Decide whether an omitted
   `fromBlock` means earliest available or latest. At capture time, the draft
   described earliest-to-latest and the observed clients split 2–2. H30 now
   proposes latest/latest after reviewing the originating Parity behavior and
   `eth_getLogs`. Explicit historical queries on a pruned node still need a
   separate check.
2. **[H31](../../../reports/decisions/H31.md): `trace_callMany` block default and optionality.** Decide whether the
   block argument is optional and, if omitted, whether calls use latest or
   pending. The draft profile says trace calls default to latest. Besu requires
   the argument; Reth executes in the pending block environment.
3. **[H32](../../../reports/decisions/H32.md): accepted block tags and pending semantics.** Decide which tags each
   trace method accepts and what `pending` means. The draft filter schema lists
   `pending`, while the draft profile explicitly leaves pending localization
   open. This needs a contract decision before treating every rejection or
   latest fallback as an implementation defect.

These are distinct from H03 address matching and H14 malformed-parameter
codes. Nethermind's explicit range starting at genesis returns `[]` in this
capture; its genesis/history handling is already tracked by
[Nethermind #13677](https://github.com/NethermindEth/nethermind/pull/13677)
and is not proposed as another decision here.

## Provenance and limits

The runner used a detached Fedora worktree at `88ec753` and added a temporary
`h30` corpus mapped to chain `a`. Its older runner needed the `latest` control
included in that temporary corpus for the controlled reruns; the current
runner adds it automatically. The manifests truthfully record
`source_dirty: true`. No client source or pinned image was changed. Each
manifest contains the selected requests, image IDs, source revision, runner
hash and fixture head; raw Hive logs and parsed observations are retained in
the linked run directories. The observations are evidence of these pinned
builds on the disposable chain, not a claim about every current release or
client-team agreement. The live mainnet Reth service was not used for these
cross-client tests.
