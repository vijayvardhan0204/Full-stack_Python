
def longestPalindrome(s):
    if not s:
        return ""

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    longest = ""

    for i in range(len(s)):
        # Odd length palindrome
        p1 = expand(i, i)

         # Even length palindrome
        p2 = expand(i, i + 1)

        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2

    return longest

if __name__ == "__main__":
    s1 = 'abbc'
    s2 = 'bacab'
    print(longestPalindrome(s1))
    print(longestPalindrome(s2))