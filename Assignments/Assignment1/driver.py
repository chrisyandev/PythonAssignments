from my_enums import *
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel
from bank_account import BankAccount
from budget import Budget
from user_list import UserList


def main():
    """
    Drives the program.
    :return: none
    """
    my_user_list = UserList()
    show_main_menu(my_user_list)

    # user_bob = load_test_user()
    # user_bob.initiate_transaction()


def show_main_menu(user_list):
    user_input = None

    while user_input != 3:
        print("Main Menu")
        print("-----------------------")
        print("1. Register new user")
        print("2. Login")
        print("3. Exit")
        print("-----------------------")

        try:
            user_input = int(input("Please enter your choice (1-3): "))
        except ValueError:
            print("Must be an integer")
            continue

        if user_input == 1:
            user_list.register_user()
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        else:
            print("Please enter a number from 1-3")

def load_test_user():
    """
    Creates dummy objects to be tested.
    :return: a User object
    """
    test_bank_account = BankAccount(12345, "RBC", 500.0)
    test_user = Troublemaker("Bob", 12, "troublemaker", test_bank_account)

    budget_entertainment = Budget(100.0, BudgetCategory.ENTERTAINMENT.value)
    budget_clothing = Budget(100.0, BudgetCategory.CLOTHING.value)
    budget_eating_out = Budget(100.0, BudgetCategory.EATING_OUT.value)
    budget_misc = Budget(100.0, BudgetCategory.MISC.value)

    test_user.add_budget(budget_entertainment)
    test_user.add_budget(budget_clothing)
    test_user.add_budget(budget_eating_out)
    test_user.add_budget(budget_misc)

    return test_user


if __name__ == "__main__":
    main()

