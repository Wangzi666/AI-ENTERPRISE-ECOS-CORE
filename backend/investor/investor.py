INVESTMENT_POOL = {
    "seo_agent": {
        "valuation": 50000,
        "roi": "12%",
        "status": "open"
    },
    "legal_agent": {
        "valuation": 120000,
        "roi": "18%",
        "status": "open"
    }
}

def invest(agent, amount):
    return {
        "status": "investment accepted",
        "agent": agent,
        "amount": amount
    }
