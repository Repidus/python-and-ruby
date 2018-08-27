input_id = input("Enter the ID: ")
input_pwd = input("Enter the password: ")
real_id = "albert"
real_pwd = "11"

if input_id == real_id and input_pwd == real_pwd:
    print("Welcome!")
else:
    print("Login failed.")