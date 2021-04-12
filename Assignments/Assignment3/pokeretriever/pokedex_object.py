from abc import *


class PokedexObject(ABC):
    def __init__(self, name, id_):
        self.name = name
        self.id = id_


class Pokemon(PokedexObject):
    def __init__(self, name, id_):
        super().__init__(name, id_)


class Move(PokedexObject):
    def __init__(self, name, id_):
        super().__init__(name, id_)


class Stat(PokedexObject):
    def __init__(self, name, id_):
        super().__init__(name, id_)


class Ability(PokedexObject):
    def __init__(self, name, id_):
        super().__init__(name, id_)