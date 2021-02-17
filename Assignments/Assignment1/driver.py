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
            show_all_users(user_list)
        elif user_input == 3:
            pass
        else:
            print("Please enter a number from 1-3")

def show_all_users(user_list):
    if len(user_list) == 0:
        print("No users")
        input("Press ENTER to go back")
        return

    last_menu_num = len(user_list) + 1
    user_input = None

    while user_input != last_menu_num:
        print("Users")
        print("-----------------------")
        for x in range(len(user_list)):
            print(f"{x + 1}. {user_list.get_user_at_index(x).name}")
        print("-----------------------")
        print(f"{last_menu_num}. Main Menu")

        try:
            user_input = int(
                input(f"Please enter your choice (1-{last_menu_num}): "))
        except ValueError:
            print("Must be an integer")
            continue

        if user_input == last_menu_num:
            pass
        elif 1 <= user_input < last_menu_num:
            user = user_list.get_user_at_index(user_input-1)
            user.show_user_menu()
        else:
            print(f"Please enter a number from 1-{last_menu_num}")


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

