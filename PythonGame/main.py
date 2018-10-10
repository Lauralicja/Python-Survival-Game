from PyQt5.QtWidgets import QApplication
from Display import Window
import sys
from VirtualWorld.WorldManager import WorldManager
from SizeError import SizeError

def main():
    app = QApplication(sys.argv)
    ex = Window(1000, 1000, 20)
    try:
        world = WorldManager(20,20,ex)
    except SizeError:
        print("Wrong size")
        raise
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()