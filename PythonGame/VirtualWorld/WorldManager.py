import pickle
import random
from VirtualWorld.World import World
from Coords import Coords
from SizeError import SizeError



class WorldManager(World):
    def __generateWorld(self):
        self.addOrganism(Coords(0, 0), "Human")
        animalsCounter=random.randint(3,8)
        a=0
        while a<animalsCounter:
            a=a+1
            nrAnim=random.randint(1,6)
            randX=random.randint(1,19)
            randY=random.randint(1,19)
            if nrAnim == 1:
                self.addOrganism(Coords(randX, randY), "Fox")
            if nrAnim == 2:
                self.addOrganism(Coords(randX, randY), "Antelope")
            if nrAnim == 3:
                self.addOrganism(Coords(randX, randY), "Wolf")
            if nrAnim == 4:
                self.addOrganism(Coords(randX, randY), "Sheep")
            if nrAnim == 5:
                self.addOrganism(Coords(randX, randY), "Turtle")
            if nrAnim == 6:
                self.addOrganism(Coords(randX, randY), "Cybersheep")
        b=0
        plantsCounter=random.randint(3,7)
        while b<plantsCounter:
            b=b+1
            nrPlant=random.randint(1,5)
            randX = random.randint(1, 19)
            randY = random.randint(1, 19)
            if nrPlant == 1:
                self.addOrganism(Coords(randX,randY), "Belladonna")
            if nrPlant == 2:
                self.addOrganism(Coords(randX, randY), "Guarana")
            if nrPlant == 3:
                self.addOrganism(Coords(randX, randY), "Grass")
            if nrPlant == 4:
                self.addOrganism(Coords(randX, randY), "SowThistle")
            if nrPlant == 5:
                self.addOrganism(Coords(randX, randY), "Hogweed")


    def executeTurn(self, humanMove):
        for organisms in self.organisms:
            for actual in organisms:
                if actual.isKilled():
                    continue
                if actual.name == "Human":
                    actual.action(humanMove)
                    actual.age += 1
                    continue
                actual.action()
                actual.age += 1
        self.__killOrganisms()
        self.drawWorld()

    def save(self):
        plik=open("save.txt","wb")
        for array in self.organisms:
            for actual in array:
                actual.world=None
        pickle.dump(self.organisms,plik)
        print("Saved")
        for array in self.organisms:
            for actual in array:
                actual.world=self

    def load(self):
        plik=open("save.txt","rb")
        self.organisms=pickle.load(plik)
        for array in self.organisms:
            for actual in array:
                actual.world=self
        print("Loaded")



    def __killOrganisms(self):
        for array in self.organisms:
            for actual in array:
                if actual.isKilled():
                    array.pop(array.index(actual))

    def drawWorld(self):
        self.mainWindow.mainWidget.clearFieldArea()
        for organisms in self.organisms:
            for actual in organisms:
                self.mainWindow.mainWidget.setFieldText(actual.location.x, actual.location.y, actual.name)

    def __init__(self, x, y, window):
        if x<=0 or y<=0:
            raise SizeError('Size Exception')
        World.__init__(self, x, y)
        self.mainWindow= window
        self.mainWindow.worldRef=self
        self.__generateWorld()
