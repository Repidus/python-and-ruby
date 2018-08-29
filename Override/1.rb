class Parent
    def method()
        return "parent"
    end
end

class Child < Parent
    def method()
        return super() + " child"
    end
end

parent = Parent.new
child = Child.new

p parent.method()
p child.method()