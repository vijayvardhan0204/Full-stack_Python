def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    maxlength = 0
    for right in range(len(s)):
        ch = s[right]
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        maxlength = max(maxlength,right - left +1)
    return maxlength

if __name__ == "__main__":
    s = 'abcabcbb'
    print(lengthOfLongestSubstring(s))