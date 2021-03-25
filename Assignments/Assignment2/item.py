from abc import *


class Item(ABC):

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
        return self._product_id

    @property
    def quantity(self):
        return self._quantity
