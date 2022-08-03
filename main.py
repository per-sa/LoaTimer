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
        self.setGeometry(0, 0, 250, 200)
        self.UiComponents()
        self.show()

    # method for widgets
    def UiComponents(self):

        self.count = 0

        self.flag = False
        self.allow_screenshot = False


        self.label = QLabel(self)
        self.label.setGeometry(60, 100, 250, 100)
        self.label.setStyleSheet("color: #ccff33; background-color: #212529;")
        self.label.setText(str(self.count))
        self.label.setFont(QFont("Arial", 60))

        start = QPushButton("▶️", self)
        start.setGeometry(50, 0, 50, 40)
        start.setStyleSheet("color: #ccff33;")
        start.pressed.connect(self.Start)

        pause = QPushButton("⏸", self)
        pause.setGeometry(100, 0, 50, 40)
        pause.setStyleSheet("color: yellow;")
        pause.pressed.connect(self.Pause)

        reset = QPushButton("❌", self)
        reset.setGeometry(150, 0, 50, 40)
        reset.setStyleSheet("color: red;")
        reset.pressed.connect(self.Reset)

        self.screenshot_btn = QPushButton("Screenshot", self)
        self.screenshot_btn.setGeometry(50, 50, 150, 40)
        
        self.screenshot_btn.setStyleSheet("color: white")

        self.screenshot_btn.pressed.connect(self.ScreenGrab)

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
        self.allow_screenshot = False
        self.screenshot_btn.setStyleSheet("color: white")



    def Pause(self):

        self.flag = False
        self.allow_screenshot = True
        self.screenshot_btn.setStyleSheet("color: white; background-color: green;")


    def Reset(self):

        self.flag = False

        self.count = 0

        self.label.setText(str(self.count))
        self.allow_screenshot = False
        self.screenshot_btn.setStyleSheet("color: white")
        

    def ScreenGrab(self):
        if self.flag == False and self.allow_screenshot == True:
            chars = string.ascii_uppercase + string.digits + string.ascii_uppercase
            name = ''.join(random.choice(chars) for i in range(12))
            screen = QApplication.primaryScreen()
            screenshot = screen.grabWindow(self.winId())
            screenshot.save(f"{name}.png", "png")
        else:
            pass


App = QApplication(sys.argv)
App.setApplicationName("LoA Timer v1.0")
App.setApplicationDisplayName("LoA Timer v1.0")
App.setWindowIcon(QIcon("icon.png"))

window = Window()

sys.exit(App.exec())
