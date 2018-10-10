class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return 1
        return 0


    def __repr__(self):
        str = "{0} {1}".format(self.x,self.y)
        return str

    def around(self, other):
        if self.x == other.x - 1 and self.y == other.y:
            return True
        elif self.x == other.x - 1 and self.y == other.y - 1:
            return True
        elif self.x == other.x - 1 and self.y == other.y + 1:
            return True
        elif self.x == other.x and self.y == other.y - 1:
            return True
        elif self.x == other.x and self.y == other.y + 1:
            return True
        elif self.x == other.x + 1 and self.y == other.y + 1:
            return True
        elif self.x == other.x + 1 and self.y == other.y:
            return True
        elif self.x == other.x + 1 and self.y == other.y - 1:
            return True
        else:
            return False