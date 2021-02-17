class Budget:
    """
    Represents a limit of how much a User can spend for a certain category.
    """

    def __init__(self, total_amount, category):
        """
        :param total_amount: a float
        :param category: a BudgetCategory
        """
        self._transaction_list = []
        self._total_amount = total_amount
        self._amount_spent = 0
        self._locked = False
        self._category = category

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
            print(f"Category {self._category.name} is locked")
            return False
        if self.__will_exceed_budget(transaction.amount):
            print(f"Cannot execute transaction because it will "
                  f"exceed your budget for {self._category.name}")
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

    def print_all_transactions(self):
        print(f"--- All transactions for {self._category.name} ---")
        for t in self._transaction_list:
            print(t)

    @property
    def category(self):
        """
        Gets the budget category.
        :return: a string
        """
        return self._category

    def __str__(self):
        """
        Formats the Budget's attributes.
        :return: a string
        """
        return f"Budget for {self._category.name}\n" \
               f"Amount spent: ${self._amount_spent : .2f}\n" \
               f"Amount left: " \
               f"${(self._total_amount - self._amount_spent) : .2f}\n" \
               f"Total amount: ${self._total_amount : .2f}\n" \
               f"Locked: {self._locked}\n"
