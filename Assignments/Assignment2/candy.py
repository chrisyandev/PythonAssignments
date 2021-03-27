from item import Item
from abc import *
from enum import *
from custom_exceptions import *


class Candy(Item, ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, has_nuts, has_lactose
        """
        self._has_nuts = kwargs.pop("has_nuts")
        self._has_lactose = kwargs.pop("has_lactose")
        super().__init__(**kwargs)


class CremeEggs(Candy):

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, pack_size
        """
        self._pack_size = kwargs.pop("pack_size")
        kwargs["has_nuts"] = True
        kwargs["has_lactose"] = True
        super().__init__(**kwargs)


class PumpkinCaramelToffee(Candy):

    class Variety(Enum):
        SEA_SALT = "sea salt"
        REGULAR = "regular"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, variety
        """
        try:
            string = kwargs.pop("variety").lower()
            self._variety = self.Variety(string)
        except ValueError:
            raise InvalidVarietyError(string)
        kwargs["has_nuts"] = True
        kwargs["has_lactose"] = True
        super().__init__(**kwargs)


class CandyCanes(Candy):

    class Colour(Enum):
        RED = "red"
        GREEN = "green"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, colour
        """
        try:
            string = kwargs.pop("colour").lower()
            self._colour = self.Colour(string)
        except ValueError:
            raise InvalidColourError(string)
        kwargs["has_nuts"] = False
        kwargs["has_lactose"] = False
        super().__init__(**kwargs)
