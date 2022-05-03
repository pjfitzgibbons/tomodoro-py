from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QRectF, QRect
from PySide6.QtGui import Qt, QImage, QPainter
from PySide6.QtWidgets import QLabel

from datetime import datetime

class PaintedIconWidget(QLabel):
    def __init__(self):
        super(PaintedIconWidget, self).__init__()

        canvas = QtGui.QPixmap(600, 120)
        canvas.fill(Qt.white)
        self.setPixmap(canvas)
        self.draw_something()

    def draw_something(self):
        canvas = self.pixmap()

        self.painter = QtGui.QPainter(canvas)
        self.draw_image_with_scale()
        self.draw_text(datetime.now().strftime('%H:%M:%S'))
        self.painter.end()
        self.setPixmap(canvas)

    def draw_image_with_scale(self):
        image = QImage()
        image.load('assets/Tomatotorrent-256.png')
        target = QRectF(0, 0, 100, 100)
        source = QRectF(0, 0, 256, 256)
        self.painter.setRenderHint(QPainter.SmoothPixmapTransform)
        self.painter.drawImage(target, image, source)

    def draw_text(self, txt):
        font = self.painter.font()
        font.setFamily(font.defaultFamily())
        font.setPixelSize(56)
        self.painter.setFont(font)

        txtRect = QRect(110, 10, 400, 100)
        self.painter.drawText(txtRect, Qt.AlignVCenter, str(txt))
