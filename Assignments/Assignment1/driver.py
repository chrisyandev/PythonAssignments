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

    while user_input != 5:
        print("Main Menu")
        print("-----------------------")
        print("1. Register new user")
        print("2. Login")
        print("3. Exit")
        print("-----------------------")
        string_input = input("Please enter your choice (1-3): ")

        if string_input == '':
            continue

        user_input = int(string_input)

        if user_input == 1:
            user_list.register_user()
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        else:
            print("Could not process the input. Please enter a"
                  " number from 1 - 3: ")

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

    test_user.budget_list.append(budget_entertainment)
    test_user.budget_list.append(budget_clothing)
    test_user.budget_list.append(budget_eating_out)
    test_user.budget_list.append(budget_misc)

    return test_user


if __name__ == "__main__":
    main()

