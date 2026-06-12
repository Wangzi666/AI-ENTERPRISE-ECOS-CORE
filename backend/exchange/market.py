AI_STOCK_EXCHANGE = {
    "AI_ENTERPRISE_OS": {"valuation": 1200000, "growth": 0.32},
    "client_companies": {}
}

def ipo(company):
    AI_STOCK_EXCHANGE["client_companies"][company] = {
        "valuation": 100000,
        "status": "listed"
    }
    return AI_STOCK_EXCHANGE
