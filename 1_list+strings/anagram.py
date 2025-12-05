# Anagram
''''An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase, using all the original letters exactly once.'''
# Method 1(simple way)

name1=input("enter 1st word:")
name2=input("enter 2nd word:")
if sorted(name1)==sorted(name2):
    print("2 words are anagrams")
else:
    print("2 words are not anagrams")

# Method 2(to ignore case & spaces)

name1 = input("Enter 1st word: ").replace(" ", "").lower() #replace(" ","") removes spaces
name2 = input("Enter 2nd word: ").replace(" ", "").lower() #lower() converts into lower case

if sorted(name1) == sorted(name2):
    print("2 words are anagrams")
else:
    print("2 words are not anagrams")


# Method 3

from collections import Counter
name1 = input("Enter 1st word: ").replace(" ", "").lower()
name2 = input("Enter 2nd word: ").replace(" ", "").lower()
if Counter(name1) == Counter(name2):
    print("Anagram")
else:
    print("Not anagram")
#Counter automatically counts occurrences of each letter.