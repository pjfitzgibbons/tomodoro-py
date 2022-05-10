import asyncio

from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import QMenu, QSystemTrayIcon
from rumps import rumps


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        menu = QMenu(parent)
        changeicon = menu.addAction("Update")
        exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)
        # exitAction.triggered.connect(QtGui.qApp.quit)
        changeicon.triggered.connect(self.updateIcon)

    def updateIcon(self):
        self.setIcon(QIcon("assets/Tomato-256.png"))


class MacosTrayIcon(rumps.App):
    def __init__(self):
        super(MacosTrayIcon, self).__init__('')
        self.menu = ["Update"]
        self.icon = "assets/Tomatotorrent-256.png"
        self.title = "Tomato!"

    @rumps.clicked("Update")
    def updateicon(self, _):
        print("Awesome title", "amazing subtitle", "hi!!1")
        self.icon = "assets/Tomato-256.png"

