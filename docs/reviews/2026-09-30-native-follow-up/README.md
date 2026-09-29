# Native follow-up, 2026-09-30

Latest-development native tests confirmed the signed-gas defect in Nethermind and all three signed-transaction defects in Besu. OpenEthereum 3.3.5 also confirmed the deleted-storage exception that had previously been supported only by source inspection. Client and specification builds ran exclusively on Fedora.

| Client | Source or release | Reproduction | Fix |
| --- | --- | --- | --- |
| Nethermind | master `ad22b8db86b9153abcbed9143df798a5607edb97` | 100,000 signed gas is silently lowered to 50,000 by the RPC cap; the serialized trace exposes 29,000 rather than 79,000 root execution gas | [#14060](https://github.com/NethermindEth/nethermind/pull/14060), `3f9be65b77a67312f9db85b0c1d2c1fcd197752d`: reject over-cap signed gas; preserve null/zero disabled caps |
| Besu | main `3cbf077c5d71acfcdc02a1292c9bba9416b40672`; runtime `26.9-develop-3cbf077` | Signed gas is clamped; a high-s legacy signature and an empty type-4 authorization list execute successfully | [#11395](https://github.com/besu-eth/besu/pull/11395), `703ae6cb4c6c63d75398f56fa227c8e7e5c98fb6`: process the original signed transaction with strict fork validation |
| OpenEthereum | final release 3.3.5, `6c2d392d8`, Rust 1.58.1 | A deploy/write/delete callMany bundle reports the prior slot-zero value 42 as a deleted-slot `-` entry | H26 permits accurate optional deleted-slot entries; no client PR for this valid behavior |

The Nethermind commit was rewritten at the user's explicit request to use `banteg <4562643+banteg@users.noreply.github.com>` for author and committer. Fedora's global Git identity now uses the same address. Besu was signed off at the user's explicit instruction as `banteg <4562643+banteg@users.noreply.github.com>` and marked ready; both DCO checks passed. Its source tree is identical to the validated `9b7e1eb` tree; only the sign-off changed. Neither CI approval nor merge is claimed.

## Native validation

**Nethermind.** The new serialized RPC regression spans five cap configurations and streaming on/off. On the original source, the two over-cap cases fail and eight controls pass ([log](nethermind-repro.log)). With the fix, all 278 TraceRpcModule tests pass ([log](nethermind-fixed.log)); targeted formatting verification also passed. The captured payload is a funded, valid signed transaction, so a funding rejection cannot mask the gas mutation.

**Besu.** Seven independently signed vectors under four trace selections produce 28 HTTP cases: valid legacy, high-s legacy, valid type-2, empty type-4, valid type-4, signed gas above cap, and genuine EVM out of gas. Against original main, 12 defect cases fail and 16 controls pass ([log](besu-new-tests-baseline.log)). With the fix, all 28 pass. The final focused run passed 1,291 tests with one skipped across TransactionSimulatorTest, RpcErrorTypeConverterTest and the Bonsai/Forest trace suites ([log](besu-final.log)); [spotlessCheck](besu-spotless.log) and installDist passed. The five added simulator cases verify original transaction identity and validation parameters, disabled/equal/over-cap budgets, and unsigned comparison of a gas value with its high bit set. No full-repository, acceptance, integration, reference or Hive run is claimed.

Baseline RPC captures at [30,000](besu-baseline-cap30000.json) and [50,000,000](besu-baseline-cap50000000.json) distinguish the cap problem from invalid-transaction admission. At the higher cap both invalid transactions return the marker 42. Final captures at [30,000](besu-fixed-cap30000.json), [100,000](besu-fixed-cap100000.json) and [50,000,000](besu-fixed-cap50000000.json) show the expected cap, signature and type rejections, alongside successful controls and a genuine execution halt. Sender nonce and marker storage remain unchanged after simulation.

The [genesis](besu-genesis.json) is derived from the harness raw-validation genesis, with base fee set to 1 wei so the transaction's fee covers it. It funds the public fixture key 1, starts its nonce at 10, and installs the marker at `0x0000000000000000000000000000000000001002`. These are test keys and an isolated chain, not mainnet credentials. [Signed vectors](transactions.json) preserve the exact transaction bytes.

A secondary defect exposed by the fix was error conversion: the real validator's `EMPTY_CODE_DELEGATION` had no RPC mapping and produced internal error `-32603`. The Besu PR maps it to invalid transaction type (`-32602`); the final captures verify that correction.

## OpenEthereum witness and H26

The [complete witness](openethereum-h26.json) contains version, nonce, head, the request, all three results, and the canonical code read afterwards. A genesis-only development chain, sender key 1 and nonce zero make the creation address independently calculable: `0xf2e246bb76df876cef8b38ae84130f4f55de395b`. Runtime `36156008576000ff5b602a60005500` writes 42 to slot zero with empty calldata and selfdestructs to address zero with nonempty calldata. The final result reports the account's balance, code and nonce with `-`, and storage slot zero with `{"-": "0x000000000000000000000000000000000000000000000000000000000000002a"}`. Canonical `eth_getCode` afterwards remains `0x`.

Binary provenance: [official 3.3.5 release](https://github.com/openethereum/openethereum/releases/tag/v3.3.5), asset `openethereum-linux-v3.3.5.zip`. ZIP SHA-256 `ad72c48a32d496f7a14acd3233fe51551401f1cdd12c7795570fbc5b3268cc6a`; executable SHA-256 `ea783c98df75ab1e2ac8d5c9d2a6c34be5c37664e774ab4d2f7c7872a2998233`.

This is an OpenEthereum 3.3.5 runtime witness, **not** a runtime capture of the originally pinned Parity 2.7.2 source. It verifies the dirty-prestate exception in the source review. Requiring `{}` alone would reject valid historical behavior. Account deletion still implies that every slot is wiped, regardless of the optional details; listed slots need not be exhaustive. Existing-account slots still use `*`, born-account slots use `+`, and changed-to-zero `*` entries do not represent account deletion.

The new `probes-forks/many-write-delete-storage` corpus case deploys, writes and deletes before Cancun. Its independent prestate oracle allows `{}` or accurate optional `-` values and rejects wrong old values, malformed words, wrong markers and retained code. It is a new **uncaptured** maintained-client corpus input, so it is not represented as a completed frozen-chain capture or added to the ledger's captured-case inventory.

## Draft and harness policy

[execution-apis #895](https://github.com/ethereum/execution-apis/pull/895) was updated without rewriting history at `b9febf5ea6e7e673bf361137606584bad12280a1`, and the Fedora-built artifact is pinned in spec.lock.json:

- H15: omitted gas follows the client's eth_call default at the selected state, bounded by the configured execution cap. Block limits and sender allowances may lower it. Explicit over-cap unsigned gas clamps; callers needing a portable budget supply gas.
- H06: unknown trace_block and trace_replayBlockTransactions accept null or an error; successful collections do not represent an unknown block. Unknown simulation blocks and invalid filter bounds remain errors.
- H13: strict signed-transaction admission remains required; original authenticated fields must not be reconstructed or silently clamped.
- H26: accurate optional deleted-slot `-` details are grandfathered, with no enumeration obligation.

Make build/test/lint and Go tool tests passed on Fedora; lint reported 119 existing warnings. All five documentation tests and the production documentation build passed ([build log](spec-docs-final.log), [final schema and docs tests](spec-final.log)). The docs tests exposed a pre-existing stale trace_get prose assertion; it now checks the current rejection wording. The published source files and their Fedora-built counterparts had identical SHA-256 hashes.

The earlier H15 harness commit `c720feaa` adds paired eth_call/trace defaults and an independent GAS-output cap bound, preventing equally wrong methods from passing merely because they agree. Those newly generated priced-call cases remain uncaptured corpus inputs. [Reth #27586](https://github.com/paradigmxyz/reth/pull/27586) addresses the independently confirmed default-gas cap escape; its earlier Fedora validation passed 131 unit tests, two doc tests and clippy.

Harness verification passed all 337 tests, the nine-method schema checks and generated-report stability ([log](harness-check.log)). After updating the final PR status, the reports were regenerated and all 19 report tests passed.

## Rerunning and cleanup

`python3 capture-besu.py --besu /path/to/besu --jdk /path/to/jdk --work-dir /temporary/work` starts isolated genesis nodes on HTTP 18645 and Engine 18651, captures the three cap configurations and terminates each owned process. It keeps its output and node databases inside the supplied work directory; remove that temporary directory after preserving captures.

For OpenEthereum, start the release binary with an empty data directory and `--chain dev --no-discovery --reserved-only --no-ipc --no-ws --jsonrpc-interface 127.0.0.1 --jsonrpc-port 18745 --jsonrpc-apis eth,web3,traces --jsonrpc-hosts localhost,127.0.0.1 --tracing on`. The API name is **traces**, plural. Then run `python3 capture-openethereum.py --endpoint http://127.0.0.1:18745 --output /path/to/witness.json`; stop the owned node afterwards.

All temporary client nodes were stopped. The task workspace held 4.0 GB of isolated clones, builds, databases, downloaded OpenEthereum binaries and documentation output; the entire workspace was removed after preserving evidence and pushing the fixes. A final web3_clientVersion request on port 8545 returned reth/v2.7.0-3d592ec, and PID 1213964 remained active. The existing archive Reth process, PID 1213964 on port 8545, was preserved. Shared user toolchains and caches were preserved. Evidence files have a SHA-256 manifest in checksums.json.
