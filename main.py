from random import random
import string
import random
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
        )

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 400, 500)
        self.UiComponents()
        self.show()

    # method for widgets
    def UiComponents(self):

        self.count = 0

        self.flag = False

        self.label = QLabel(self)
        self.label.setGeometry(75, 100, 250, 70)
        self.label.setStyleSheet("color: #ccff33;")
        self.label.setText(str(self.count))
        self.label.setFont(QFont("Arial", 25))
        self.label.setAlignment(Qt.AlignCenter)

        start = QPushButton("Start", self)
        start.setGeometry(125, 250, 150, 40)
        start.setStyleSheet("color: #ccff33;")
        start.pressed.connect(self.Start)

        pause = QPushButton("Pause", self)
        pause.setGeometry(125, 300, 150, 40)
        pause.setStyleSheet("color: yellow;")
        pause.pressed.connect(self.Pause)

        reset = QPushButton("Reset", self)
        reset.setGeometry(125, 350, 150, 40)
        reset.setStyleSheet("color: red;")
        reset.pressed.connect(self.Reset)

        screenshot = QPushButton("Screenshot", self)
        screenshot.setGeometry(125, 400, 150, 40)
        screenshot.setStyleSheet("color: white; background-color: green;")
        screenshot.pressed.connect(self.ScreenGrab)

        timer = QTimer(self)

        timer.timeout.connect(self.showTime)

        timer.start(100)

    def showTime(self):

        if self.flag:

            self.count += 1

        text = str(self.count / 10)

        self.label.setText(text)


    def Start(self):

        self.flag = True


    def Pause(self):

        self.flag = False


    def Reset(self):

        self.flag = False

        self.count = 0

        self.label.setText(str(self.count))


    def ScreenGrab(self):
        chars = string.ascii_uppercase + string.digits + string.ascii_uppercase
        name = ''.join(random.choice(chars) for i in range(12))
        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save(f"{name}.png", "png")


App = QApplication(sys.argv)
App.setApplicationName("LoA Timer v1.0")
App.setApplicationDisplayName("LoA Timer v1.0")

window = Window()

sys.exit(App.exec())
