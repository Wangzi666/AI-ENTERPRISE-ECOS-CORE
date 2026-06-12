class BillingSystem:
    def __init__(self):
        self.revenue = {}

    def log_usage(self, company, agent, cost):
        if company not in self.revenue:
            self.revenue[company] = 0
        self.revenue[company] += cost
        return self.revenue
