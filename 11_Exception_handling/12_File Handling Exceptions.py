try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("The file does not exist!")
except PermissionError:
    print("You don't have permission to open this file!")
finally:
    print("File operation completed.")
