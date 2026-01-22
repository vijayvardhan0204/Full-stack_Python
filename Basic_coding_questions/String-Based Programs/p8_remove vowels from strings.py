s = input("Enter string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch not in vowels:
        result += ch

print(result)
