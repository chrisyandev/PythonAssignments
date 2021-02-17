from user import User
from my_enums import *
from bank_account import BankAccount
from user_factory import UserFactory

class UserList:
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
                    print("Choice not available")
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
        self._user_list.append(new_user)
        print(new_user)
        print(type(new_user))

    def delete_user(self, user_id):
        for user in self._user_list:
            if user.id == user_id:
                self._user_list.remove(user)
                return True
        return False


    @property
    def user_list(self):
        return self._user_list
