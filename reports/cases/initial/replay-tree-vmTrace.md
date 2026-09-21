# initial/replay-tree-vmTrace

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "vmTrace"
    ]
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

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

Capture: **unsupported**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

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

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

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
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "idx": "1-0",
          "op": "PUSH32",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 578994
          },
          "idx": "1-1",
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "idx": "1-2",
          "op": "MSTORE",
          "pc": 35,

… preview truncated; use the full evidence link above.
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

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
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "idx": "1-0",
          "op": "PUSH32",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 578994
          },
          "idx": "1-1",
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "idx": "1-2",
          "op": "MSTORE",
          "pc": 35,

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'transactionHash': '0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738', 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 578994
          },
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x20
… preview truncated; use the full evidence link above.
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H07: **matches** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **change_needed** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'transactionHash': '0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738', 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 578994
          },
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x20
… preview truncated; use the full evidence link above.
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H07: **change_needed** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 579000
          },
          "op": "PUSH32",
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
              "0x0"
            ],
            "store": null,
            "used": 578997
          },
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578994
          },
          "op": "MSTORE",
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {

… preview truncated; use the full evidence link above.
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/initial/observations.json).

- H07: **change_needed** — Individual replay includes its transactionHash.
- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested stateDiff is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H21: **matches** — Stack words use minimal hex quantities at every depth.

Draft result schema: **invalid**.
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 579000
          },
          "op": "PUSH32",
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
              "0x0"
            ],
            "store": null,
            "used": 578997
          },
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578994
          },
          "op": "MSTORE",
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {

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
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "idx": "1-0",
          "op": "PUSH32",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 578994
          },
          "idx": "1-1",
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "idx": "1-2",
          "op": "MSTORE",
          "pc": 35,

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
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "idx": "1-0",
          "op": "PUSH32",
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x0"
            ],
            "store": null,
            "used": 578994
          },
          "idx": "1-1",
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "idx": "1-2",
          "op": "MSTORE",
          "pc": 35,

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
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'transactionHash': '0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738', 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 578994
          },
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x20
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
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'transactionHash': '0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738', 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "transactionHash": "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 578997
          },
          "pc": 0,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x00"
            ],
            "store": null,
            "used": 578994
          },
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0xff01000000000000000000000000000000000000000000000000000000000000",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578988
          },
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": null,
            "push": [
              "0x20
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
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 579000
          },
          "op": "PUSH32",
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
              "0x0"
            ],
            "store": null,
            "used": 578997
          },
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578994
          },
          "op": "MSTORE",
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {

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
- ``: {'output': '0xffee', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": null,
    "trace": [],
    "vmTrace": {
      "code": "0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261ea60fa506000600060006000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60fa5060006000526000600060046000737dcd17433742f4c0ca53122ab541d0ba67fc27df61ea60f4507fff0100000000000000000000000000000000000000000000000000000000000060005260006000600260006000739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f25060006000600460006000600461ea60f15061015a38038061015a610200396102006000f050637472656560006000a16002610100f35b646368696c6460006000a133ff",
      "ops": [
        {
          "cost": 3,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [
              "0xff01000000000000000000000000000000000000000000000000000000000000"
            ],
            "store": null,
            "used": 579000
          },
          "op": "PUSH32",
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
              "0x0"
            ],
            "store": null,
            "used": 578997
          },
          "op": "PUSH1",
          "pc": 33,
          "sub": null
        },
        {
          "cost": 6,
          "ex": {
            "mem": {
              "data": "0x",
              "off": 0
            },
            "push": [],
            "store": null,
            "used": 578994
          },
          "op": "MSTORE",
          "pc": 35,
          "sub": null
        },
        {
          "cost": 3,
          "ex": {
            "mem": {

… preview truncated; use the full evidence link above.
```

</details>

