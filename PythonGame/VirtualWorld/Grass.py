from VirtualWorld.Plant import Plant


class Grass(Plant):
    def __init__(self, coords, world):
        Plant.__init__(self, coords, world)
        self.name = "Grass"
