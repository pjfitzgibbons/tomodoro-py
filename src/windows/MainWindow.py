from datetime import datetime

from PyQt6.QtCore import QFile, QTimer
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtWidgets import QLabel, QMenu, QWidget, QMainWindow
from PyQt6.uic.properties import QtGui

import util.Aggregators
from util.Commands import Commands
from widgets.PaintedIconWidget import PaintedIconWidget
import reactivex as rx

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100, 250, 250)
        self.build()
        #
        # self.timer = QTimer()
        # self.timer.singleShot(1, lambda: print("single timer"))
        # timer =rx.timer(1.0, 1.0)
        # sub1 = timer.subscribe(on_next=lambda x: print("timer sub 1", x, datetime.now().timestamp()))
        # sub2 = timer.subscribe(on_next=lambda x: print("timer sub 2", x, datetime.now().timestamp()))
        # Commands.ApplicationStart()

    def build(self):
        label = QLabel(self)
        label.setText("Right-Click in this window")
        label = QLabel(self)
        label.setText("Hello")
        image = "assets/Tomatotorrent-256.png"
        with open(image):
            world = QLabel(self)
            pixmap = QPixmap(image)
            world.setPixmap(pixmap)
            world.setGeometry(0, 0, 100, 100)
            world.move(25, 40)