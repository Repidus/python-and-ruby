print("Enter the ID: ")
input_id = gets.chomp()
print("Enter the password: ")
input_pwd = gets.chomp()
real_id = "albert"
real_pwd = "11"

if input_id == real_id and input_pwd == real_pwd
    puts("Welcome!")
else
    puts("Login failed.")
end