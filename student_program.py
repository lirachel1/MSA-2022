import math

new_account = input("Do you want to create a new password or login? ")

user_name = input("Username: ")
password = input("Password: ")

while True: 
    if len(user_name)  16 or len(user_name) >= 4:
        print(f"Valid username, thank you {user_name}.")
        break
    else:
        print("Username must be between 4-16 characters.")
        break
  
while True:
    if len(password) <= 12 or len(password) >= 6:
        print(f"Valid password, thank you {user_name}.")
        break
    else:
        print("Password must be between 6-12 characters.")
        break
