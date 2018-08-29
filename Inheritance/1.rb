class Class1
    def method1 
        "method1"
    end
end

class Class2 < Class1
    def method2 
        "method2"
    end
end

c1 = Class1.new
c2 = Class2.new

# You can print the class name of the instance the output came from with it.
p c1, c1.method1
p c2, c2.method1
p c2, c2.method2