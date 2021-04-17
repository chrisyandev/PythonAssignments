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
    async def create_object(self, **kwargs):
        """
        Creates an Ability object.
        :return: an Ability object
        """
        return Ability(**kwargs)


class MoveFactory(PokedexObjectFactory):
    async def create_object(self, **kwargs):
        """
        Creates a Move object.
        :return: a Move object
        """
        return Move(**kwargs)


class FactoryTypes:
    """ Matches category types to their respective PokedexObjectFactory. """

    factory_types = {
        "pokemon": PokemonFactory,
        "ability": AbilityFactory,
        "move": MoveFactory
    }
