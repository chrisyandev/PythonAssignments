from abc import *
from my_enums import *
from transaction_processor import *
from budget import Budget


class User(ABC):
    """ Represents an abstract base class of users. """

    # For making each user id unique
    __next_id = 100

    @abstractmethod
    def __init__(self, name, age, user_type, bank_account):
        """
        :param name: a string
        :param age: an int
        :param user_type: a UserType
        :param bank_account: a BankAccount object
        """
        self._name = name
        self._age = age
        self._user_type = user_type
        self._bank_account = bank_account
        self._budget_list = []
        self._id = self.__next_id
        self.__next_id += 1

    def show_user_menu(self):
        user_input = None

        while user_input != 5:
            print("What do you want to do?")
            print("-----------------------")
            print("1. View budgets")
            print("2. Record a transaction")
            print("3. View transactions by budget")
            print("4. View bank account details")
            print("-----------------------")
            print("5. Log out")

            try:
                user_input = int(input("Please enter your choice (1-5): "))
            except ValueError:
                print("Must be an integer")
                continue

            if user_input == 1:
                print("--- All Budgets ---")
                self.print_all_budgets()
                input("Press ENTER to continue")
            elif user_input == 2:
                self.initiate_transaction()
            elif user_input == 3:
                self.view_transactions_by_budget()
            elif user_input == 4:
                print("--- Bank Account Details ---")
                print(self._bank_account)
                print("--- All Transactions ---")
                self._bank_account.print_transactions()
                input("Press ENTER to continue")
            elif user_input == 5:
                pass
            else:
                print("Please enter a number from 1-5")

    def initiate_transaction(self):
        """
        Starts a transaction process. Lets the user pick a budget category.
        :return: none
        """
        user_input = None

        while user_input != 5:
            print("In which category do you want to perform a transaction?")
            print("-----------------------")
            print("1. Entertainment")
            print("2. Clothing")
            print("3. Eating out")
            print("4. Misc")
            print("-----------------------")
            print("5. Quit")

            try:
                user_input = int(input("Please enter your choice (1-5): "))
            except ValueError:
                print("Must be an integer")
                continue

            if user_input == 1:
                budget = self.get_budget(BudgetCategory.ENTERTAINMENT)
                TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 2:
                budget = self.get_budget(BudgetCategory.CLOTHING)
                TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 3:
                budget = self.get_budget(BudgetCategory.EATING_OUT)
                TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 4:
                budget = self.get_budget(BudgetCategory.MISC)
                TransactionProcessor.process_transaction(budget, self._bank_account)
            elif user_input == 5:
                pass
            else:
                print("Please enter a number from 1-5")

    def view_transactions_by_budget(self):
        user_input = None
        while user_input != 5:
            print("View transactions for which category?")
            print("----------------")
            print("1. Entertainment")
            print("2. Clothing")
            print("3. Eating out")
            print("4. Misc")
            print("----------------")
            print("5. Back")

            try:
                user_input = int(input("Please enter your choice (1-5): "))
            except ValueError:
                print("Must be an integer")
                continue

            if user_input == 1:
                self.get_budget(BudgetCategory.ENTERTAINMENT)\
                    .print_all_transactions()
                input("Press ENTER to continue")
            elif user_input == 2:
                self.get_budget(BudgetCategory.CLOTHING)\
                    .print_all_transactions()
                input("Press ENTER to continue")
            elif user_input == 3:
                self.get_budget(BudgetCategory.EATING_OUT)\
                    .print_all_transactions()
                input("Press ENTER to continue")
            elif user_input == 4:
                self.get_budget(BudgetCategory.MISC)\
                    .print_all_transactions()
                input("Press ENTER to continue")
            elif user_input == 5:
                pass
            else:
                print("Please enter a number from 1-5")


    def get_budget(self, category):
        """
        Retrieves a Budget of a certain category.
        :param category: a BudgetCategory
        :return: a Budget object
        """
        for b in self._budget_list:
            if b.category == category:
                return b
        return None

    def get_all_budgets(self):
        return self._budget_list

    def add_budget(self, budget_amount, category):
        self._budget_list.append(Budget(budget_amount, category, self))

    def print_all_budgets(self):
        """
        Prints the whole list of Budgets.
        :return: none
        """
        for budget in self._budget_list:
            print(budget)

    @property
    def id(self):
        """
        Gets the user id.
        :return: an int
        """
        return self._id

    @property
    def name(self):
        """
        Gets the user's name.
        :return: a string
        """
        return self._name

    def __str__(self):
        return f"Name: {self._name}\n" \
               f"Age: {self._age}\n" \
               f"User type: {self._user_type.name}\n"


