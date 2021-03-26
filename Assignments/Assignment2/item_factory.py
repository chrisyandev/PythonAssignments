from abc import *
from candy import *
from stuffed_animal import *
from toy import *


class ItemFactory(ABC):

    @abstractmethod
    def create_toy(self, **kwargs):
        pass

    @abstractmethod
    def create_candy(self, **kwargs):
        pass

    @abstractmethod
    def create_stuffed_animal(self, **kwargs):
        pass


class EasterItemFactory(ABC):

    def create_toy(self, **kwargs):
        print("Creating Robot Bunny")
        return RobotBunny(**kwargs)

    def create_candy(self, **kwargs):
        print("Creating Creme Eggs")
        return CremeEggs(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        print("Creating Easter Bunny")
        return EasterBunny(**kwargs)


class HalloweenItemFactory(ABC):

    def create_toy(self, **kwargs):
        print("Creating RC Spider")
        return RCSpider(**kwargs)

    def create_candy(self, **kwargs):
        print("Creating Pumpkin Caramel Toffee")
        return PumpkinCaramelToffee(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        print("Creating Dancing Skeleton")
        return DancingSkeleton(**kwargs)


class ChristmasItemFactory(ABC):

    def create_toy(self, **kwargs):
        print("Creating Santa's Workshop")
        return SantasWorkshop(**kwargs)

    def create_candy(self, **kwargs):
        print("Creating Candy Canes")
        return CandyCanes(**kwargs)

    def create_stuffed_animal(self, **kwargs):
        print("Creating Reindeer")
        return Reindeer(**kwargs)


class ItemFactoryMapper:

    @classmethod
    def get_factory(cls, holiday):
        item_factory_types = {
            "easter": EasterItemFactory,
            "halloween": HalloweenItemFactory,
            "christmas": ChristmasItemFactory
        }
        return item_factory_types[holiday.lower()]()

    @staticmethod
    def get_method(factory, item_type):
        item_types = {
            "toy": factory.create_toy,
            "candy": factory.create_candy,
            "stuffedanimal": factory.create_stuffed_animal
        }
        return item_types[item_type.lower()]
