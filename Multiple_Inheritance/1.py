class C1:
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("m of C1")

class C2:
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("m of C2")

class C3(C1, C2):
    def m(self):
        print("m of C3")

c = C3()

c.c1_m()
c.c2_m()
c.m()
print(C3.__mro__)   # prints the hierarchy of classes related with inheritance when they have names of method in common.