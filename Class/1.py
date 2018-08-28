class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    
    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2

cal1 = Cal(10, 10)
print(cal1.add())
print(cal1.subtract())

cal2 = Cal(10, 20)
print(cal2.add())
print(cal2.subtract())