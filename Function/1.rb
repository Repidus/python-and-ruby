def login(id)
    members = ["Albert", "Bethany", "Charles"]
    for member in members
        if member == id
            return true
        end
    end
    return false
end

print("Enter the ID: ")
input_id = gets.chomp()
if login(input_id)
    puts("Welcome, " + input_id + "!")
else
    puts("Who are you?")
end