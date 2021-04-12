from abc import *


class PokedexObject(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.id = kwargs.get("id")


class Pokemon(PokedexObject):

    class PokemonStat:
        def __init__(self):
            pass

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
        # for stat_dict in json_stats:
        #     self.stats.append(Stat(stat_dict))

        self.types = kwargs.get("types")
        self.abilities = kwargs.get("abilities")
        self.moves = kwargs.get("moves")

        self.expanded = kwargs.get("expanded")


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
        self.is_battle_only = kwargs.get("is_battle_only")


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



