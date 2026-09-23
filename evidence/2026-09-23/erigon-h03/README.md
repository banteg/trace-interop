# Erigon H03 implementation

[Erigon #24255](https://github.com/erigontech/erigon/pull/24255) implements the
[H03 recommendation](../../../reports/decisions/H03.md) following
[Erigon's feedback](https://github.com/ethereum/execution-apis/issues/890#issuecomment-5784143408).
Head: `64f1ab04f8d1fc0fd3d02549ce2e9b08b101c6aa`; tested base:
`12b6b3391b8038d0dc89fac593fcad8e5ea022f8`.

The default is AND between populated address lists, with OR within each list.
Explicit union and intersection remain supported. Empty sides are unrestricted
in the index scan and per-trace matching. Unknown, empty, null and non-string mode
values return `-32602`; an omitted mode uses the default. The documentation explains
that queries for all activity involving X must explicitly request union when they
supply X in both lists.

## Validation on Fedora

Ten regression subtests fail against the original implementation and pass with
the fix. The final tests use JSON-RPC requests and a real indexed chain, including
one-sided/null/empty lists, both-list composition, the migration case and pagination.
The complete `rpc/jsonrpc` package passes: 649 top-level tests, 3,333 including
subtests, no failures or skips. Full lint reports zero issues and the `erigon` and
`integration` binaries build. Local source hashes match the tested Fedora files.

The documentation site builds and all generated text artifacts match. Of 226
script tests, 225 pass. The remaining assertion expects the absent CSS class
`theme-doc-footer`; it also fails after rebuilding with the unchanged upstream
trace page. That unrelated failure is disclosed in the PR and was not muted.

[Validation summary](validation.json) records the failing baseline cases and commands.
The [upstream CI gate](https://github.com/erigontech/erigon/actions/runs/35851717201)
needs maintainer approval. The PR is mergeable and has review requests, including
lupin012. This is native validation of an open patch, not a new cross-client capture
or proof of merged/released behavior. H03 remains converged on direction.
