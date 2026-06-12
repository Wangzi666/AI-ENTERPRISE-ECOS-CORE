STREAMS = {
    "ozon": [],
    "wb": [],
    "amazon": [],
    "market_trends": []
}

def push_stream(source, data):
    STREAMS[source].append(data)
    return STREAMS[source]
