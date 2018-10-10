

from VirtualWorld.Animal import Animal


class Wolf(Animal):
    def __init__(self, coords, world):
        Animal.__init__(self, coords, world)
        self.name = "Wolf"
        self.initiative = 5
        self.strength = 9
