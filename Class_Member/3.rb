class Cal
    @@_history = []
    def initialize(v1, v2)
        @val1 = v1
        @val2 = v2
    end
    def add()
        @@_history.push("add: #{@val1}+#{@val2}=#{@val1+@val2}")
        return @val1+@val2
    end
    def Cal.history()
        for item in @@_history
            p item
        end
    end
end

c1 = Cal.new(20, 10)
c1.add()
c2 = Cal.new(30, 10)
c2.add()
Cal.history()