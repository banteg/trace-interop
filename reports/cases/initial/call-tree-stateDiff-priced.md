# initial/call-tree-stateDiff-priced

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x112b446d0b4e9"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34642dd61bc3496"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x112b446d0b4e9"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34642dd61bc3496"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x112b446d0b4e9"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **change_needed** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.
- H10: **matches** — Successful creation uses address, code and gasUsed.
- H09: **matches** — Failed frames have an explicit result; REVERT preserves return bytes and measured gas.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x112b446d0b4e9"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [
      {
        "action": {
          "callType": "call",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x8d5b8",
          "input": "0x",

… preview truncated; use the full evidence link above.
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **change_needed** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- `output`: None is not of type 'string'

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": null,
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x112b446d0b4e9"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34642dd61bc3496"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **change_needed** — Output remains a byte string under every trace selection.

Draft result schema: **invalid**.
- `output`: None is not of type 'string'

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": null,
    "stateDiff": {
      "0x0000000000000000000000000000000000000000": {
        "balance": {
          "*": {
            "from": "0x66863b",
            "to": "0x112b446d0b4e9"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": {
          "*": {
            "from": "0xc097ce7bc90715b34755ccb0391096",
            "to": "0xc097ce7bc90715b34642dd61bc3496"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-initial/observations.json).

- H08: **matches** — Unrequested trace is an empty array.
- H08: **matches** — Unrequested vmTrace is null.
- H08: **matches** — Output remains a byte string under every trace selection.

Draft result schema: **valid**.

<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "output": "0xffee",
    "stateDiff": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "=",
        "code": "=",
        "nonce": {
          "*": {
            "from": "0x85",
            "to": "0x86"
          }
        },
        "storage": {}
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0": {
        "balance": {
          "*": {
            "from": "0x3b9ac9f2",
            "to": "0x3b9ac9f1"
          }
        },
        "code": "=",
        "nonce": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "storage": {
          "0x0000000000000000000000000000000000000000000000000000000000000000": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000e",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000f"
            }
          },
          "0xe8e77626586f73b955364c7b4bbf0bb7f7685ebd40e852b164633a4acbd3244c": {
            "*": {
              "from": "0x000000000000000000000000000000000000000000000000000000000000000d",
              "to": "0x000000000000000000000000000000000000000000000000000000000000000e"
            }
          }
        }
      },
      "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d1": {
        "balance": {
          "*": {
            "from": "0xe",
            "to": "0xf"
          }
        },
        "code": "=",
        "nonce": "=",
        "storage": {}
      }
    },
    "trace": [],
    "vmTrace": null
  }
}
```

</details>

