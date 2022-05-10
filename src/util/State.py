
class State:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(State, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._appStart = False

    def appStart(self):
        self._appStart = True
