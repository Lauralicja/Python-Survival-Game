from VirtualWorld.Plant import Plant

class Guarana(Plant):

    def __init__(self,coords,world):
        Plant.__init__(self,coords,world)
        self.name="Guarana"

    def specialCollision(self,other):
        other.strength+=3
        return 1