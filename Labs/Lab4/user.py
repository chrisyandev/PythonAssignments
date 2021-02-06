from abc import *
from my_enums import *
from transaction_processor import *


class User(ABC):
    """ Represents an abstract base class of users. """

    @abstractmethod
    def __init__(self, name, age, user_type, bank_account):
        """
        :param name: a string
        :param age: an int
        :param user_type: a string
        :param bank_account: a BankAccount object
        """
        self._name = name
        self._age = age
        self._user_type = user_type.lower()
        self._bank_account = bank_account
        self._budget_list = []

    # def view_budgets(self):
    #     pass
    #
    # def view_transactions_by_budget(self):
    #     for budget in self._budgetList:
    #         print(budget)
    #
    # def view_bank_account_details(self):
    #     print(self._bankAccount)

    def initiate_transaction(self):
        """
        Starts a transaction process. Lets the user pick a budget category.
        :return: none
        """
        user_input = None

        while user_input != 5:
            print("In which category do you want to perform a transaction?")
            print("-----------------------")
            print(f"1. {BudgetCategory.ENTERTAINMENT.value.title()}")
            print(f"2. {BudgetCategory.CLOTHING.value.title()}")
            print(f"3. {BudgetCategory.EATING_OUT.value.title()}")
            print(f"4. {BudgetCategory.MISC.value.title()}")
            print("-----------------------")
            print("5. Quit")
            print("6. Print All Transactions")
            string_input = input("Please enter your choice (1-6): ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                budget = self.get_budget(BudgetCategory.ENTERTAINMENT.value)
                if budget is not None:
                    TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 2:
                budget = self.get_budget(BudgetCategory.CLOTHING.value)
                if budget is not None:
                    TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 3:
                budget = self.get_budget(BudgetCategory.EATING_OUT.value)
                if budget is not None:
                    TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 4:
                budget = self.get_budget(BudgetCategory.MISC.value)
                if budget is not None:
                    TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 5:
                pass
            elif user_input == 6:
                print("\nALL TRANSACTIONS")
                print("----------------")
                self._bank_account.print_transactions()
                input("Press ENTER to continue")
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 6: ")

    def get_budget(self, category):
        """
        Retrieves a Budget of a certain category.
        :param category: a string
        :return: a Budget object
        """
        for b in self._budget_list:
            if b.category == category:
                return b
        return None

    @property
    def budget_list(self):
        """
        Gets the whole list of Budgets.
        :return: a list
        """
        return self._budget_list
