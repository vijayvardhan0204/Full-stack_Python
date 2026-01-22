s = input("Enter string: ")
s = s.replace(" ", "").lower()

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
