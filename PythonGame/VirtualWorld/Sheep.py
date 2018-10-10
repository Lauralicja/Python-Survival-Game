

from VirtualWorld.Animal import Animal


class Sheep(Animal):
    def __init__(self, coords, world):
        Animal.__init__(self, coords, world)
        self.name = "Sheep"
        self.inicja = 4
        self.strength = 4
