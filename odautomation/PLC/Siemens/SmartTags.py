from .DataTypes import *

class SmartTags:
    def __init__(self, plcclient):
        self._plcclient = plcclient

    def Int(self, db, start):
        return Int(self._plcclient, db, start)