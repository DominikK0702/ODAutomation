class Int:
    def __init__(self, plcclient, db, start, name=None):
        self._plcclient = plcclient
        self.db = db
        self.start = start
        self.name = name

    def read(self):
        pass

    def write(self, value):
        pass