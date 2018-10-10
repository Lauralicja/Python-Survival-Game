
from VirtualWorld.Organism import Organism
from Coords import Coords

class Animal(Organism):

    def __init__(self,coords,world):
        Organism.__init__(self,coords,world)
        self.name="zwierze"


    def multiply(self):
        newCoords = self.world.freeRandomAround(self.location,1)
        if newCoords==self.location:
            return
        self.world.addOrganism(newCoords,self.name)

    def action(self):
        self.movePermission=1
        self.move(self.world.randomAround(self.location,1))

    def move(self,newCoords):
        if newCoords==self.location or not self.world.inBoundaries(newCoords):
            return
        if self.world.isEmpty(newCoords):
            self.location=newCoords
            return
        enemy = self.world.findObject(newCoords)
        if not enemy.isKilled():
            Organism.collision(self,self,enemy)
        if not self.isKilled() and self.movePermission:
            self.location=newCoords
        return
