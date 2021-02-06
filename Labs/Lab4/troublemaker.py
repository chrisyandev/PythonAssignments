from user import User


class Troublemaker(User):

    def __init__(self, name, age, user_type, bank_account):
        super().__init__(name, age, user_type, bank_account)
