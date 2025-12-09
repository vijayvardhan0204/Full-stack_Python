try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
