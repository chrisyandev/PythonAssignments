from abc import *
from .poke_retriever import *


class PokedexObject(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.id = kwargs.get("id")


class Pokemon(PokedexObject):

    class PokemonStat:
        def __init__(self, **kwargs):
            self.name = kwargs["stat"]["name"]
            self.base_value = kwargs["base_stat"]
            self.details = None

        def set_details(self):
            response = PokeRetriever.retrieve("stat", [self.name])
            self.details = Stat(**response[0])

        def __str__(self):
            return f"PokemonStat -> name: {self.name}, base_value: {self.base_value}, details: {self.details}"


    class PokemonAbility:
        def __init__(self):
            pass

    class PokemonMove:
        def __init__(self):
            pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.height = kwargs.get("height")
        self.weight = kwargs.get("weight")
        self.stats = []
        json_stats = kwargs.get("stats")
        for st in json_stats:
            pokemon_stat = self.PokemonStat(**st)
            if kwargs.get("expanded"):
                pokemon_stat.set_details()
            self.stats.append(pokemon_stat)

        self.types = kwargs.get("types")
        self.abilities = kwargs.get("abilities")
        self.moves = kwargs.get("moves")

        self.expanded = kwargs.get("expanded")

        for s in self.stats:
            print(s)


class Ability(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generation = kwargs.get("generation")
        self.effect = kwargs.get("effect")
        self.effect_short = kwargs.get("effect_short")
        self.pokemon = kwargs.get("pokemon")


class Stat(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs["name"]
        self.id = kwargs["id"]
        self.is_battle_only = kwargs["is_battle_only"]

    def __str__(self):
        return f"Stat -> name: {self.name}, id: {self.id}, is_battle_only: {self.is_battle_only}"


class Move(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generation = kwargs.get("generation")
        self.accuracy = kwargs.get("accuracy")
        self.pp = kwargs.get("pp")
        self.power = kwargs.get("power")
        self.type = kwargs.get("type")
        self.damage_class = kwargs.get("damage_class")
        self.effect_short = kwargs.get("effect_short")



