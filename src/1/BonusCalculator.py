class SalesRecord:
    def __init__(self, quota: int, commission: int, tax: int):
        self.quota = quota
        self.commission = commission
        self.tax = tax
        self.total_sale = 0

    def calculate_bonus(self):
        bonus = max(self.total_sale - self.quota, 0) * self.commission / 100
        return bonus - (bonus * self.tax) / 100

    def add_sale(self, sale: int):
        self.total_sale += sale

