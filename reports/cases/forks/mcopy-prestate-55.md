# forks/mcopy-prestate-55

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
    "0x37",
    {
      "tracer": "prestateTracer",
      "tracerConfig": {
        "diffMode": true
      }
    }
  ]
}
```

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
        "balance": "0xc4f2424ca6582b63d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b343b5112a3e9958",
        "nonce": 128
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a8742bfd"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "nonce": 128
      }
    },
    "pre": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "balance": "0xc4f2424ca6582b63d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b343b5112a3e9958",
        "nonce": 128
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a8742bfd"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "balance": "0xc4f2424ca6582b63d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b343b5112a3e9958",
        "nonce": 128
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a8742bfd"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "balance": "0xc4f2424ca6582b63d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b343b5112a3e9958",
        "nonce": 128
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a8742bfd"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "balance": "0xc4f2424ca6582b63d"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b343b5112a3e9958",
        "nonce": 128
      }
    },
    "pre": {
      "0x0000000000000000000000000000000000000000": {
        "balance": "0xc4f200cb8a8742bfd"
      },
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "nonce": 128
      }
    },
    "pre": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
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
        "nonce": 128
      }
    },
    "pre": {
      "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f": {
        "balance": "0xc097ce7bc90715b347f875eff99958",
        "nonce": 127
      }
    }
  }
}
```

</details>

