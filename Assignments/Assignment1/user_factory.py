from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel

class UserFactory:

    __available_users = {
        1: Angel,
        2: Troublemaker,
        3: Rebel
    }

    @classmethod
    def create_user(cls, **kwargs):
        user_class = cls.__available_users[kwargs['user_type'].value]
        return user_class(**kwargs)
