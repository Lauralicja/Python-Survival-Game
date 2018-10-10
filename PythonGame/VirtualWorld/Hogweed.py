from VirtualWorld.Plant import Plant
from Coords import Coords
class Hogweed(Plant):

    def __init__(self,coords,world):
        Plant.__init__(self,coords,world)
        self.name="Hogweed"
        self.strength=10

    def specialCollision(self, other):
        if Coords.around(other):
            if not other.nazwa=="Cybersheep":
                other.kill()
                return 0