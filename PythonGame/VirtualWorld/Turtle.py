from VirtualWorld.Animal import Animal
import random

class Turtle(Animal):
    def __init__(self,coords,world):
        Animal.__init__(self,coords,world)
        self.name="Turlte"
        self.initiative=1
        self.strength=2

    def action(self):
        if random.randint(0,4)==0:
            return
        self.move(self.world.randomAround(self.location,1))

    def specialCollision(self,other):
        if other.strength<5:
            other.movePermission=0
            self.movePermission=0
            return 0
        return 1