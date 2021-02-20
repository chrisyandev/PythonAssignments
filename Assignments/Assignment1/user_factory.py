from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel

class UserFactory:
    """ Creates objects that are subtypes of User. """

    # Holds User subclasses that can be instantiated
    __available_users = {
        1: Angel,
        2: Troublemaker,
        3: Rebel
    }

    @classmethod
    def create_user(cls, **kwargs):
        """
        Matches a UserType's value with a key in __available_users.
        The key's corresponding value is the class to make an object of.
        :param kwargs: name, age, user_type, bank_account
        :return: a subtype of User
        """
        user_class = cls.__available_users[kwargs['user_type'].value]
        return user_class(**kwargs)
