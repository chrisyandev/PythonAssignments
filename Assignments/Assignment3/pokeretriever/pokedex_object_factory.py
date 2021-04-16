from abc import *
from .pokedex_object import *


class PokedexObjectFactory(ABC):
    """ Creates different types of PokedexObjects. """
    @abstractmethod
    def create_object(self, **kwargs):
        pass


class PokemonFactory(PokedexObjectFactory):
    async def create_object(self, **kwargs):
        """
        Creates a Pokemon object.
        :return: a Pokemon object
        """
        pokemon = Pokemon(**kwargs)
        if kwargs["expanded"]:
            await pokemon.add_pokemon_details()
        return pokemon


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
