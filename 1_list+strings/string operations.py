# string operations

# 1️⃣ Creating Strings
s = "Hello"
s2 = 'Python'
s3 = """Multiline
String"""
print(s, s2, s3)

# 2️⃣ Accessing Characters (Indexing)
s = "Vijay"
print(s[0])     # V
print(s[-1])    # y

# 3️⃣ Slicing
s = "VijayVardhan"
print(s[0:5])    # Vijay
print(s[6:])     # Vardhan
print(s[::-1])   # reverse

# 4️⃣ String Concatenation
a = "Hello"
b = "World"
print(a + b)     # HelloWorld

# 5️⃣ String Repetition
print("Hi" * 3)   # HiHiHi

# 6️⃣ Length of String
s = "Python"
print(len(s))    # 6

# 7️⃣ Membership Operators
s = "Hello Python"
print("Hello" in s)       # True
print("Java" not in s)    # True

# 8️⃣ String Comparison
print("apple" == "apple")   # True
print("a" < "b")            # True (ASCII comparison)

# 9️⃣ Iterating Through a String
for ch in "Vijay":
    print(ch)

# 🔟 Useful String Methods

print("hello".upper())               # HELLO
print("HELLO".lower())               # hello
print("hello world".title())         # Hello World
print("python".capitalize())         # Python
print("   hi  ".strip())             # hi
print("   hi".lstrip())              # hi
print("hi   ".rstrip())              # hi
print("text text".replace("text", "code"))  # code code
print("one two three".split())       # ['one', 'two', 'three']
print("-".join(["a", "b", "c"]))     # a-b-c
print("hello".find("l"))             # 2
print("banana".count("a"))           # 3
print("python".startswith("py"))     # True
print("python".endswith("on"))       # True

# 🔶 EXTRA — String Formatting
name = "Vijay"
print(f"My name is {name}")           # f-string
print("My name is {}".format(name))   # .format()
