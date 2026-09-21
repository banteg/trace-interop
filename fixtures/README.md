# Fixture provenance

These are the exact small generated chains used in the September 15 investigation.
They are public test data; authorization keys in `contracts.json` are intentionally public fixture keys.

`initial` is the original 48-block Prague chain. `a` adds diagnostic contracts,
`b` is its alternate tail for reorg scenarios, and `forks` crosses historical fork boundaries.
The request corpora were prepared against these exact chain hashes. Importing a chain is
sufficient to reproduce a case; regenerating it with a newer generator may change hashes.

Generator: ethereum/hive at `43ea47bef5761351e3da7b726050ea80ab362c52`, with additional
genesis contracts documented in `../evidence/2026-09-15/contracts.json` and an alternate
tail omitting transaction modifiers from block 40. Original preparation sources are
retained in the prior evidence archive; frozen inputs are authoritative here.

Consensus/state roots, contract bytecode and expected heads are checked before interpreting
trace differences. Reorg and pruning require scenario setup beyond an ordinary import.
