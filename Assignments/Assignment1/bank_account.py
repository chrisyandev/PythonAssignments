class BankAccount:
    """ Represents a bank account that holds available funds of the User. """

    def __init__(self, account_number, bank_name, balance):
        """
        :param account_number: a string
        :param bank_name: a string
        :param balance: a float
        """
        self._account_number = account_number
        self._bank_name = bank_name
        self._balance = balance
        self._transaction_list = []

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

    def __str__(self):
        """
        Formats the BankAccount's attributes.
        :return: a string
        """
        return f"Account number: {self._account_number}\n" \
               f"Bank name: {self._bank_name}\n" \
               f"Balance: ${self._balance : .2f}\n"
