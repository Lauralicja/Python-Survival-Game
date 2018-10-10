from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Coords import Coords

class Window(QMainWindow):

    worldRef=None

    def __init__(self, sizex, sizey, size):
        QMainWindow.__init__(self)
        self.setFixedSize(sizex, sizey)
        self.setWindowTitle('Projekt PO')
        self.mainWidget = MainWidget(self, sizex, sizey, size)
        self.setCentralWidget(self.mainWidget)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Down:
            self.worldRef.executeTurn(Coords(0,1))
        if e.key() ==Qt.Key_Up:
            self.worldRef.executeTurn(Coords(0,-1))
        if e.key() ==Qt.Key_Right:
            self.worldRef.executeTurn(Coords(1,0))
        if e.key() ==Qt.Key_Left:
            self.worldRef.executeTurn(Coords(-1,0))
        if e.key()==Qt.Key_Space:
            self.worldRef.executeTurn(Coords(0,0))
        if e.key()==Qt.Key_R:
            self.worldRef.drawWorld()
        if e.key()==Qt.Key_S:
            self.worldRef.save()
        if e.key()==Qt.Key_L:
            self.worldRef.load()


class MainWidget(QWidget):
    def __init__(self, parent, sizex, sizey, size):
        QWidget.__init__(self, parent)
        self.resize(sizex, sizey)
        self.__labelsize=(sizex/size)
        self.size=size
        grid = QGridLayout()
        self.setLayout(grid)
        self.labels = []
        for i in range(size):
            self.labels.append([])
            for j in range(size):
                self.labels[i].append(FieldLabel(self,Coords(i,j)))
                self.labels[i][j].setGeometry(self.__labelsize*i, self.__labelsize*j, self.__labelsize-2, self.__labelsize-2)

    def clearFieldArea(self):
        for i in range(self.size):
            for j in range(self.size):
                self.labels[i][j].setText("")

    def setFieldText(self,x,y,text):
        self.labels[x][y].setText(text)

class FieldLabel(QLabel):
    def __init__(self,parent,coords):
        self.coords=coords
        QLabel.__init__(self,parent)
        self.setStyleSheet("background-color: white; color: black;")

    def contextMenuEvent(self,event):
        self.__menu = QMenu(self)
        names=["Antelope","Fox","Sheep","Turtle","Wolf", "Cybersheep","Belladonna","Grass","Guarana","Sow Thistle", "Hogweed"]
        actions=[]
        for i in range (0,11):
            actions.append(QAction(names[i],self))
            self.__menu.addAction(actions[i])
        actions[0].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[0]))
        actions[1].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[1]))
        actions[2].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[2]))
        actions[3].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[3]))
        actions[4].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[4]))
        actions[5].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[5]))
        actions[6].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[6]))
        actions[7].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[7]))
        actions[8].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords,names[8]))
        actions[9].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords, names[9]))
        actions[10].triggered.connect(lambda: self.parent().parent().worldRef.addOrganism(self.coords, names[10]))
        self.__menu.popup(QCursor.pos())