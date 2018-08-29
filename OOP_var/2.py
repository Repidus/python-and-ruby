class C(object):
    def __init__(self, value):
        self.__val = value
        # Now you can't access this variable directly from outside.
        # It's a "property" from now.
    
    def show(self):
        print(self.__val)

    def getValue(self):
        return self.__val

    def setValue(self, value):
        if isinstance(value, int):
            self.__val = value

c = C(100)
c.show()
c.setValue(200)
print(c.getValue())