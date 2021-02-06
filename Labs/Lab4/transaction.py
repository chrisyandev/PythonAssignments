import datetime


class Transaction:

    def __init__(self, amount, budget_category, shop):
        self._timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self._amount = amount
        self._budget_category = budget_category.title()
        self._shop = shop

    @property
    def amount(self):
        return self._amount

    def __str__(self):
        return f"You made a transaction at {self._timestamp}\n" \
               f"Amount: ${self._amount}\n" \
               f"Category: {self._budget_category}\n" \
               f"Shop/Website: {self._shop}\n"
