from user import User


class Rebel(User):

    def __init__(self, name, age, user_type, bank_account):
        super().__init__(name, age, user_type, bank_account)