from VirtualWorld.Organism import Organism
import random


class Plant(Organism):
    def __init__(self,coords,world):
        Organism.__init__(self,coords,world)
        self.strength=0
        self.initiative=0

    def multiply(self):
        newCoords=self.world.freeRandomAround(self.location,1)
        if newCoords==self.location:
            return
        if random.randint(0,10)==0:
            self.world.addOrganism(newCoords,self.name)

    def action(self):
        self.multiply()