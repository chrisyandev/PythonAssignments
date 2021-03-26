from item import Item
from enum import *
from abc import *


class StuffedAnimal(Item, ABC):

    class Fabric(Enum):
        LINEN = "linen"
        COTTON = "cotton"
        ACRYLIC = "acrylic"

    class Stuffing(Enum):
        POLYESTER_FIBREFILL = "polyester fibrefill"
        WOOL = "wool"

    class Size(Enum):
        SMALL = "s"
        MEDIUM = "m"
        LARGE = "l"

    @abstractmethod
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size, fabric, stuffing
        """
        self._size = self.Size(kwargs.pop("size").lower())
        self._fabric = kwargs.pop("fabric")
        self._stuffing = kwargs.pop("stuffing")
        super().__init__(**kwargs)


class EasterBunny(StuffedAnimal):

    class Colour(Enum):
        WHITE = "white"
        GREY = "grey"
        PINK = "pink"
        BLUE = "blue"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size, colour
        """
        self._colour = self.Colour(kwargs.pop("colour").lower())
        kwargs["fabric"] = self.Fabric.LINEN
        kwargs["stuffing"] = self.Stuffing.POLYESTER_FIBREFILL
        super().__init__(**kwargs)


class DancingSkeleton(StuffedAnimal):

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size
        """
        self._has_glow = True
        kwargs["fabric"] = self.Fabric.ACRYLIC
        kwargs["stuffing"] = self.Stuffing.POLYESTER_FIBREFILL
        super().__init__(**kwargs)


class Reindeer(StuffedAnimal):

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size
        """
        self._has_glow = True
        kwargs["fabric"] = self.Fabric.COTTON
        kwargs["stuffing"] = self.Stuffing.WOOL
        super().__init__(**kwargs)
