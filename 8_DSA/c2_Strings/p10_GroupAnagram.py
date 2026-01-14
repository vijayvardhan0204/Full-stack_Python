def GroupAnagram(s):
    look={}
    for word in s:
        count =[0]* 26
        for c in word:
            count[ord(c)-ord('a')] += 1
        key = tuple(count)
        look.setdefault(key,[]).append(word)
    return list(look.values())

if __name__ == "__main__":
    s = ["eat","tea","tan","ate","nat","bat"]       
    print(GroupAnagram(s))