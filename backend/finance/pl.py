FINANCIALS = {
    "revenue": 0,
    "costs": 0,
    "profit": 0
}

def update_financials(revenue, costs):
    FINANCIALS["revenue"] += revenue
    FINANCIALS["costs"] += costs
    FINANCIALS["profit"] = FINANCIALS["revenue"] - FINANCIALS["costs"]
    return FINANCIALS
