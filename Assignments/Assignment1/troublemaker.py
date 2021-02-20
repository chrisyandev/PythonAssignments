from user import User


class Troublemaker(User):
    """ Represents a child that behaves satisfactorily. """

    warning_threshold = 0.75
    budget_lock_threshold = 1.2
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
