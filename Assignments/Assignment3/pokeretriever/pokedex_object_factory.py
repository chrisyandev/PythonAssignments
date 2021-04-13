from abc import *
from .pokedex_object import *


class PokedexObjectFactory(ABC):
    """ Creates different types of PokedexObjects. """
    @abstractmethod
    def create_object(self, json_data, request):
        pass


class PokemonFactory(PokedexObjectFactory):
    def create_object(self, json_data, request):
        """
        Creates a Pokemon object.
        :return: a Pokemon object
        """
        return Pokemon(**json_data, expanded=request.expanded)


class AbilityFactory(PokedexObjectFactory):
    def create_object(self, json_data, request):
        """
        Creates an Ability object.
        :return: an Ability object
        """
        pass


class StatFactory(PokedexObjectFactory):
    def create_object(self, json_data, request):
        """
        Creates a Stat object.
        :return: a Stat object
        """
        return Stat(**json_data)


class MoveFactory(PokedexObjectFactory):
    def create_object(self, json_data, request):
        """
        Creates a Move object.
        :return: a Move object
        """
        pass


class FactoryTypes:
    """ Matches category types to their respective PokedexObjectFactory. """

    factory_types = {
        "pokemon": PokemonFactory,
        "ability": AbilityFactory,
        "stat": StatFactory,
        "move": MoveFactory
    }
