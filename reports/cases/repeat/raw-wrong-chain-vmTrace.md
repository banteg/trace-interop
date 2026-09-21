# repeat/raw-wrong-chain-vmTrace

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86481858477359400825208940000000000000000000000000000000000001234018026a0680e20ade3f3bfbbb3d8e2246c26a13efb3a8e886c182c159cd240b4636342b8a027a25d70c994f869fa5abe6b841ddfff0ab32944d6e9719c830ace909c024a3b",
    [
      "vmTrace"
    ]
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x",
      "ops": []
    }
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "invalid chain id for signer"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "invalid chain id for signer"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **malformed_json**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **change_needed** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "raw_response": "{\"jsonrpc\":\"2.0\",\"result\":{\"vmTrace\":\"output\":null,\"stateDiff\":null,\"trace\":[]}",
  "status": "malformed_json"
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **malformed_json**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **change_needed** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "raw_response": "{\"jsonrpc\":\"2.0\",\"result\":{\"vmTrace\":\"output\":null,\"stateDiff\":null,\"trace\":[]}",
  "status": "malformed_json"
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "invalid chain ID"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **rpc_error**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-repeat/observations.json).

- H25: **matches** — Return one complete JSON-RPC response, including on validation failure.

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32000,
    "message": "invalid chain ID"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

