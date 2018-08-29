class Cal
    attr_reader :val1
    attr_writer :val1
    # 2 lines above have same meaning as the following:
    # attr_accessor :val1
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

cal1.val1 = 45
p cal1.val1