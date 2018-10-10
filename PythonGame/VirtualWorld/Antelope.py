from VirtualWorld.Animal import Animal
import random


class Antelope(Animal):
    def __init__(self, coords, world):
        Animal.__init__(self, coords, world)
        self.name = "Antelope"
        self.initiative = 4
        self.strength = 4

    def action(self):
        self.move(self.world.randomAround(self.location, 2))

    def specialCollision(self, other):
        if random.randint(0, 1):
            newLocation = self.world.freeRandomAround(self.location, 1)
            if newLocation == self.location:
                return 1
        return 0
