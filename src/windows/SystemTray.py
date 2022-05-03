from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu

def setup(tray):
    # Create the icon
    icon = QIcon("assets/Tomatotorrent-256.png")
    tray.setIcon(icon)
    tray.setVisible(True)
    tray.setToolTip("A Tooltip")

    # Create the Tray Menu
    menu = QMenu()

    action = QAction("A Menu Item")
    menu.addAction(action)
    # menu.triggered.connect(self.doMenuItem)

    quit = QAction("Quit")
    menu.addAction(quit)
    tray.setContextMenu(menu)

    return menu
#
# class SystemTray():
#     def __init__(self):
#         tray = QSystemTrayIcon()
#
#
#     def doMenuItem(self):
#         self.showMessage('Tomodoro!', 'The Pampelmousse are Vert!')