class Budget:
    def __init__(self, total_amount, category):
        self._transaction_list = []
        self._total_amount = total_amount
        self._amount_spent = 0
        self._locked = False
        self._category = category.lower()

    def __will_exceed_budget(self, spending):
        if (spending + self._amount_spent) > self._total_amount:
            return True
        return False

    def check_transaction(self, transaction):
        if self._locked:
            print(f"Category {self._category.title()} is locked")
            return False
        if self.__will_exceed_budget(transaction.amount):
            print(f"Cannot execute transaction because it will "
                  f"exceed your budget for {self._category.title()}")
            return False
        return True

    def execute_transaction(self, transaction):
        self._amount_spent += transaction.amount
        self._transaction_list.append(transaction)

    @property
    def category(self):
        return self._category
