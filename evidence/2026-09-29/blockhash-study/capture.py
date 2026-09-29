"""Bounded, read-only mainnet selector probes; no reorg or orphan-state claims."""

import datetime
import json
from pathlib import Path
import urllib.request


observations = []


def rpc(name, method, params):
    request = {"jsonrpc": "2.0", "id": len(observations) + 1,
               "method": method, "params": params}
    wire = urllib.request.Request(
        "http://127.0.0.1:8545", json.dumps(request).encode(),
        {"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(wire, timeout=30) as response:
        result = json.load(response)
    observations.append({"name": name, "request": request, "response": result})
    return result


rpc("version", "web3_clientVersion", [])
block = rpc("block-one", "eth_getBlockByNumber", ["0x1", False])["result"]
block_hash = block["hash"]
unknown = "0x" + "00" * 32
rpc("block-number", "trace_block", ["0x1"])
rpc("block-hash", "trace_block", [block_hash])
rpc("block-hash-canonical", "trace_block",
    [{"blockHash": block_hash, "requireCanonical": True}])
rpc("block-unknown-hash", "trace_block", [unknown])
rpc("filter-range-reward", "trace_filter",
    [{"fromBlock": "0x1", "toBlock": "0x1", "toAddress": [block["miner"]]}])
rpc("filter-hash-reward", "trace_filter",
    [{"blockHash": block_hash, "toAddress": [block["miner"]], "count": 1}])
rpc("filter-hash-and-range", "trace_filter",
    [{"blockHash": block_hash, "fromBlock": "0x1", "toBlock": "0x1"}])
rpc("filter-hash-count-zero", "trace_filter", [{"blockHash": block_hash, "count": 0}])
rpc("replay-hash", "trace_replayBlockTransactions", [block_hash, ["trace"]])
rpc("logs-known-empty", "eth_getLogs", [{"blockHash": block_hash}])
rpc("logs-unknown-hash", "eth_getLogs", [{"blockHash": unknown}])

output = {"captured_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "scope": "Mainnet canonical block 1; no induced reorg or noncanonical execution test",
          "observations": observations}
Path(__file__).with_name("reth.json").write_text(json.dumps(output, indent=2) + "\n")
for observation in observations:
    response = observation["response"]
    result = response.get("result")
    summary = response.get("error", f"{len(result)} records" if isinstance(result, list) else "ok")
    print(observation["name"], summary)
