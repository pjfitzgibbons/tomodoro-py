from util import EventLog


class Commands:
    @staticmethod
    def ApplicationStart():
        EventLog.AppStarted.on_next("AppStarted")