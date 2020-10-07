
import sys
import threading
import time

from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor, QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QApplication, QWidget, QLabel

app = None
side = None
label = None
vbox = None

class Game_display(QWidget) :
    def __init__(self) :
        global app, side, label, vbox
        self.width = 1000
        self.height = 600
        self.left = 500
        self.top = 40
        self.image = 'C:/Users/User/Desktop/shrimp cocktail/map1.png'
        self.app = QApplication(sys.argv)
        self.side = QWidget()
        self.label = QLabel()
        self.vbox = QVBoxLayout()
        self.window = QMainWindow()

        app = self.app
        side = self.label
        label = self.vbox
        vbox = self.window
        self.create_map()
    def create_map(self) :
        #self.side.resize(self.width, self.height)
        #self.side.move(self.left, self.top)
        self.side.setGeometry(self.left, self.top, self.width, self.height)
        self.side.setWindowTitle('เรวัตมุดผ้าห่ม')

        pixmap = QPixmap(self.image)
        self.label.setPixmap(pixmap)
        self.vbox.addWidget(self.label)
        self.side.setLayout(self.vbox)
        self.side.resize(pixmap.width(),pixmap.height())
        time.sleep(0.1)


        self.side.show()
        sys.exit(self.app.exec_())

#________________________________________________________________________________________________________________________

class Ground(QWidget) :
    def __init__(self) :
        global app, side, label, vbox
        self.image = 'C:/Users/User/Desktop/shrimp cocktail/type2.png'
        self.app = app
        self.side = side
        self.label = label
        self.vbox = vbox
        self.create_map()
    def create_map(self) :

        pixmap = QPixmap(self.image)
        self.label.setPixmap(pixmap)
        self.vbox.addWidget(self.label)
        self.side.setLayout(self.vbox)
        self.side.resize(pixmap.width(),pixmap.height())

        self.side.show()
        sys.exit(self.app.exec_())



if __name__ == '__main__':
    lock = threading.Lock()
    background = threading.Thread( target = Game_display())
    #ground = threading.Thread( target = Ground())
    background.start()
    #ground.start()
    #background.start()
