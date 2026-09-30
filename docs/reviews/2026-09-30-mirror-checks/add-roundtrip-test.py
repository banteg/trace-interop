"""Add the reproduction to an isolated checkout at Nethermind 2cb4e9e."""
from pathlib import Path
import sys

source = Path(sys.argv[1]) / 'src/Nethermind/Nethermind.JsonRpc.TraceStore.Test/TraceSerializerTests.cs'
text = source.read_text()
text = text.replace('using Nethermind.Logging;', 'using Nethermind.Logging;\nusing Nethermind.Core;\nusing Nethermind.Serialization.Json;')
method = '''    [Test]
    public void round_trips_stored_trace_families([Values("trace", "empty-state", "vm", "state")] string family)
    {
        ParityLikeTraceSerializer serializer = new(LimboLogs.Instance);
        ParityLikeTxTrace trace = new()
        {
            Output = [],
            Action = new ParityTraceAction
            {
                Type = "call",
                CallType = "call",
                From = Address.Zero,
                To = Address.Zero,
                Result = new ParityTraceResult { GasUsed = 1, Output = [] },
            },
        };
        if (family == "vm")
        {
            trace.VmTrace = new ParityVmTrace { Code = [0x00], Operations = [] };
        }
        if (family == "empty-state")
        {
            trace.StateChanges = [];
        }
        if (family == "state")
        {
            trace.StateChanges = new Dictionary<Address, ParityAccountStateChange>
            {
                [Address.Zero] = new()
                {
                    Code = new ParityStateChange<byte[]>([0x00], [0x01]),
                },
            };
        }

        byte[] stored = serializer.Serialize([trace]);
        List<ParityLikeTxTrace>? restored = serializer.Deserialize(stored);
        EthereumJsonSerializer json = new();
        Assert.That(json.Serialize(restored), Is.EqualTo(json.Serialize(new[] { trace })));
    }

'''
assert 'round_trips_stored_trace_families' not in text
text = text.replace('    private List<ParityLikeTxTrace>? Deserialize', method + '    private List<ParityLikeTxTrace>? Deserialize')
source.write_text(text)
