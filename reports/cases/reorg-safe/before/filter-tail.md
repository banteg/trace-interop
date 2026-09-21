# reorg-safe/before/filter-tail

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x28",
      "toBlock": "0x30"
    }
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


Draft result schema: **invalid**.
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


Draft result schema: **invalid**.
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **False**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


Draft result schema: **invalid**.
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property
- `7`: 'transactionHash' is a required property
- `7`: 'transactionPosition' is a required property
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `10`: 'transactionHash' is a required property
- `10`: 'transactionPosition' is a required property
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


Draft result schema: **invalid**.
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property
- `7`: 'transactionHash' is a required property
- `7`: 'transactionPosition' is a required property
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `10`: 'transactionHash' is a required property
- `10`: 'transactionPosition' is a required property
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **False**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-ready/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


Draft result schema: **invalid**.
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


Draft result schema: **invalid**.
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52
- `15`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'erro
- `18`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e521fb2d33330a72c8b7aa2bf1b2281ffe', 'blockNumber': 43, 'result': {'address': '0x05
- `30`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'error':
- `33`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431
- `35`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'erro
- `38`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6d70b', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x5b3627e612c821267b54826693cfde431298fd7cdb8f8ec6ea90d952c494e7e8', 'blockNumber': 46, 'result': {'address': '0x9e

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **False**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


Draft result schema: **invalid**.
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property
- `7`: 'transactionHash' is a required property
- `7`: 'transactionPosition' is a required property
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `10`: 'transactionHash' is a required property
- `10`: 'transactionPosition' is a required property
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


Draft result schema: **invalid**.
- `3`: 'transactionHash' is a required property
- `3`: 'transactionPosition' is a required property
- `7`: 'transactionHash' is a required property
- `7`: 'transactionPosition' is a required property
- `9`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6cb3089f8b5ff993ed24ed9ccbfa8bae322848d722842e6453576f30029b1434', 'blockNumber': 42, 'error':
- `10`: 'transactionHash' is a required property
- `10`: 'transactionPosition' is a required property
- `13`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x22e8e9edaefc674ba389450dc41088e52

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **False**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../../evidence/2026-09-21/verified-reorg-safe/observations.json).


Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": [
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x036464a71961a53a656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x0efc1e4671e41e768fa107ecf72ab35e03d5a8b7e3f5bbe29cb28dc1eea265a2",
      "transactionPosition": 0,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0x9ec58f808778768f656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x2"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0x1942a6223310f991ab036dccb28259dd634e39e08152d383afc422481e5ab2c2",
      "transactionPosition": 1,
      "type": "call"
    },
    {
      "action": {
        "callType": "call",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x11ba0",
        "input": "0xcd417355d4039279656d6974",
        "to": "0x7dcd17433742f4c0ca53122ab541d0ba67fc27df",
        "value": "0x3"
      },
      "blockHash": "0xfc2b688f6d286950eff2cf6f1b10a6bf63e92a20fcdf8db7377ef647b154eb52",
      "blockNumber": 40,
      "result": {
        "gasUsed": "0x5f9c",
        "output": "0x"
      },
      "subtraces": 0,
      "traceAddress": [],
      "transactionHash": "0xbc3230ca851b7baad39753405e55d96f2124d1e5e8ab9cd76c638bb
… preview truncated; use the full evidence link above.
```

</details>

