# forks/block-60

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x3c"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- `5`: 'transactionHash' is a required property
- `5`: 'transactionPosition' is a required property

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **change_needed** — A PoS block has no synthetic PoW reward records.
- H09: **change_needed** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **invalid**.
- `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767', 'blockNumber': 60, 'error':
- `5`: 'transactionHash' is a required property
- `5`: 'transactionPosition' is a required property

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).

- H05: **matches** — A PoS block has no synthetic PoW reward records.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "creationMethod": "create",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x4b0e",
        "init": "0x600d380380600d6000396000f336156009575f355f555b305f525f5460205260405ff3",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "address": "0xfdb19a177ed1b386d141e392b7a27467469fabb2",
        "code": "0x36156009575f355f555b305f525f5460205260405ff3",
        "gasUsed": "0x114d"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x7a4a9d54552bc6b4b024a707408e6c304ead4f2de44a131ecb98c03998b1f153",
      "transactionPosition": 0,
      "type": "create"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x0",
        "input": "0x",
        "to": "0x0000000000000000000000000000000000000000",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x0",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x2eeede94c04e0a644f532b31b9cb71387ba69a26323fed48fa3a7dae6eb23084",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0xbef8",
        "input": "0x696e766f6b6564",
        "to": "0xeda8645ba6948855e3b3cd596bbb07596d59c603",
        "value": "0x0"
      },
      "blockHash": "0x9732abf48d7d692097d80da5ae6d726f466d264bee9b657ab9e89544453d2767",
      "blockNumber": 60,
      "result": {
        "gasUsed": "0x56ec",
        "output": "0x000000000000000000000000eda8645ba6948855e3b3cd596bbb07596d59c603696e766f6b656400000
… preview truncated; use the full evidence link above.
```

</details>

