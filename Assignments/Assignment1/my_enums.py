from enum import *


class UserType(Enum):
    """ Possible types of Users. """
    ANGEL = 1
    TROUBLEMAKER = 2
    REBEL = 3


class BudgetCategory(Enum):
    """ Possible Budget categories. """
    ENTERTAINMENT = "entertainment"
    CLOTHING = "clothing"
    EATING_OUT = "eating out"
    MISC = "misc"
