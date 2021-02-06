import datetime


class Transaction:
    """ Represents money spent online or offline. """

    def __init__(self, amount, budget_category, shop):
        """
        :param amount: a float
        :param budget_category: a string
        :param shop: a string
        """
        self._timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        self._amount = amount
        self._budget_category = budget_category.title()
        self._shop = shop

    @property
    def amount(self):
        """
        Gets the amount in dollars.
        :return: a float
        """
        return self._amount

    def __str__(self):
        """
        Formats the Transaction's attributes.
        :return: a string
        """
        return f"You made a transaction at {self._timestamp}\n" \
               f"Amount: ${self._amount : .2f}\n" \
               f"Category: {self._budget_category}\n" \
               f"Shop/Website: {self._shop}\n"
