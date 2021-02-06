from enum import *


class UserType(Enum):
    """ Possible types of Users. """
    ANGEL = "angel"
    TROUBLEMAKER = "troublemaker"
    REBEL = "rebel"


class BudgetCategory(Enum):
    """ Possible Budget categories. """
    ENTERTAINMENT = "entertainment"
    CLOTHING = "clothing"
    EATING_OUT = "eating out"
    MISC = "misc"
