WALLET_SYSTEM = {}

def create_wallet(company):
    WALLET_SYSTEM[company] = 0
    return WALLET_SYSTEM

def transact(company, amount):
    WALLET_SYSTEM[company] += amount
    return {"company": company, "balance": WALLET_SYSTEM[company]}
