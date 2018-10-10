class Organism:

    def __init__(self, coords, world):
        self.name=""
        self.killed = 0
        self.movePermission = 1
        self.age = 0
        self.location = coords
        self.world = world
        self.strength=0
        self.initiative=0

    def kill(self):
        self.killed = 1

    def isKilled(self):
        return self.killed

    def action(self):
        return

    def getLocation(self):
        return self.location

    def specialCollision(self,deffender):
        return 1

    def collision(self,attacker,deffender):
        if attacker.name==deffender.name:
            self.multiply()
            attacker.movePermission=0
            return

        if self.specialCollision(deffender)==0 or deffender.specialCollision(self)==0:
            return

        if attacker.strength>=deffender.strength:
            deffender.kill()
            return
        attacker.kill()
        return


    def multiply(self):
        return

