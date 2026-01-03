
# Approach 1(Using Frequency Array (Two Traversal) – O(2*n) Time and O(MAX_CHAR ) Space)

MAX_CHAR = 26  

def nonRep(s):
    freq = [0] * MAX_CHAR

    for c in s:
        freq[ord(c) - ord('a')] += 1

    # Find the first character with frequency 1
    for c in s:
        if freq[ord(c) - ord('a')] == 1:
            return c

    return '\$'

s = "vijayvardhan"
print(nonRep(s))

# Approach 2(By Storing Indices (Single Traversal) – O(n) Time and O(MAX_CHAR ) Space)

def nonRep(s):
    MAX_CHAR = 26
    vis = [-1] * MAX_CHAR

    for i in range(len(s)):
        index = ord(s[i]) - ord('a')
        if vis[index] == -1:
            
            # Store the index when character is first seen
            vis[index] = i  
        else:
            
            # Mark character as repeated
            vis[index] = -2  

    idx = len(s)

    # Find the smallest index of the non-repeating characters
    for i in range(MAX_CHAR):
        if vis[i] >= 0 :
            idx = min(idx,vis[i])

    return '\$' if idx == len(s) else s[idx]


s = "aabbccc"
print(nonRep(s))