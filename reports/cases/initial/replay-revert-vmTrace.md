# initial/replay-revert-vmTrace

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    [
      "vmTrace"
    ]
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
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
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78981
          },
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78978
          },
          "op": "CALLDATALOAD",
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78975
          },
          "op": "PUSH2",
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 76875
          },
          "op": "SLOAD",
          "pc": 6,
          "sub": null
        },
        {
          "cost": 2,
          "ex": {
            "mem": null,
            "push": [],
            "store": null,

… preview truncated; use the full evidence link above.
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H01: **unsupported** — trace_replayTransaction

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H01: **unsupported** — trace_replayTransaction

<details><summary>Response preview</summary>

```json
{
  "error": {
    "code": -32601,
    "message": "Method not found"
  },
  "id": 1,
  "jsonrpc": "2.0"
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
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
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78981
          },
          "idx": "0-0",
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78978
          },
          "idx": "0-1",
          "op": "CALLDATALOAD",
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78975
          },
          "idx": "0-2",
          "op": "PUSH2",
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 76875
          },
          "idx": "0-3",
          "op": "SLOAD",
          "pc": 6,
          "sub": null
        },
        {
          "cost": 2,

… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
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
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78981
          },
          "idx": "0-0",
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78978
          },
          "idx": "0-1",
          "op": "CALLDATALOAD",
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78975
          },
          "idx": "0-2",
          "op": "PUSH2",
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 76875
          },
          "idx": "0-3",
          "op": "SLOAD",
          "pc": 6,
          "sub": null
        },
        {
          "cost": 2,

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'transactionHash': '0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae', 'vmTra

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 78981
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78978
          },
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78975
          },
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": null,
            "push": [
              "0x0000000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 76875
          },
          "pc": 6,
          "sub": null
        },
        {
          "cost": 2,
          "ex": {
            "mem": null,
            "push": [],
            "store": null,
            "used": 76873
          },

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'transactionHash': '0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae', 'vmTra

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 78981
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78978
          },
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78975
          },
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 76875
          },
          "pc": 6,
          "sub": null
        },
        {
          "cost": 2,
          "ex": {
            "mem": null,
            "push": [],
            "store": null,
            "used": 76873
          },
          "pc": 7,
          "sub": null
        },
        {

… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **change_needed** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x6000356142ff54501515603b577f4e487b71000000000000000000000000000000000000

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78984
          },
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78981
          },
          "op": "CALLDATALOAD",
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78978
          },
          "op": "PUSH2",
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78975
          },
          "op": "SLOAD",
          "pc": 6,

… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H07: **change_needed** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x6000356142ff54501515603b577f4e487b71000000000000000000000000000000000000

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x6000356142ff54501515603b577f4e487b7100000000000000000000000000000000000000000000000000000000600052600160045260246000fd5b7f08c379a0000000000000000000000000000000000000000000000000000000006000526020600452600a6024527f75736572206572726f7200000000000000000000000000000000000000000000604452604e6000fd",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78984
          },
          "op": "PUSH1",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x100000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 78981
          },
          "op": "CALLDATALOAD",
          "pc": 2,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x42ff"
            ],
            "store": null,
            "used": 78978
          },
          "op": "PUSH2",
          "pc": 3,
          "sub": null
        },
        {
          "cost": 2100,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 78975
          },
          "op": "SLOAD",
          "pc": 6,

… preview truncated; use the full evidence link above.
```

</details>

