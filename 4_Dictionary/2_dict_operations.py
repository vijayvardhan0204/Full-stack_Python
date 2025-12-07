def sep():
    print("\n" + "-" * 40 + "\n")

# 1. Basic Dictionary
person = {"name": "Vijay", "age": 21}
print("1:", person)
sep()

# 2. Accessing a Value
student = {"name": "Rahul", "marks": 90}
print("2:", student["marks"])
sep()

# 3. Adding a New Key–Value Pair
car = {"brand": "BMW"}
car["color"] = "Black"
print("3:", car)
sep()

# 4. Changing a Value
info = {"city": "Hyderabad"}
info["city"] = "Delhi"
print("4:", info)
sep()

# 5. Deleting a Key–Value Pair
data = {"a": 1, "b": 2}
del data["a"]
print("5:", data)
sep()

# 6. Dictionary with Different Types
details = {
    "name": "Arjun",
    "age": 20,
    "is_student": True,
    "marks": [89, 76, 90]
}
print("6:", details)
sep()

# 7. Empty Dictionary
empty_dict = {}
print("7:", empty_dict)
sep()

# 8. Using get()
student = {"name": "Vijay", "age": 21}
print("8:", student.get("age"))
print("8:", student.get("marks"))   # None
sep()

# 9. Looping through keys
fruits = {"apple": 50, "banana": 20, "orange": 30}
print("9:")
for item in fruits:
    print(" -", item)
sep()

# 10. Looping through values
prices = {"pen": 10, "book": 50}
print("10:")
for value in prices.values():
    print(" -", value)
sep()

# 11. Key–value pairs
employee = {"name": "Ravi", "salary": 40000}
print("11:")
for key, value in employee.items():
    print(key, ":", value)
sep()

# 12. Updating dictionary
info = {"name": "Arun", "age": 22}
info.update({"age": 23, "city": "Mumbai"})
print("12:", info)
sep()

# 13. Nested dictionary
users = {
    "user1": {"name": "Vijay", "age": 21},
    "user2": {"name": "Arjun", "age": 22}
}
print("13:", users["user1"]["name"])
sep()

# 14. List inside dictionary
marks = {"math": [90, 85, 88]}
print("14:", marks["math"][1])
sep()

# 15. Dictionary inside list
students = [
    {"name": "Vijay", "marks": 90},
    {"name": "Karthik", "marks": 85}
]
print("15:", students[1]["marks"])
sep()

# 16. Using dict() function
d = dict(name="Vijay", age=21)
print("16:", d)
sep()

# 17. Check if key exists
person = {"name": "Vijay"}
if "name" in person:
    print("17: Key exists!")
sep()

# 18. Removing last item
data = {"a": 1, "b": 2}
data.popitem()
print("18:", data)
sep()