from my_enums import *
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel
from bank_account import BankAccount
from budget import Budget


def main():
    """
    Drives the program.
    :return: none
    """
    user_bob = load_test_user()
    user_bob.initiate_transaction()


def load_test_user():
    """
    Creates dummy objects to be tested.
    :return: a User object
    """
    test_bank_account = BankAccount("RBC", 500.0)
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

