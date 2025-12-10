try:
    username = input("Enter username: ")
    if username == "":
        raise ValueError("Username cannot be empty!")

    password = input("Enter password: ")
    if password == "":
        raise ValueError("Password cannot be empty!")

    print("Login successful!")
except ValueError as e:
    print("Error:", e)
