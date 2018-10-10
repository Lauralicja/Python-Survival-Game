from VirtualWorld.Animal import Animal

class Fox(Animal):
    def __init__(self,coords,world):
        Animal.__init__(self,coords,world)
        self.initiative=7
        self.strength=3
        self.name="Fox"

    def action(self):
        counter=20
        newCoords=self.world.randomAround(self.location,1)
        while not self.world.isEmpty(newCoords) and self.world.findObject(newCoords).strength>self.strength:
            if counter==0:
                return
            newCoords=self.world.randomAround(self.location,1)
            counter-=1
        self.move(newCoords)