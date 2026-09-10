# Login system

username = "admin"
password = "12345"
user = input("Enter username: ")
passcode = input("Enter password: ")
if user == username and passcode == password:
    print("Login successful")
else:
    print("Login failed")
