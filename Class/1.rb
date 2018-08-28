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
end

cal1 = Cal.new(10, 10)
p cal1.add
p cal1.subtract

cal2 = Cal.new(10, 20)
p cal2.add
p cal2.subtract