from item import Item
from abc import *
from enum import *


class Toy(Item, ABC):

    @abstractmethod
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, min_age, has_batteries
        """
        self._has_batteries = kwargs.pop("has_batteries")
        self._min_age = kwargs.pop("min_age")
        super().__init__(**kwargs)


class RobotBunny(Toy):

    class Color(Enum):
        ORANGE = "orange"
        BLUE = "blue"
        PINK = "pink"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, min_age, num_sfx, color_str
        """
        self._num_sfx = kwargs.pop("num_sfx")
        self._color = self.Color(kwargs.pop("color_str"))
        kwargs["has_batteries"] = True
        super().__init__(**kwargs)


class RCSpider(Toy):

    class SpiderType(Enum):
        TARANTULA = "tarantula"
        WOLF_SPIDER = "wolf spider"

    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, min_age, speed, jump_height, has_glow, spider_type_str
        """
        self._speed = kwargs.pop("speed")
        self._jump_height = kwargs.pop("jump_height")
        self._has_glow = kwargs.pop("has_glow")
        self._spider_type = self.SpiderType(kwargs.pop("spider_type_str"))
        kwargs["has_batteries"] = True
        super().__init__(**kwargs)


class SantasWorkshop(Toy):
    def __init__(self, **kwargs):
        """
        :param kwargs: product_id, name, desc, quantity, min_age, width, height, num_rooms
        """
        self._width = kwargs.pop("width")
        self._height = kwargs.pop("height")
        self._num_rooms = kwargs.pop("num_rooms")
        kwargs["has_batteries"] = False
        super().__init__(**kwargs)
