from transaction import Transaction


class TransactionProcessor:
    """ Processes a transaction. """

    @staticmethod
    def process_transaction(budget, bank_account):
        """
        Makes sure both the Budget and BankAccount allows for the Transaction
        to execute before actually executing it.
        """
        amount = None
        while amount is None:
            try:
                amount = float(input("Enter amount: "))
            except ValueError:
                print("Must be a number")
                continue
        shop = input("Enter shop/website name: ")

        transaction = Transaction(amount, budget.category, shop)

        if not bank_account.check_transaction(transaction):
            return False
        elif not budget.check_transaction():
            return False
        else:
            bank_account.execute_transaction(transaction)
            budget.execute_transaction(transaction)
            return True
