s = input("Enter string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("After removing duplicates:", result)
