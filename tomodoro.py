from datetime import datetime

from PyQt6.QtWidgets import QApplication

from libs.hlc.Timestamp import Timestamp
from windows.MainWindow import MainWindow
from windows.SystemTray import MacosTrayIcon

from util import Commands

print("database start")
#
# data = { 'apple': 123 }
# now = datetime.now()
# ts = now.timestamp()
# id = Timestamp.now()
# evt = EventLog(id=ts, name='ApplicationStart', data=data, timestamp=now)
# from sqlalchemy import select
# with Session(engine) as session:
#     session.add(evt)
#     session.commit()
#     records = select(EventLog)
#     print(records)
#     with session.connection() as conn:
#         for row in conn.execute(records):
#             print(row)

app = QApplication([])
window = MainWindow()
window.show()

Commands.Commands.ApplicationStart()

# MacosTrayIcon/Rumps is a blocking call
tray = MacosTrayIcon()
tray.run()
# no code after this line will be run

