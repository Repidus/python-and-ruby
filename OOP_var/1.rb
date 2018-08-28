class Cal
    def initialize(v1, v2)
        @val1, @val2 = v1, v2
    end

    def add
        return @val1 + @val2
    end

    def subtract
        return @val1 - @val2
    end

    def getV1
        return @val1
    end

    def setV1(v1)
        if v1.is_a?(Integer)
            @val1 = v1
        end
    end
end

cal1 = Cal.new(10, 10)
p cal1.add
p cal1.subtract

cal1.setV1("one")
p cal1.getV1