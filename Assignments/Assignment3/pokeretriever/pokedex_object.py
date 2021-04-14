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
        def __init__(self, **kwargs):
            self.name = kwargs["ability"]["name"]
            self.details = None

        def set_details(self):
            response = PokeRetriever.retrieve("ability", [self.name])
            self.details = Ability(**response[0])

        def __str__(self):
            return self.name

    class PokemonMove:
        def __init__(self, **kwargs):
            pass

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expanded = kwargs.get("expanded")
        self.height = kwargs.get("height")
        self.weight = kwargs.get("weight")
        self.types = [t["type"]["name"] for t in kwargs["types"]]

        self.stats = []
        json_stats = kwargs.get("stats")
        for st in json_stats:
            pokemon_stat = self.PokemonStat(**st)
            if self.expanded:
                pokemon_stat.set_details()
            self.stats.append(pokemon_stat)

        self.abilities = []
        json_abilities = kwargs.get("abilities")
        for ab in json_abilities:
            pokemon_ability = self.PokemonAbility(**ab)
            if self.expanded:
                pokemon_ability.set_details()
            self.abilities.append(pokemon_ability)

        # self.moves = []
        # json_moves = kwargs.get("moves")
        # for mo in json_moves:
        #     pokemon_move = self.PokemonMove(**mo)
        #     if self.expanded:
        #         pokemon_move.set_details()
        #     self.moves.append(pokemon_move)

    def __str__(self):
        output = f"Name: {self.name}\n" \
                 f"ID: {self.id}\n" \
                 f"Height: {self.height} decimetres\n" \
                 f"Weight: {self.weight} hectograms\n" \
                 f"Types: {', '.join(self.types)}\n"
        if self.expanded:
            output += f"\nStats:\n------\n"
            for s in self.stats:
                output += str(s.details)
                output += f"Base_Value: {s.base_value}\n\n"

            output += f"\nAbilities:\n------\n"
            for a in self.abilities:
                output += str(a.details) + "\n"

        else:
            output += f"\nStats:\n------\n"
            for s in self.stats:
                output += str(s) + "\n"

            output += f"\nAbilities:\n------\n"
            for a in self.abilities:
                output += str(a) + "\n"

        return output


class Ability(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.generation = kwargs["generation"]["name"]
        effect_en = list(filter(lambda eff: eff["language"]["name"] == "en", kwargs["effect_entries"]))[0]
        self.effect = effect_en["effect"]
        self.effect_short = effect_en["short_effect"]
        self.pokemon = [p["pokemon"]["name"] for p in kwargs["pokemon"]]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n" \
               f"Effect (Short): {self.effect_short}\n" \
               f"Pokemon: {', '.join(self.pokemon)}\n"


class Stat(PokedexObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
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



