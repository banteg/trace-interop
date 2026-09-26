# Mined transaction probes

Some source-review findings concern behaviour that only a mined transaction can show:
replay of a block's own pre-transaction system calls, the result shape of a failed
CREATE in a block trace, SELFDESTRUCT inside the creating transaction, refunds that
separate root `gasUsed` from receipt gas, and several EIP-7702 tuples folded into one
diff. The `mined-probes` chain holds one small probe family per block, so every
expectation can be derived by hand from the frozen chain rather than learned from a
client response.

## Chain

A six-block Prague chain with the fork schedule of `raw-validation`. Public fixture
key 1 (`0x7e5f…5bdf`) sends every transaction with a 2 gwei tip. The fee recipient is
the zero address, which the first transaction creates.

| Block | Transaction | Program | Decisions |
|---|---|---|---|
| 1 | `blob-transfer` | type 3, one blob, 7 wei to absent `0x…b10b` | H16, H17 |
| 2 | `beacon-root-read` | `0x…4788` STATICCALLs EIP-4788 with its own TIMESTAMP and stores success and root in slots 1 and 0 | H16, H28 |
| 2 | `history-read` | `0x…2935` reads the EIP-2935 hash of block NUMBER−1 the same way | H16, H28 |
| 3 | `create-revert` | top-level CREATE of `0x63deadbeef5f526004601cfd` (REVERT with `0xdeadbeef`) | H09, H16, H17, H23 |
| 3 | `factory-create-revert` | factory `0x…fac0` CREATEs the same initcode and returns the address word | H09, H16, H17, H23 |
| 4 | `selfdestruct-self` | `0x…de57` (1000 wei, slot 1 = 42) runs `ADDRESS SELFDESTRUCT` | H16, H23, H26 |
| 4 | `create-destroy-absent` | factory CREATEs `30ff` with 256 wei at an absent address | H16, H23, H26 |
| 4 | `create-destroy-prefunded` | the same at the factory's nonce-3 address, which genesis funds with 5000 wei | H16, H26 |
| 5 | `refund-clear` | `0x…5501` clears slot 0 (42): refund 4800 | H09, H16, H19, H20 |
| 5 | `refund-capped` | `0x…5502` clears slots 0 and 1: refund 9600, capped at 6201 | H09, H16, H19, H20 |
| 6 | `authorizations` | type 4 to key 2, six tuples (below) | H16, H17, H18 |

The type-4 tuples, in order: key 2 (nonce 5) delegates to `0x…7702a` at nonce 5, then to
`0x…7702b` at nonce 6; a third key-2 tuple reuses the stale nonce 5 and is skipped; key 3,
absent from genesis, delegates to A at nonce 0; key 4, delegated to A in genesis at nonce
3, delegates to B and back to A. Expected net diffs: key 2 code `0x`→B and nonce 5→7; key 3
born with `+` balance 0, nonce 1 and code A; key 4 nonce 3→5 with code `=`.

## Independent expectations

[`scripts/build_mined_probes_fixtures.py`](../scripts/build_mined_probes_fixtures.py)
derives each expectation from the chain RLP, genesis and the probe programs:

- **H28.** The reader output, the slot-0 word and the STATICCALL child's output are the
  block-2 header `parentBeaconBlockRoot` and `parentHash`. Neither system contract may appear
  in the transaction diff. The root vmTrace SSTOREs must write the same words. A replay
  that skips the block's pre-transaction calls (Besu #10953) diverges visibly: the EIP-4788
  call reverts, leaving slot 1 zero and the input timestamp in slot 0, and the EIP-2935
  call returns a zero hash.
- **H09.** A reverted CREATE, top-level or nested, has error `Reverted` and result exactly
  `{gasUsed: 0x11, output: 0xdeadbeef}`, with no address or code. The 17 gas comes from the
  bounded VM model. The factory root keeps its success, and root `action.gas` is the
  transaction gas minus intrinsic gas. For the refund probes, root `gasUsed` is execution
  gas before the refund (5004 and 10009), not the receipt figure.
- **H23.** Filters over block 3 must not match either would-be address by `toAddress`,
  must match the creator by `fromAddress`, and must keep the creator match under `union`
  but not under intersection. Over block 4, the created-then-destroyed address matches its
  create frame and its suicide beneficiary, and the self-destructing contract matches on
  both sides. Each filter pins the exact `(transactionHash, traceAddress, type)` list.
- **H26.** The pre-existing contract survives, so it has no account diff. Its suicide
  frame moves its whole 1000 wei to itself. An account created and destroyed in one
  transaction has no diff; the prefunded one is a deletion with `-` balance 5000, `-`
  nonce 0, `-` code `0x` and storage `{}`. Suicide frames carry 256 and 5256 wei.
- **H16.** Sender and fee-recipient deltas are exact for every transaction whose gas is
  derived by hand, and nonce and storage transitions are pinned. The generic
  conservation oracle subtracts the corpus's `destroyed_wei`: the balance that a
  same-transaction SELFDESTRUCT to self burns (256 and 5256 wei).
- **H17/H18.** New accounts carry `+` markers for every field; would-be addresses of
  failed creations have no diff. The generic H18 oracle folds the decoded tuples, and the
  corpus also pins each authority's full hand-derived diff.

Receipt gas per transaction, derived without any client:

| Transaction | Intrinsic | Execution | Refund | Receipt |
|---|---|---|---|---|
| `blob-transfer` | 21000 | 0 | 0 | 21000, blob gas 131072 at 1 wei |
| `create-revert` | 53194 | 17 | 0 | 53211 |
| `factory-create-revert` | 21192 | 32050 | 0 | 53242 |
| `selfdestruct-self` | 21000 | 5002 | 0 | 26002 |
| `create-destroy-*` | 21032 | 37035 | 0 | 58067 |
| `refund-clear` | 21000 | 5004 | 4800 | 21204 |
| `refund-capped` | 21000 | 10009 | min(9600, 31009/5) = 6201 | 24808 |

Factory execution is `CALLDATASIZE PUSH0 PUSH0` (6), `CALLDATACOPY` (3 + 3 per word + memory
expansion), `CALLDATASIZE PUSH0 CALLVALUE` (6), `CREATE` (32000 + 2 per initcode word) plus
the child's used gas, then `PUSH0 MSTORE PUSH1 PUSH0 RETURN` (10). A SELFDESTRUCT to its own
warm, non-empty address costs 5000. The bounded VM model now executes SSTORE under
EIP-2200, EIP-2929 and EIP-3529 for slots whose transaction-start values the corpus anchors
(`storage_anchors`). The replay H20 check and the H16 root-gas fallback therefore use the
exact refund instead of a one-fifth bound. A unit test checks the derived receipts
against the consensus `gasUsed` of every block whose gas is fully derived (blocks 1, 3, 4
and 5).

## Controls

A run is eligible only when every setup control matches: the frozen head and latest block,
and the post-chain state at `latest`. The state controls are the reader slots and the
system-contract ring-buffer slots, the factory nonce, the surviving contract's code,
balance and storage, the destroyed addresses, the cleared slots, each authority's code and
nonce, the sender nonce and the blob recipient. Receipt controls pin `status` and, where
derived, `gasUsed`, `blobGasUsed` and `blobGasPrice` through `expected_control_fields`.
Each replay also retains its generic `_control/receipt/<hash>` witness.

## Reproduction

Capture the corpus on Linux with Docker:

```sh
uv run python scripts/run_matrix.py --corpora mined-probes --output runs/mined-probes-current
```

To regenerate the chain, copy `fixtures/generators/mined_probes_test.go` into
`cmd/hivechain/` in ethereum/hive at `43ea47bef5761351e3da7b726050ea80ab362c52`, then run:

```sh
TRACE_MINED_OUTPUT=/fresh/output GOTOOLCHAIN=go1.26.1 \
  go test ./cmd/hivechain -run '^TestMinedProbes$' -count=1 -v
```

Copy the output files into `fixtures/chains/mined-probes/`. Then rebuild the corpus and its
checksums:

```sh
uv run python scripts/build_mined_probes_fixtures.py
```

Two generator runs give byte-identical files. The pinned chain maker applies the
EIP-4788 system call after the block callback, whereas block import applies it before the
first transaction. The generator therefore writes the same two ring-buffer slots before
block 2's transactions. The generator's own import, which runs the real block processor,
then validates every block.

Before the matrix capture, the corpus was checked against a local
[Geth draft fork](geth.md) build (`banteg/go-ethereum` `feat/trace` at `0a663f3c`). That
build imported the chain and passed every setup control, and every assertion matched.
This validates the oracles against the draft; it does not replace the full client matrix.

These probes do not cover pre-Cancun SELFDESTRUCT, trapped nested-call gas, blob fee
collectors or authorization tuples with a foreign chain ID.
