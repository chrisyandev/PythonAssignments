from item import Item
from enum import *
from abc import *


class StuffedAnimal(Item, ABC):

    class Fabric(Enum):
        LINEN = "linen"
        COTTON = "cotton"
        ACRYLIC = "acrylic"

    class Stuffing(Enum):
        POLYESTER_FIBERFILL = "polyester fiberfill"
        WOOL = "wool"

    class Size(Enum):
        SMALL = "small"
        MEDIUM = "medium"
        LARGE = "large"

    @abstractmethod
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size_str, fabric, stuffing
        """
        self._size = self.Size(kwargs.pop("size_str"))
        self._fabric = kwargs.pop("fabric")
        self._stuffing = kwargs.pop("stuffing")
        super().__init__(**kwargs)


class EasterBunny(StuffedAnimal):

    class Color(Enum):
        WHITE = "white"
        GREY = "grey"
        PINK = "pink"
        BLUE = "blue"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size_str, color_str
        """
        self._color = self.Color(kwargs.pop("color_str"))
        kwargs["fabric"] = self.Fabric.LINEN
        kwargs["stuffing"] = self.Stuffing.POLYESTER_FIBERFILL
        super().__init__(**kwargs)


class DancingSkeleton(StuffedAnimal):

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size_str
        """
        self._has_glow = True
        kwargs["fabric"] = self.Fabric.ACRYLIC
        kwargs["stuffing"] = self.Stuffing.POLYESTER_FIBERFILL
        super().__init__(**kwargs)


class Reindeer(StuffedAnimal):

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, size_str
        """
        self._has_glow = True
        kwargs["fabric"] = self.Fabric.COTTON
        kwargs["stuffing"] = self.Stuffing.WOOL
        super().__init__(**kwargs)
