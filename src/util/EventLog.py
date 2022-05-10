import reactivex as rx

def eventLogRecord(data):
    pass

AppStarted = rx.Subject()
AppStarted.subscribe(eventLogRecord)