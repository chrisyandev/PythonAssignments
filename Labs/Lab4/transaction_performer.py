from my_enums import *
from transaction import Transaction


class TransactionPerformer:

    @staticmethod
    def perform_transaction(budget, bank_account):
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
            return True
