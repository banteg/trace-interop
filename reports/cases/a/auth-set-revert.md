# Auth set revert

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0x04f8d4870c72dd9d5e883e818501847735940083030d40941563915e194d8cfba1943570603f7606a31155088080c0f863f861870c72dd9d5e883e9400000000000000000000000000000000000010038080a01c3f9771a572f2fdc37253483e7c67cc8d8e294276bf1dccd8ebe091477d763ba04b0d0c594ea086b9c13812d8810b1320e83b99be260518f6ff94055e04ac61fc80a0eae005bf7758c07ba75a1a0b37133bac4a0625efe1c91958ce0949a08a1bb3bda07c1d251064247970bf84ce0e9c37a44096182fba91e65d4022e080ddc396a15f",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (3 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x1563915e194d8cfba1943570603f7606a3115508', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid unde
- Result shape at `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None,

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (3 in total).
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x1563915e194d8cfba1943570603f7606a3115508', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid unde
- Result shape at `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None,

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (3 in total).
- Result shape at `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None,

</details>
