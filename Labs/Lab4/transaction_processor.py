from transaction import Transaction


class TransactionProcessor:
    """ Processes a transaction. """

    @staticmethod
    def process_transaction(budget, bank_account):
        """
        Makes sure both the Budget and BankAccount allows for the Transaction
        to execute before actually executing it.
        """
        amount = float(input("Enter amount: "))
        shop = input("Enter shop/website name: ")

        transaction = Transaction(amount, budget.category, shop)

        if not budget.check_transaction(transaction):
            return False
        elif not bank_account.check_transaction(transaction):
            return False
        else:
            budget.execute_transaction(transaction)
            bank_account.execute_transaction(transaction)
            print("Transaction successful")
            print(transaction)
            return True
