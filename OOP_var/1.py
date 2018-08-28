class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

    def getV1(self):
        return self.v1

    def setV1(self, v1):
        if isinstance(v1, int):
            self.v1 = v1

cal1 = Cal(10, 10)
print(cal1.add())
print(cal1.subtract())

cal1.setV1("one")
print(cal1.getV1())