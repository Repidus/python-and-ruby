def login(id):
    members = ["Albert", "Bethany", "Charles"]
    for member in members:
        if member == id:
            return True
    return False

input_id = input("Enter the ID: ")
if login(input_id):
    print("Welcome, " + input_id + "!")
else:
    print("Who are you?")