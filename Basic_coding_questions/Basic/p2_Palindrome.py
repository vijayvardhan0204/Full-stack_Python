# Palindrome

s="madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")


# Check List is Palindrome
lst = [1, 2, 3, 2, 1]
print("Palindrome" if lst == lst[::-1] else "Not Palindrome")
