AGENT_MARKETPLACE = {
    "seo_agent": {
        "price": 49,
        "rating": 4.8,
        "installs": 1200
    },
    "legal_agent": {
        "price": 99,
        "rating": 4.9,
        "installs": 800
    },
    "ved_agent": {
        "price": 79,
        "rating": 4.7,
        "installs": 650
    }
}

def buy_agent(agent):
    return {
        "agent": agent,
        "status": "purchased",
        "license": "active"
    }
