# Assertion models and coverage

The assessment distinguishes an evaluated property from a successful RPC request.
`matches` and `change_needed` describe a specific assertion. `blocked` means that
setup, transport, method availability or a prerequisite prevented evaluation.
`control` identifies reference evidence, and `not_applicable` explains why an
execution property does not apply (for example, to a correctly rejected signed
transaction). Neither is a pass. An absent assertion remains `unassessed`.

The technical appendix lists each unevaluated obligation and its reason. A
response can have an evaluated failure and a blocked property simultaneously;
the displayed verdict prioritizes the failure while the coverage table preserves
the incomplete assessment.

## Independent inputs

`chain_model.py` decodes the frozen RLP blocks, hashes transactions and recovers
transaction senders and EIP-7702 authorities. This supplies complete transaction
inventories, rather than the original `txinfo` index, which intentionally indexed
only selected transaction generators. Block replay must return every transaction
in order. Root traces must preserve those hashes and recovered senders.

Genesis, preceding signed transactions and recovered authorization tuples model
account existence and delegation changes. This is specific to the retained
chains: their persistent creations are top-level; the calltree's internal child
self-destructs in its creation transaction. It is not a general state-transition
engine for arbitrary chains.

Fresh captures retain receipt gas for mined replays and block-trace references
for filters. Receipt identity is checked against the decoded transaction and block.
Receipt data is an independent RPC witness, not a second implementation or a
cryptographic receipt proof. Relational checks only use successful responses;
missing or invalid witnesses cannot establish agreement.

## Executable models

| Property | Model |
| --- | --- |
| VM instructions | The bounded interpreter computes opcode costs, post-step gas, stack values, actual memory writes, return bytes and REVERT outcome from fixture code. It rejects unsupported instructions, missing environment/storage, OOG and resource-bound violations. |
| Memory | MLOAD with and without expansion, MCOPY including overlap and zero length, MSTORE, RETURN and empty output distinguish writes from snapshots and allocation. |
| Environment | A creation program returns GASPRICE, BASEFEE, NUMBER, TIMESTAMP and GASLIMIT. Zero and nonzero fees use the same frozen block values. |
| Creation | The constructor address is derived from sender/nonce. Deployed bytes come from independent execution. Empty code and zero balance still require creation markers. |
| Transfer accounting | Known empty recipients and a funded sender establish exact 21000-gas debits, value credits, miner tips, base-fee burn and nonce changes. The second call starts from the first call's post-state. |
| Broader accounting | Balance deltas conserve value, credit the miner and burn base fee using receipt gas, or an explicitly identified root-gas witness. This does not independently prove every internal transfer or refund. |
| Replay and authorization | Decoded transaction ordering, recovered authorization authorities, before/after delegation code and genesis/initcode root execution sources. |
| Filtering | Independently anchored block inventories, address selection, count zero, pagination, past-end pages and canonical roots across reorg phases. |
| Storage refunds | SSTORE follows EIP-2200, EIP-2929 and EIP-3529 for slots a corpus anchors at transaction start. The replay VM check and the root-gas accounting fallback use the exact capped refund. |
| Mined probes | [Mined-probes](mined-probes.md) transactions carry hand-derived frames, account diffs, balance deltas, receipt gas and SSTORE effects for each replay and block trace. Filters over them pin exact frame identities. Accounting subtracts the wei that a same-transaction SELFDESTRUCT to self destroys. |

`local_invariants` additionally checks nested VM bytecode/PUSH consistency,
post-step gas arithmetic outside CALL/CREATE, and the absence of write deltas on
memory reads and returns. This catches timing defects in complex programs but is
not independent execution of those programs. Detailed trapped-call gas boundaries,
warm-access reset, refunds outside anchored straight-line programs and arbitrary nested state
execution remain outside the bounded model. A topic receiving an assertion is
not proof of every recommendation in that topic.

The VM comparator treats pushed words numerically. H21 separately checks minimal
wire quantities. Optional mnemonic labels must agree with bytecode when present;
the models do not invent a convention for optional `idx` numbering.

The Prague intrinsic/floor distinction follows
[EIP-7623](https://eips.ethereum.org/EIPS/eip-7623), creation metering follows
[EIP-3860](https://eips.ethereum.org/EIPS/eip-3860), and tip/burn accounting follows
[EIP-1559](https://eips.ethereum.org/EIPS/eip-1559). The trace serialization rules
are the repository's proposed contract, not an assertion of client consensus.

## Reproduce

```sh
uv run python scripts/build_coverage_fixtures.py
uv run python -m unittest discover -s tests -v
uv run python scripts/run_matrix.py --output runs/coverage-matrix
```

The matrix runs sequentially because one Hive checkout owns the mutable simulator
build context. It resolves current builds, checks freshness, freezes their identities
for the suite, retains failed/incomplete runs, and exits
nonzero if any capture is incomplete. Run output should remain under ignored
`runs/` until it is frozen into evidence, so generated logs do not mark later
captures as dirty. The experimental Geth fork participates separately; only the
two Reth builds use the verified pruning adapter.
