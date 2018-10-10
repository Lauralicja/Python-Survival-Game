

from VirtualWorld.Plant import Plant

class SowThistle(Plant):
    def __init__(self,coords,world):
        Plant.__init__(self,coords,world)
        self.name="Sow Thistle"

    def action(self):
        self.multiply()
        self.multiply()
        self.multiply()
