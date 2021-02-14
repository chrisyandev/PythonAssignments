class BankAccount:
    """ Represents a bank account that holds available funds of the User. """

    # For making each account number unique
    __next_account_number = 100000

    def __init__(self, bank_name, balance):
        """
        :param bank_name: a string
        :param balance: a float
        """
        self._bank_name = bank_name
        self._balance = balance
        self._transaction_list = []
        self._bank_account_number = self.__next_account_number
        self.__next_account_number += 1

    # Checks if there is enough in the bank to fulfill request
    def __not_enough_balance(self, spending):
        if (self._balance - spending) < 0:
            return True
        return False

    def check_transaction(self, transaction):
        """
        Checks if transaction is allowed to execute.
        :param transaction: a Transaction
        :return: a boolean
        """
        if self.__not_enough_balance(transaction.amount):
            print("Your bank balance is not enough to cover this transaction")
            return False
        return True

    def execute_transaction(self, transaction):
        """
        Executes a transaction.
        :param transaction: a Transaction
        :return: none
        """
        self._balance -= transaction.amount
        self._transaction_list.append(transaction)

    def print_transactions(self):
        """
        Prints all transactions made in this account.
        :return: none
        """
        for t in self._transaction_list:
            print(t)
