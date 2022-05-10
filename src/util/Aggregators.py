from util import EventLog

def appStartedPrint(e):
    print("AppStarted", e)

appStartedAggregator = EventLog.AppStarted.subscribe(on_next=appStartedPrint)