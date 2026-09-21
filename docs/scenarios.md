# Stateful scenarios

All mutations below target disposable Hive databases. They never connect to an existing node.

## Canonical reorg and restoration

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --corpus reorg-safe --output runs/reorg
```

The small adapter imports branch A, queries it, submits branch B's alternate tail through
the Engine API, changes forkchoice, queries B, then restores A and queries it again. The
safe marker is on the common prefix. All three phase controls are mandatory, so a case
selector selects the complete scenario. `reorg` retains the earlier strict-marker variant.

Each phase must expose the expected canonical hash. An Engine rejection or an unverified
switch is a setup/coverage failure, not evidence that a client returned a wrong trace.
The dated baseline includes Erigon forkchoice failures and preserves that gap.

## Unavailable historical state

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --clients reth_release,reth_development --corpus pruned --output runs/pruned
```

Only Reth has a verified pruning adapter in this milestone. It imports the tiny chain,
prunes account/storage history before block 44, and starts the RPC node. Old headers and
receipts must remain readable, a latest-state call must succeed, and historical traces
must report explicit pruned-state errors. Merely enabling a pruning flag is not proof.

Erigon, Nethermind and Besu retention scenarios remain an explicit coverage gap. Selecting
them with `pruned` fails before client execution. This limitation does not affect their
ordinary replay or historical-query probes on fully retained fixture chains.
