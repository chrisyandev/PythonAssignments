from enum import *


class UserType(Enum):
    """ Possible types of Users. """
    ANGEL = 1
    TROUBLEMAKER = 2
    REBEL = 3


class BudgetCategory(Enum):
    """ Possible Budget categories. """
    ENTERTAINMENT = 1
    CLOTHING = 2
    EATING_OUT = 3
    MISC = 4
