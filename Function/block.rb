5.times() {|i| puts i}
2.times() {puts "2times"}
3.upto(5) {|item| puts item}

arr = [1, 2, 3, 4, 5, 6, 7]

arr.each() {|item| puts(item)}

arr.delete_if() do |item|
    item > 4    # If the last statement is true, deletes the element.
end

puts(arr)