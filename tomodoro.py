from widgets.PaintedIconWidget import PaintedIconWidget
from windows import SystemTray
from windows.MainWindow import MainWindow

from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget

app = QApplication([])
# app.setQuitOnLastWindowClosed(False)

tray = QSystemTrayIcon()
tray_menu = SystemTray.setup(tray)

window = MainWindow()
window.show()

app.exec()
