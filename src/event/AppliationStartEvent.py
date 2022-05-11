from dataclasses import dataclass
from datetime import datetime

from event.BaseEvent import BaseEvent
from models.Synchrony import Synchrony

@dataclass
class ApplicationStartEvent(BaseEvent):
    """

    >>> dt = datetime.fromtimestamp(0.0)
    >>> e = ApplicationStartEvent(startTime = dt)
    >>> e.asSynchronyStream()
    [Synchrony(tableName=None, recordId=None, key='start', value=datetime.datetime(1969, 12, 31, 16, 0))]
    """
    startTime: datetime = None

    def asSynchronyStream(self):
        return [Synchrony(tableName=None, key=Synchrony.Keys.START, value=self.startTime, recordId=None)]