from my_enums import *
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel
from bank_account import BankAccount
from user_list import UserList


def main():
    """
    Drives the program.
    :return: none
    """
    my_user_list = UserList()
    load_test_users(my_user_list)

    show_main_menu(my_user_list)


def show_main_menu(user_list):
    """ Displayed on program start. """
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
    """ Displays all users and allows for user selection to 'log in'. """
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


def load_test_users(user_list):
    """ Creates dummy objects to be tested. """
    bank_acc_1 = BankAccount("12345", "TD", 1000.0)
    user_1 = Angel("Jane", 14, UserType.ANGEL, bank_acc_1)
    user_1.add_budget(500.0, BudgetCategory.ENTERTAINMENT)
    user_1.add_budget(500.0, BudgetCategory.CLOTHING)
    user_1.add_budget(500.0, BudgetCategory.EATING_OUT)
    user_1.add_budget(500.0, BudgetCategory.MISC)
    user_list.add_user(user_1)

    bank_acc_2 = BankAccount("67890", "RBC", 500.0)
    user_2 = Troublemaker("Bob", 12, UserType.TROUBLEMAKER, bank_acc_2)
    user_2.add_budget(200.0, BudgetCategory.ENTERTAINMENT)
    user_2.add_budget(200.0, BudgetCategory.CLOTHING)
    user_2.add_budget(200.0, BudgetCategory.EATING_OUT)
    user_2.add_budget(200.0, BudgetCategory.MISC)
    user_list.add_user(user_2)

    bank_acc_3 = BankAccount("112233", "CIBC", 500.0)
    user_3 = Rebel("Jack", 13, UserType.REBEL, bank_acc_3)
    user_3.add_budget(50.0, BudgetCategory.ENTERTAINMENT)
    user_3.add_budget(50.0, BudgetCategory.CLOTHING)
    user_3.add_budget(50.0, BudgetCategory.EATING_OUT)
    user_3.add_budget(50.0, BudgetCategory.MISC)
    user_list.add_user(user_3)


if __name__ == "__main__":
    main()

