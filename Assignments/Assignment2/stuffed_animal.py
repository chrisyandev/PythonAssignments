from item import Item
from enum import *
from abc import *
from custom_exceptions import *


class StuffedAnimal(Item, ABC):
    """ Represents a stuffed animal item. """

    class Fabric(Enum):
        """ Types of fabric the stuffed animal can be made of. """
        LINEN = "linen"
        COTTON = "cotton"
        ACRYLIC = "acrylic"

    class Stuffing(Enum):
        """ Types of stuffing the stuffed animal can contain. """
        POLYESTER_FIBREFILL = "polyester fibrefill"
        WOOL = "wool"

    class Size(Enum):
        """ Different sizes of the stuffed animal. """
        SMALL = "s"
        MEDIUM = "m"
        LARGE = "l"

    @abstractmethod
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size, fabric, stuffing
        """
        try:
            string = kwargs.pop("size").lower()
            self._size = self.Size(string)
        except ValueError:
            raise InvalidSizeError(string)
        self._fabric = kwargs.pop("fabric")
        self._stuffing = kwargs.pop("stuffing")
        super().__init__(**kwargs)


class EasterBunny(StuffedAnimal):
    """ Represents an Easter stuffed animal. """

    class Colour(Enum):
        """ Different colours the easter bunny can be. """
        WHITE = "white"
        GREY = "grey"
        PINK = "pink"
        BLUE = "blue"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size, colour
        """
        try:
            string = kwargs.pop("colour").lower()
            self._colour = self.Colour(string)
        except ValueError:
            raise InvalidColourError(string)
        kwargs["fabric"] = self.Fabric.LINEN
        kwargs["stuffing"] = self.Stuffing.POLYESTER_FIBREFILL
        super().__init__(**kwargs)


class DancingSkeleton(StuffedAnimal):
    """ Represents a Halloween stuffed animal. """

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size
        """
        self._has_glow = True
        kwargs["fabric"] = self.Fabric.ACRYLIC
        kwargs["stuffing"] = self.Stuffing.POLYESTER_FIBREFILL
        super().__init__(**kwargs)


class Reindeer(StuffedAnimal):
    """ Represents a Christmas stuffed animal. """

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size
        """
        self._has_glow = True
        kwargs["fabric"] = self.Fabric.COTTON
        kwargs["stuffing"] = self.Stuffing.WOOL
        super().__init__(**kwargs)
