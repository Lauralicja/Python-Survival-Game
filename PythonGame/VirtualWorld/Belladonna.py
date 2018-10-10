
from VirtualWorld.Plant import Plant

class Belladonna(Plant):

    def __init__(self,coords,world):
        Plant.__init__(self,coords,world)
        self.name="Belladonna"
        self.strength=99

    def specialCollision(self,other):
        other.kill()
        self.kill()
        return 0
