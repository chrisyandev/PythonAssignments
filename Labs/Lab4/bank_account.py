class BankAccount:

    __next_account_number = 100000

    def __init__(self, bank_name, balance):
        self._bank_name = bank_name
        self._balance = balance
        self._transaction_list = []
        self._bank_account_number = self.__next_account_number
        self.__next_account_number += 1

    def __not_enough_balance(self, spending):
        if (self._balance - spending) < 0:
            return True
        return False

    def check_transaction(self, transaction):
        if self.__not_enough_balance(transaction.amount):
            print("Your bank balance is not enough to cover this transaction")
            return False
        return True

    def execute_transaction(self, transaction):
        self._balance -= transaction.amount
        self._transaction_list.append(transaction)
