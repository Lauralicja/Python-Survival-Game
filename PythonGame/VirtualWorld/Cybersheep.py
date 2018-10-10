from VirtualWorld.Animal import Animal


class Cybersheep(Animal):
    def __init__(self, coords, world):
        Animal.__init__(self, coords, world)
        self.name = "Cybersheep"
        self.initiative = 4
        self.strength = 4

    def specialCollision(self, other):
        if other.name=="Hogweed":
            other.kill()
        else: return



