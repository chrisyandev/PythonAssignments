from abc import *


class Item(ABC):
    """ Represents an item in a Store. """

    @abstractmethod
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity
        """
        self._product_id = kwargs.pop("product_id")
        self._name = kwargs.pop("name")
        self._desc = kwargs.pop("desc")
        self._quantity = kwargs.pop("quantity")

    @property
    def product_id(self):
        """ Gets the product id. """
        return self._product_id

    @property
    def name(self):
        """ Gets the item name. """
        return self._name

    @property
    def quantity(self):
        """ Gets the quantity. """
        return self._quantity
