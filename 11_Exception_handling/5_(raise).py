age=int(input("enter age:"))
if age<0:
     raise ValueError("age can't be negative ")
else:
     print(f"age is {age}")