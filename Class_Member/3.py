class Cal:
    _history = []
    def __init__(self, v1, v2):
        self.val1 = v1
        self.val2 = v2
    def add(self):
        Cal._history.append("add: %d+%d=%d" % (self.val1, self.val2, self.val1+self.val2))
        return self.val1+self.val2
    @classmethod
    def history(cls):
        for item in cls._history:
            print(item)

c1 = Cal(20, 10)
c1.add()
c2 = Cal(30, 10)
c2.add()
Cal.history()