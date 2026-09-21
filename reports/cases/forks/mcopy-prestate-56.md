# forks/mcopy-prestate-56

Exact observations; group size is not a correctness vote.

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "debug_traceCall",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x000000000000000000000000000000000000100a"
    },
    "0x38",
    {
      "tracer": "prestateTracer",
      "tracerConfig": {
        "diffMode": true
      }
    }
  ]
}
```

## go-ethereum_trace · Geth/v1.17.6-unstable-6141d1d4-2026-09-21/linux-amd64/go1.26.1

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/geth-final-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f2031a55517f643"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347c881fd969950",
        "nonce": 131
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a876839d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## besu_development · besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f2031a55517f643"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347c881fd969950",
        "nonce": 131
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a876839d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## besu_release · besu/v26.8.1/linux-x86_64/openjdk-java-25

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "nonce": 131
      }
    },
    "pre": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## erigon_development · 3.8.0-dev-c25b8e47

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f2031a55517f643"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347c881fd969950",
        "nonce": 131
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a876839d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## erigon_release · 3.6.1-0c4d9c91

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f2031a55517f643"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347c881fd969950",
        "nonce": 131
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a876839d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## nethermind_development · 2.1.0-unstable+a404c4f0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f2031a55517f643"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347c881fd969950",
        "nonce": 131
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a876839d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## nethermind_release · 1.39.3+28cbe2a0

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f2031a55517f643"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347c881fd969950",
        "nonce": 131
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a876839d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## reth_development · Reth Version: 2.5.2+03cb186c

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "nonce": 131
      }
    },
    "pre": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

## reth_release · Reth Version: 2.6.0+73a3a008

Capture: **result**; scenario eligible: **True**. [Full evidence](../../../evidence/2026-09-21/verified-forks/observations.json).


<details><summary>Response preview</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "result": {
    "post": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "nonce": 131
      }
    },
    "pre": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347eec2d8f29150",
        "nonce": 130
      }
    }
  }
}
```

</details>

