# Fresh coverage matrix

Captured on Fedora with the nine pinned release/development/draft-fork images in
`clients.lock.json`. The selected captures use clean harness commit `429987c`.
Only the two Reth builds use the pruning adapter. All databases are disposable
Hive fixtures; the host's production node is not used.

`reports.lock.json` is the authoritative selection: thirteen corpora, 4,547
captured RPC responses and ten missing responses in the Erigon development reorg
scenario. The other twelve corpora captured completely. Both Reth builds
completed the reorg, unlike the earlier retained matrix.

Erigon development accepts the nine alternate payloads and then rejects the
forkchoice update with `Invalid forkchoice state`. This reproduces in
`reorg-erigon-recheck`; both incomplete captures are retained. Scenario controls
exclude its reorg observations from semantic assessment.

The initial matrix run is retained as `initial`, but its source was marked dirty
because the matrix output directory was initially untracked. `initial-clean` is
the complete clean rerun selected by the reports. The original `matrix.json`
remains an unchanged record of the first sequential run; it is not a claim that
every scenario succeeded. The duplicate initial run and focused reorg recheck
are not counted twice in reports.

Each capture's `checksums.json` authenticates its manifest, raw logs,
observations and summary. Subsequent assertion improvements are recorded
separately by `reports/assessment.json`; original responses are unchanged.

The new `coverage` corpus models VM effects, environment preservation, creation
markers and exact sequential transfer accounting. See
[assertion models](../../../docs/assertion-models.md) for scope and limitations.
