# Recurssive palindrome

def is_palindrome(s):
    # Base case: if string is empty or 1 char -> palindrome
    if len(s) <= 1:
        return True
    if s[0] == s[-1]: # Check first and last characters
        # Recursively check remaining substring
        return is_palindrome(s[1:-1])
    else:
        return False
word = input("Enter a word: ")
if is_palindrome(word):
    print("It is a palindrome")
else:
    print("Not a palindrome")
