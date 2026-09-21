# fork-followup/withdrawal-block-51

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_getBlockByNumber",
  "params": [
    "0x33",
    true
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **not_observed**; scenario eligible: **False**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-fork-followup-besu-retry/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "baseFeePerGas": "0x810ed7c",
    "difficulty": "0x0",
    "extraData": "0x",
    "gasLimit": "0xbebc200",
    "gasUsed": "0x2fb12",
    "hash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
    "logsBloom": "0x00000000000000000000000000000000000000000000000000000000000000000000000200000000000010000000000000000000000000000000000001000000010000000000000000004000002000000200004200400000000000000000002000000000400400000000000000000000000000000000000000000000000080000000000000000100000000000000000000000000000000010000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000",
    "miner": "0x0000000000000000000000000000000000000000",
    "mixHash": "0x0000000000000000000000000000000000000000000000000000000000000000",
    "nonce": "0x0000000000000000",
    "number": "0x33",
    "parentHash": "0x81f27dba10123293c218f7e559812921bb76397f6f7cc77d281db9e94ff4fe9b",
    "receiptsRoot": "0x67ab042bd973e8dedef30801a5589a00987c86c1ca17461677560545101482a8",
    "sha3Uncles": "0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347",
    "size": "0x35c",
    "stateRoot": "0x65aca059c8cbe1978e45591e3617d262f8d435fb832cefcf8234b0f8c72eb4e1",
    "timestamp": "0x1fe",
    "transactions": [
      {
        "accessList": [],
        "blockHash": "0x022037fe9ef69d04fd00706fcd5a9c80b1b791c6f9c3088469b6407a660c28b9",
        "blockNumber": "0x33",
        "blockTimestamp": "0x1fe",
        "chainId": "0xc72dd9d5e883e",
        "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
        "gas": "0x5208",
        "gasPrice": "0x810ed7d",
        "hash": "0x87d8ef31d0d35ae040f2998b90fd61eeb04882b21f189c521bec5c3cefb416d2",
        "input": "0x",
        "nonce": "0x72",
        "r": "0x56abc4bae751cb1703f3c3f1bcdddbf9f88c9c2f8c1416308ac46a5fdad1894e",
        "s
… preview truncated; use the full evidence link above.
```

</details>

