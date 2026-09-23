# Auth replace

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Failed frames have an error string and an explicit object or null result. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0x04f8d4870c72dd9d5e883e818501847735940083030d409419e7e376e7c213b7e7e7e46cc70a5dd086daff2a8080c0f863f861870c72dd9d5e883e9400000000000000000000000000000000000010038080a032b48971f74add2ebe91ce111113ff37b7f8d272ed23134e89aa7658b677ca45a05bc973423f88f2644a49fa4509864691835ff138f284a233ecba072e79dfb5f580a0d69accc0eaf71c8a02bf2b11adb6644f9b694243463e8300fc88feeff61f8884a02f3f0627d55d5268f16db3cef6ef2636ee568713e5a631e7f73656f3c0d26d76",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid unde

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid unde

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x25990', 'input': '0x', 'to': '0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x60006000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 0, 'ex': {'mem': None, 'push': [], 'store': None

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. Authority 0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a; expected {'*': {'from': '0xef01000000000000000000000000000000000000001002', 'to': '0xef01000000000000000000000000000000000000001003'}}.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x60006000fd.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. Authority 0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a; expected {'*': {'from': '0xef01000000000000000000000000000000000000001002', 'to': '0xef01000000000000000000000000000000000000001003'}}.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x60006000fd.

</details>
