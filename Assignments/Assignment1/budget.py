class Budget:
    """
    Represents a limit of how much a User can spend for a certain category.
    """

    def __init__(self, total_amount, category):
        """
        :param total_amount: a float
        :param category: a string
        """
        self._transaction_list = []
        self._total_amount = total_amount
        self._amount_spent = 0
        self._locked = False
        self._category = category.lower()

    # Checks if request can be fulfilled without exceeding budget
    def __will_exceed_budget(self, spending):
        if (spending + self._amount_spent) > self._total_amount:
            return True
        return False

    def check_transaction(self, transaction):
        """
        Checks if transaction is allowed to execute.
        :param transaction: a Transaction
        :return: a boolean
        """
        if self._locked:
            print(f"Category {self._category.title()} is locked")
            return False
        if self.__will_exceed_budget(transaction.amount):
            print(f"Cannot execute transaction because it will "
                  f"exceed your budget for {self._category.title()}")
            return False
        return True

    def execute_transaction(self, transaction):
        """
        Executes a transaction.
        :param transaction: a Transaction
        :return: none
        """
        self._amount_spent += transaction.amount
        self._transaction_list.append(transaction)

    @property
    def category(self):
        """
        Gets the budget category.
        :return: a string
        """
        return self._category
