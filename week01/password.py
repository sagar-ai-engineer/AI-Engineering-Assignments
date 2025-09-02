actual_password = "openAI123"
attempts = 3

for i in range(1,4):
    user_input = input("Enter password: ")
    if(user_input == actual_password):
        print("Login successful")
        break
    elif attempts - i == 0:
        print("Account locked")
        break
    
    