users = {
    "admin": "1234",
    "sreeja": "python"
}
username = input("Enter your username: ")
password = input("Enter your password: ")

if users[username]== password:
    print("Login successful!")
else:
    print("Invalid username or password.")
