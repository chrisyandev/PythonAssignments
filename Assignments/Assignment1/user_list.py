from user import User
from budget import Budget
from my_enums import *
from bank_account import BankAccount
from user_factory import UserFactory


class UserList:
    """ Holds the Users registered and controlled by a parent. """

    def __init__(self):
        self._user_list = []

    def register_user(self):
        name = input("Name: ")

        age = None
        while age is None:
            try:
                age = int(input("Age: "))
            except ValueError:
                print("Must be a number")
                continue

        user_type = None
        user_input = None
        while user_input is None:
            print("1. Angel")
            print("2. Troublemaker")
            print("3. Rebel")

            try:
                user_input = int(input("Select a user type (1-3): "))
            except ValueError:
                print("Please enter an integer")
                continue
            else:
                if 1 <= user_input <= 3:
                    user_type = UserType(user_input)
                else:
                    print("Please enter a number from 1-3")
                    user_input = None

        bank_account_number = input("Bank account number: ")
        bank_name = input("Bank name: ")
        bank_balance = None
        while bank_balance is None:
            try:
                bank_balance = float(input("Bank balance: "))
            except ValueError:
                print("Must be a number")
                continue

        bank_account = BankAccount(bank_account_number, bank_name, bank_balance)

        new_user = UserFactory.create_user(name=name, age=age, user_type=user_type, bank_account=bank_account)
        self.__set_up_budgets(new_user)
        self._user_list.append(new_user)

        new_user.show_user_menu()

    @staticmethod
    def __set_up_budgets(user):
        for category in BudgetCategory:
            budget_amount = None
            while budget_amount is None:
                try:
                    budget_amount = float(input(f"Budget for {category.name}: "))
                except ValueError:
                    print("Must be a number")
                    continue
            user.add_budget(Budget(budget_amount, category))

    def delete_user(self, user_id):
        for user in self._user_list:
            if user.id == user_id:
                self._user_list.remove(user)
                return True
        return False

    def get_user_at_index(self, index):
        return self._user_list[index]

    def __len__(self):
        return len(self._user_list)
