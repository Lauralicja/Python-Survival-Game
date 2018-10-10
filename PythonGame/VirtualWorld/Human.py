
from VirtualWorld.Animal import Animal
from Coords import Coords


class Human(Animal):
    def __init__(self, coords, world):
        Animal.__init__(self, coords, world)
        self.name = "Human"
        self.specialAbility = 0
        self.specialAbilityCounter = 0
        self.initiative = 4
        self.strength = 5

    def action(self, delta):
        if delta == Coords(0, 0):
            if self.specialAbilityCounter == 0:
                self.specialAbility = 1
                self.specialAbilityCounter += 5
        while self.specialAbilityCounter > 0:
            self.strength=10
            self.move(Coords(self.location.x + delta.x, self.location.y + delta.y))
            self.specialAbilityCounter -= 1
            self.strength -=1

    def specialCollision(self, other):
        if self.specialAbility == 1:
            other.location=self.world.freeRandomAround(self.location, 1)
            other.movePermission = 0
            return 0
        return 1
