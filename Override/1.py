class Parent:
    def method(self):
        return "parent"
    
class Child(Parent):
    def method(self):
        return super().method() + " child"

parent = Parent()
child = Child()

print(parent.method())
print(child.method())