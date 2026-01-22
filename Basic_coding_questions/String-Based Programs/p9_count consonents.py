s = input("Enter string: ")
count = 0
vowels = "aeiouAEIOU"

for ch in s:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonants count:", count)
