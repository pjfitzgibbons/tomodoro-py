from dataclasses import dataclass
from datetime import datetime


@dataclass
class BaseEvent:
    aggregateName: str = None
    recordId: float = None
    data: map = lambda: dict()
    timestamp: datetime = datetime.now()

    def asSynchronyStream(self):
        pass

    def asEventLog(self):
        EventLog(**dict(self))
