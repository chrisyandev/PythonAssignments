from user import User


class Rebel(User):
    """ Represents a child that behaves very poorly. """

    warning_threshold = 0.50
    budget_lock_threshold = 1
    account_lock_threshold = 2
    warn_once = False
    notify_once = False

    def __init__(self, name, age, user_type, bank_account):
        """
        :param name: a string
        :param age: an int
        :param user_type: a string
        :param bank_account: a BankAccount object
        """
        super().__init__(name, age, user_type, bank_account)
