try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file...")
