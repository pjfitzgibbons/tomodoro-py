from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRectF
from PySide6.QtGui import Qt, QImage, QPainter
from PySide6.QtWidgets import QMainWindow, QPushButton

from widgets.PaintedIconWidget import PaintedIconWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tomodoro')

        paintedIcon = PaintedIconWidget()
        # self.label = QtWidgets.QLabel()
        # canvas = QtGui.QPixmap(400, 300)
        # canvas.fill(Qt.white)
        # self.label.setPixmap(canvas)
        # self.setCentralWidget(self.label)
        self.setCentralWidget(paintedIcon)
        # self.draw_something()

    def draw_something(self):
        image = QImage()
        image.load('assets/Tomatotorrent-256.png')
        target = QRectF(0, 0, 100, 100)
        source = QRectF(0, 0, 256, 256)

        canvas = self.label.pixmap()

        painter = QtGui.QPainter(canvas)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawImage(target, image, source)
        painter.end()
        self.label.setPixmap(canvas)