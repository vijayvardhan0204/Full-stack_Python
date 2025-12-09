age=int(input("enter age:"))
if age<0:
     raise ValueError("age can't be negative and 0")
else:
     print(f"age is {age}")