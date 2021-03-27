from abc import *
from candy import *
from stuffed_animal import *
from toy import *


class ItemFactory(ABC):
    """ Creates a group of Items for a specific holiday. """

    @abstractmethod
    def create_toy(self, **kwargs):
        """ Creates a Toy. """
        pass

    @abstractmethod
    def create_candy(self, **kwargs):
        """ Creates a Candy. """
        pass

    @abstractmethod
    def create_stuffed_animal(self, **kwargs):
        """ Creates a StuffedAnimal. """
        pass


class EasterItemFactory(ItemFactory):
    """ Creates a group of Items for Easter. """

    @staticmethod
    def create_toy(**kwargs):
        """ Creates a RobotBunny. """
        return RobotBunny(**kwargs)

    @staticmethod
    def create_candy(**kwargs):
        """ Creates a CremeEggs. """
        return CremeEggs(**kwargs)

    @staticmethod
    def create_stuffed_animal(**kwargs):
        """ Creates an EasterBunny. """
        return EasterBunny(**kwargs)


class HalloweenItemFactory(ItemFactory):
    """ Creates a group of Items for Halloween. """

    @staticmethod
    def create_toy(**kwargs):
        """ Creates an RCSpider. """
        return RCSpider(**kwargs)

    @staticmethod
    def create_candy(**kwargs):
        """ Creates a PumpkinCaramelToffee. """
        return PumpkinCaramelToffee(**kwargs)

    @staticmethod
    def create_stuffed_animal(**kwargs):
        """ Creates a Dancing Skeleton. """
        return DancingSkeleton(**kwargs)


class ChristmasItemFactory(ItemFactory):
    """ Creates a group of Items for Christmas. """

    @staticmethod
    def create_toy(**kwargs):
        """ Creates a SantasWorkshop. """
        return SantasWorkshop(**kwargs)

    @staticmethod
    def create_candy(**kwargs):
        """ Creates a CandyCanes. """
        return CandyCanes(**kwargs)

    @staticmethod
    def create_stuffed_animal(**kwargs):
        """ Creates a Reindeer. """
        return Reindeer(**kwargs)


class ItemFactoryMapper:
    """ Maps strings to their respective factory or factory method name. """

    @classmethod
    def get_factory(cls, holiday):
        """ Maps a string to a factory. """
        item_factory_types = {
            "easter": EasterItemFactory,
            "halloween": HalloweenItemFactory,
            "christmas": ChristmasItemFactory
        }
        return item_factory_types[holiday.lower()]()

    @staticmethod
    def get_method(factory, item_type):
        """ Maps a string to a factory's method. """
        item_types = {
            "toy": factory.create_toy,
            "candy": factory.create_candy,
            "stuffedanimal": factory.create_stuffed_animal
        }
        return item_types[item_type.lower()]
