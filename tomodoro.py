from datetime import datetime

import hsc as hsc
from PyQt6.QtWidgets import QApplication, QMessageBox

from libs.hlc.Timestamp import Timestamp
from windows.MainWindow import MainWindow
from windows.SystemTray import MacosTrayIcon

from util import Commands

print("database start")
from util.Database import Session, EventLog, engine

from libs.hlc.hlc import HLC

data = { 'apple': 123 }
now = datetime.now()
ts = now.timestamp()
id = Timestamp.now()
evt = EventLog(id=id, data=data, timestamp=now, epochMillis=ts, version=str(id) )
from sqlalchemy import select
with Session(engine) as session:
    session.add(evt)
    session.commit()
    records = select(EventLog)
    print(records)
    with session.connection() as conn:
        for row in conn.execute(records):
            print(row)

app = QApplication([])
window = MainWindow()
window.show()

Commands.Commands.ApplicationStart()

# MacosTrayIcon/Rumps is a blocking call
tray = MacosTrayIcon()
tray.run()
# no code after this line will be run

