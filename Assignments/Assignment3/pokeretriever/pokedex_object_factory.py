from abc import *
from .pokedex_object import *
from .error_object import PokedexError


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
        json_obj = kwargs["json_obj"]
        if json_obj is None:
            return PokedexError()

        pokemon = Pokemon(**json_obj)
        if kwargs["expanded"]:
            await pokemon.add_pokemon_details()
        return pokemon


class AbilityFactory(PokedexObjectFactory):
    async def create_object(self, **kwargs):
        """
        Creates an Ability object.
        :return: an Ability object
        """
        json_obj = kwargs["json_obj"]
        if json_obj is None:
            return PokedexError()

        return Ability(**json_obj)


class MoveFactory(PokedexObjectFactory):
    async def create_object(self, **kwargs):
        """
        Creates a Move object.
        :return: a Move object
        """
        json_obj = kwargs["json_obj"]
        if json_obj is None:
            return PokedexError()

        return Move(**json_obj)


class FactoryTypes:
    """ Matches category types to their respective PokedexObjectFactory. """

    factory_types = {
        "pokemon": PokemonFactory,
        "ability": AbilityFactory,
        "move": MoveFactory
    }
