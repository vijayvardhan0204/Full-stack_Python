
# Approach 1(Naive)
def areAnagrams(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    # Sort both strings
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Compare sorted strings
    return s1 == s2

if __name__ == "__main__":
    
    s1 = "Maths"
    s2 = "sathm"
    if areAnagrams(s1, s2):
        print("true")
    else:
        print("false")

# Approach 2(Using Hash Map or Dictionary - O(n + m) Time and O(1) Space)

def areAnagrams(s1, s2):
    
    if len(s1) != len(s2):
        return False
    
    # create a hashmap to store
    # character frequencies
    charCount = {}
    
    # count frequency of each 
    # character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
  
    # count frequency of each
    # character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
  
    # check if all frequencies are zero
    for value in charCount.values():
        if value != 0:
            return False
    
    return True

if __name__ == "__main__":
    
    s1 = "vitamin"
    s2 = "minvita"
    if areAnagrams(s1, s2):
        print("true")
    else:
        print("false")