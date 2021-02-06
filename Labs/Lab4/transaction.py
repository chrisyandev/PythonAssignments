import datetime


class Transaction:

    def __init__(self, amount, budget_category, shop):
        self._timestamp = datetime.datetime.now()
        self._amount = amount
        self._budget_category = budget_category
        self._shop = shop

    @property
    def amount(self):
        return self._amount
