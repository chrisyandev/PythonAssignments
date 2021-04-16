from abc import *
from .poke_retriever import *


class PokedexObject(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.id = kwargs["id"]


class Pokemon(PokedexObject):

    class PokemonStat:
        def __init__(self, **kwargs):
            self.name = kwargs["stat"]["name"]
            self.base_value = kwargs["base_stat"]
            self.details = None

        async def set_details(self):
            response = await PokeRetriever.process_requests("stat", [self.name])
            self.details = Stat(**response[0])

        def __str__(self):
            return f"{self.name}: {self.base_value}"

    class PokemonAbility:
        def __init__(self, **kwargs):
            self.name = kwargs["ability"]["name"]
            self.details = None

        async def set_details(self):
            response = await PokeRetriever.process_requests("ability", [self.name])
            self.details = Ability(**response[0])

        def __str__(self):
            return self.name

    class PokemonMove:
        def __init__(self, **kwargs):
            self.name = kwargs["move"]["name"]
            self.level_acquired = kwargs["version_group_details"][0]["level_learned_at"]
            self.details = None

        async def set_details(self):
            response = await PokeRetriever.process_requests("move", [self.name])
            self.details = Move(**response[0])

        def __str__(self):
            return f"Move name: {self.name}, Level acquired: {self.level_acquired}"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expanded = kwargs["expanded"]
        self.height = kwargs["height"]
        self.weight = kwargs["weight"]
        self.types = [t["type"]["name"] for t in kwargs["types"]]
        self.stats = []
        self.abilities = []
        self.moves = []

        json_stats = kwargs["stats"]
        for st in json_stats:
            pokemon_stat = self.PokemonStat(**st)
            self.stats.append(pokemon_stat)

        json_abilities = kwargs["abilities"]
        for ab in json_abilities:
            pokemon_ability = self.PokemonAbility(**ab)
            self.abilities.append(pokemon_ability)

        json_moves = kwargs["moves"]
        for mo in json_moves:
            pokemon_move = self.PokemonMove(**mo)
            self.moves.append(pokemon_move)

    async def add_pokemon_details(self):
        async_coroutines = []
        for st in self.stats:
            async_coroutines.append(st.set_details())
        for ab in self.abilities:
            async_coroutines.append(ab.set_details())
        for mo in self.moves:
            async_coroutines.append(mo.set_details())
        await asyncio.gather(*async_coroutines)

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

            output += f"\nMoves:\n------\n"
            for m in self.moves:
                output += str(m.details) + "\n"

        else:
            output += f"\nStats:\n------\n"
            for s in self.stats:
                output += str(s) + "\n"

            output += f"\nAbilities:\n------\n"
            for a in self.abilities:
                output += str(a) + "\n"

            output += f"\nMoves:\n------\n"
            for m in self.moves:
                output += str(m) + "\n"

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
        self.generation = kwargs["generation"]["name"]
        self.accuracy = kwargs["accuracy"]
        self.pp = kwargs["pp"]
        self.power = kwargs["power"]
        self.type = kwargs["type"]["name"]
        self.damage_class = kwargs["damage_class"]["name"]
        self.effect_short = kwargs["effect_entries"][0]["short_effect"]

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"ID: {self.id}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type}\n" \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect (Short): {self.effect_short}\n"



