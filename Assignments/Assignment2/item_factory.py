from abc import *


class ItemFactory(ABC):

    @abstractmethod
    def create_toy(self):
        pass

    @abstractmethod
    def create_candy(self):
        pass

    @abstractmethod
    def create_stuffed_animal(self):
        pass


class EasterItemFactory(ABC):

    def create_toy(self):
        print("Creating Robot Bunny")

    def create_candy(self):
        print("Creating Creme Eggs")

    def create_stuffed_animal(self):
        print("Creating Easter Bunny")


class HalloweenItemFactory(ABC):

    def create_toy(self):
        print("Creating RC Spider")

    def create_candy(self):
        print("Creating Pumpkin Caramel Toffee")

    def create_stuffed_animal(self):
        print("Creating Dancing Skeleton")


class ChristmasItemFactory(ABC):

    def create_toy(self):
        print("Creating Santa's Workshop")

    def create_candy(self):
        print("Creating Candy Canes")

    def create_stuffed_animal(self):
        print("Creating Reindeer")


class ItemFactoryType:

    __item_factory_types = {
        "easter": EasterItemFactory,
        "halloween": HalloweenItemFactory,
        "christmas": ChristmasItemFactory
    }

    @classmethod
    def get_factory(cls, holiday):
        return cls.__item_factory_types.get(holiday)()
