from budget_manager import BudgetManager

class Budget:
    """
    Represents a limit of how much a User can spend for a certain category.
    """

    def __init__(self, total_amount, category, user):
        """
        :param total_amount: a float
        :param category: a BudgetCategory
        :param user: a User
        """
        self._transaction_list = []
        self._total_amount = total_amount
        self._amount_spent = 0
        self._locked = False
        self._category = category
        self._budget_manager = BudgetManager(self, user)

    def set_lock(self, do_lock):
        self._locked = do_lock

    def check_transaction(self, transaction):
        """
        Checks if transaction is allowed to execute.
        :param transaction: a Transaction
        :return: a boolean
        """
        if self._locked:
            print(f"Category {self._category.name} is locked")
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
        print("Transaction successful")
        print(transaction)
        self._budget_manager.trigger()

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

    @property
    def amount_spent(self):
        return self._amount_spent

    @property
    def total_amount(self):
        return self._total_amount

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
