import random

from Coords import Coords
from VirtualWorld.Human import Human
from VirtualWorld.Antelope import Antelope
from VirtualWorld.Fox import Fox
from VirtualWorld.Sheep import Sheep
from VirtualWorld.Turtle import Turtle
from VirtualWorld.Wolf import Wolf
from VirtualWorld.Belladonna import Belladonna
from VirtualWorld.Grass import Grass
from VirtualWorld.Hogweed import Hogweed
from VirtualWorld.Cybersheep import Cybersheep
from VirtualWorld.Guarana import Guarana
from VirtualWorld.SowThistle import SowThistle

class World():
    species = {"Human":Human, "Cybersheep":Cybersheep, "Antelope":Antelope,"Fox":Fox,"Sheep":Sheep,"Turtle":Turtle,"Wolf":Wolf,"Belladonna":Belladonna,"Grass":Grass,
               "Guarana":Guarana,"Sow Thistle":SowThistle, "Hogweed":Hogweed}

    def __init__(self, x, y):
        self.size = Coords(x, y)
        self.organisms = []
        for i in range(12):
            self.organisms.append([])

    def isEmpty(self, coords):
        for array in self.organisms:
            for organism in array:
                if organism.location == coords:
                    return 0
        return 1

    def inBoundaries(self, coords):
        return 0 <= coords.x < self.size.x and 0 <= coords.y < self.size.y

    def findObject(self, coords):
        for array in self.organisms:
            for organism in array:
                if organism.location == coords:
                    return organism
        return None

    def addOrganism(self, coords, name):
        if (not self.isEmpty(coords)):
            return None
        if not name in self.species:
            return None
        newOrganism = self.species[name](coords,self)
        self.organisms[newOrganism.initiative].append(newOrganism)




    def randomAround(self, center,range):
        triesCounter = 2
        newCoords = Coords(center.x + range*random.randint(-1, 1), center.y + range*random.randint(-1, 1))
        while not self.inBoundaries(newCoords) or newCoords == center:
            if triesCounter==0:
                return center
            newCoords = Coords(center.x + range*random.randint(-1, 1), center.y + range*random.randint(-1, 1))
            triesCounter-=1
        return newCoords

    def freeRandomAround(self, center,range):
        triesCounter = 2
        newCoords = Coords(center.x + range*random.randint(-1, 1), center.y + range*random.randint(-1, 1))
        while not self.inBoundaries(newCoords) or newCoords == center or not self.isEmpty(newCoords):
            if triesCounter==0:
                return center
            newCoords = Coords(center.x + range*random.randint(-1, 1), center.y + range*random.randint(-1, 1))
            triesCounter-=1
        return newCoords
