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
            return f"{self.name}: {self.base_value}"


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

        self.types = [t["type"]["name"] for t in kwargs["types"]]
        self.abilities = kwargs.get("abilities")
        self.moves = kwargs.get("moves")

        self.expanded = kwargs.get("expanded")

    def __str__(self):
        output = f"Name: {self.name}\n" \
                 f"ID: {self.id}\n" \
                 f"Height: {self.height} decimetres\n" \
                 f"Weight: {self.weight} hectograms\n" \
                 f"Types: {', '.join(self.types)}\n" \
                 f"\nStats:\n------\n"
        if self.expanded:
            for s in self.stats:
                output += str(s.details)
                output += f"Base_Value: {s.base_value}\n\n"
        else:
            for s in self.stats:
                output += str(s) + "\n"
        return output


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
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Is_Battle_Only: {self.is_battle_only}\n"


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



