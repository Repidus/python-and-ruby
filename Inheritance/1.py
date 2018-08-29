class Class1(object):
    def method1(self): return("method1")

class Class2(Class1):
    def method2(self): return("method2")

c1 = Class1()
c2 = Class2()

# You can print the class name of the instance the output came from with it.
print(c1, c1.method1())
print(c2, c2.method1())
print(c2, c2.method2())