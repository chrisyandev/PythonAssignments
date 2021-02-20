from user import User


class Angel(User):
    """ Represents a child that behaves very well. """

    warning_threshold = 0.90
    budget_lock_threshold = None
    account_lock_threshold = None
    warn_once = True
    notify_once = True

    def __init__(self, name, age, user_type, bank_account):
        """
        :param name: a string
        :param age: an int
        :param user_type: a string
        :param bank_account: a BankAccount object
        """
        super().__init__(name, age, user_type, bank_account)
