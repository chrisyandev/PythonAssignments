from abc import *
from my_enums import *
from transaction_performer import *


class User(ABC):
    @abstractmethod
    def __init__(self, name, age, user_type, bank_account):
        self._name = name
        self._age = age
        self._user_type = user_type.lower()
        self._bank_account = bank_account
        self._budget_list = []

    def view_budgets(self):
        print("View budgets")

    def view_transactions_by_budget(self):
        for budget in self._budgetList:
            print(budget)

    def view_bank_account_details(self):
        print(self._bankAccount)

    def initiate_transaction(self):
        user_input = None

        while user_input != 5:
            print("This transaction belongs to category: ")
            print("-----------------------")
            print(f"1. {BudgetCategory.ENTERTAINMENT.value.title()}")
            print(f"2. {BudgetCategory.CLOTHING.value.title()}")
            print(f"3. {BudgetCategory.EATING_OUT.value.title()}")
            print(f"4. {BudgetCategory.MISC.value.title()}")
            print("5. Quit")
            string_input = input("Please enter your choice (1-5): ")

            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                budget = self.get_budget(BudgetCategory.ENTERTAINMENT.value)
                if budget is not None:
                    TransactionPerformer.perform_transaction(budget, self._bank_account)
            elif user_input == 2:
                budget = self.get_budget(BudgetCategory.CLOTHING.value)
                if budget is not None:
                    TransactionPerformer.perform_transaction(budget, self._bank_account)
            elif user_input == 3:
                budget = self.get_budget(BudgetCategory.EATING_OUT.value)
                if budget is not None:
                    TransactionPerformer.perform_transaction(budget, self._bank_account)
            elif user_input == 4:
                budget = self.get_budget(BudgetCategory.MISC.value)
                if budget is not None:
                    TransactionPerformer.perform_transaction(budget, self._bank_account)
            elif user_input == 5:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 5: ")

    def get_budget(self, category):
        for b in self._budget_list:
            if b.category == category:
                return b
        return None

    @property
    def budget_list(self):
        return self._budget_list
