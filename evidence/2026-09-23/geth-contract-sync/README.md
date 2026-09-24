# Geth trace contract update

Source: [c36ee43e38](https://github.com/banteg/go-ethereum/commit/c36ee43e3827331276d045bd56d1297e4c3c9b15),
compared with [40eecf3647](https://github.com/banteg/go-ethereum/commit/40eecf3647f26546df9dbf72ce48f372df469ef2).
The [build lock](geth-lock.json) pins the clean source, toolchain, base image and binary.
The [reference rebuild](rebuild-lock.json) reproduced the binary SHA-256:

`09221759120b5309160772458954b24bbc43849424cb0e1cbc4e6ed33d1ea871`

## Result

439 eligible RPC observations, including 304 trace requests, across eleven corpora.
All 875 evaluated semantic assertions match and all 220 schema-checked results are valid.
There are 87 unassessed declared-topic checks and four policy observations: the raw
transaction third argument and three pending-tag requests. This does not establish
complete conformance or upstream Geth adoption.

The update fixes unknown-block and signed-validation error codes, accepts standard
unsigned blob/authorization fields, ignores unknown call fields, makes earliest mean
genesis, and reports unavailable transaction lookup history rather than asserting absence.
Pruned-index classification is unit-tested; the full pruning capture remains Reth-specific.

## Regression and repository checks

The [final regression tests on the old head](validation/geth-contract-before-final.log)
fail for all eight targeted groups. A Go overlay supplied the new tests without editing
the old checkout. The fixed source passed [32 namespace tests/subtests](validation/geth-contract-tests.json)
and the [race-enabled namespace suite](validation/geth-contract-race.log).

The same file hashes were verified between the tested checkout and committed source.
Required checks passed with Go 1.26.1:

- `make all`: [build log](validation/geth-contract-build.log).
- `go run ./build/ci.go test`, without `-short`, including execution-spec fixtures and
  the keeper module: [full log](validation/geth-contract-full-v2.log).
- `go run ./build/ci.go lint`: [lint log](validation/geth-contract-lint.log).
- `go run ./build/ci.go check_generate`: [generated code and tidy log](validation/geth-contract-generate.log).
- `go run ./build/ci.go check_baddeps`: [dependency log](validation/geth-contract-deps.log).
- Modified Go files were formatted with `gofmt` and `goimports`.

The full suite used an isolated network namespace to avoid test-port collisions.
An initial attempt needed a missing checksum cached by `TestBindings`; after that
networked cache warm-up, the complete isolated rerun passed. No test was skipped to
work around that failure.

The tracker passed all 96 tests, frozen-input verification and schema checks.
Regeneration was deterministic. Native-client assessments are unchanged, and every
previously matching Geth assertion still matches.

## Captures

Harness source: `1ace6fb7e850ae6f1da794b91f803c5df03c3025`; draft:
`9317297a1fcdf1055baac989d1747e340291c61a`. Each capture records clean source provenance,
image identity, setup controls, requests, responses and file checksums.

| Corpus | RPC observations | Evidence |
| --- | ---: | --- |
| `a` | 91 | [Manifest](geth-contract-a/manifest.json) · [Responses](geth-contract-a/observations.json.gz) |
| `callmany-isolation` | 10 | [Manifest](geth-contract-callmany-isolation/manifest.json) · [Responses](geth-contract-callmany-isolation/observations.json.gz) |
| `fork-followup` | 21 | [Manifest](geth-contract-fork-followup/manifest.json) · [Responses](geth-contract-fork-followup/observations.json.gz) |
| `forks` | 65 | [Manifest](geth-contract-forks/manifest.json) · [Responses](geth-contract-forks/observations.json.gz) |
| `h30` | 16 | [Manifest](geth-contract-h30/manifest.json) · [Responses](geth-contract-h30/observations.json.gz) |
| `initial` | 69 | [Manifest](geth-contract-initial/manifest.json) · [Responses](geth-contract-initial/observations.json.gz) |
| `precompile-values` | 15 | [Manifest](geth-contract-precompile-values/manifest.json) · [Responses](geth-contract-precompile-values/observations.json.gz) |
| `precompiles` | 19 | [Manifest](geth-contract-precompiles/manifest.json) · [Responses](geth-contract-precompiles/observations.json.gz) |
| `raw-validation` | 71 | [Manifest](geth-contract-raw-validation/manifest.json) · [Responses](geth-contract-raw-validation/observations.json.gz) |
| `reorg-safe` | 18 | [Manifest](geth-contract-reorg-safe/manifest.json) · [Responses](geth-contract-reorg-safe/observations.json.gz) |
| `repeat` | 44 | [Manifest](geth-contract-repeat/manifest.json) · [Responses](geth-contract-repeat/observations.json.gz) |

Reproduce with the pinned source and `scripts/build_geth.py --reference geth-lock.json`,
then `trace-interop run --lock <rebuilt-lock> --corpus <corpus> --output <new-directory>`.
Previous captures remain unchanged; the report inventory selects these current runs.
