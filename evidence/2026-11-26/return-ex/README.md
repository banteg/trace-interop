# H20 RETURN `ex` — 2026-11-26

A focused recapture of `probes-prague` that adds six vmTrace cases about a creation's RETURN. It runs with the
[2026-11-25 eval](../../2026-11-25/eval/README.md)'s [build lock](../../2026-11-25/eval/clients.lock.json)
(`trace_interop run --lock`), so every build is that matrix's image. It resends every request of that matrix's
`probes-prague` run, so [reports.lock.json](../../../reports.lock.json) selects it in place of that run. Captured
on Fedora from harness commit `f3899aed`.

[probes-prague](probes-prague/summary.json) is complete: **1,507 responses**, and every build passed the setup
controls.

## Probes

The draft gives `ex: null` only to an operation that began executing and halted exceptionally. Besu's tracer
also writes a failed code deposit's halt onto the creation's last traced operation, and #11353 and #11286 each
decide in their own way whether an operation's halt is its own. These cases check what the reference clients do:

- `vm-return-deposit-oog` returns 24,000 bytes the creation cannot pay to deposit. The RETURN and the PUSH before
  it completed, so both keep `ex`.
- `vm-mcopy-deposit-oog` puts an MCOPY right before that RETURN.
- `vm-return-oog` RETURNs 2^32 bytes, so the RETURN itself runs out of gas expanding memory and has `ex: null`.

Each runs as the root creation and, with `-nested`, as a child CREATE, whose own operation keeps `ex`.

## Findings

| Builds | Deposit fails, root | Deposit fails, child | RETURN out of gas, root | RETURN out of gas, child |
| --- | --- | --- | --- | --- |
| Erigon, Nethermind, Reth, Anvil (both builds each), Geth draft | `ex` | `ex` | `ex: null` | `ex: null` |
| Besu 26.11.2 and develop | `ex` | RETURN `ex: null` | RETURN `ex` | `ex: null` |

The operation before the RETURN, MCOPY included, keeps `ex` in every build. Besu writes the deposit failure onto
the RETURN itself, not the operation before it, and drops a child's report for any out-of-gas halt and never a
root's. A halt-check helper for #11353 and #11286 therefore has to tell a RETURN that could pay for its memory
from one that could not, at the root and in a child.

A root creation whose deposit fails has envelope `output` `0x` in every build but the Geth draft, which returns
the undeployed code. The draft does not say which is right, so the VM model's H08 output check skips a root
creation whose code cannot be deposited.
