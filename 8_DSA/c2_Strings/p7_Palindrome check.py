def is_palindrome(s):
    s = s.replace(" ","").lower()
    n = len(s)
    left = 0
    right = n - 1
    while left < right :
        if s[left] != s[right] :
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__" :
    s = "madama"
    print(is_palindrome(s))


