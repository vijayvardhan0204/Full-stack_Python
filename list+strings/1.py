# Reverse a string without using slicing.
name = "Vijay"
for i in range(len(name) - 1 ,-1 ,-1):
    print(name[i] , end='')



#Check if a string is palindrome.
name = "Vijay"
if name == name[::-1]:
    print('palindrome')
else :
    print("not palindrome")



# Count vowels and consonants in a string.
vowels = 'AEIOUaeiou'
vow = 0
con = 0
name = "vijayvardhan"
for i in name:
    if i in vowels:
        vow += 1
    else:
        con += 1
print(f"no of vowels in string are {vow} and consonants are {con}")




# Find the frequency of each character in a string.
name = "Vijay"
for i in name:
    print(i , name.count(i))



# Remove all duplicate characters from a string.
name = "VijayVardhan"
result = ''
for i in name:
    if i not in result:
        result += i
print(result)



# Count words in a string (without using .split()).
name = "Uppaloju Vijay vardhan Chary"
count = 1
for i in name:
    if i == " " :
        count += 1
print(f'no of words are {count}')        
 


# Check if two strings are anagrams.
name = "Yashwanth"
name2 = "Kasula"
if sorted(name1) == sorted(name2):
    print("anagram")
else :
    print("not anagram")    



# Find the first non-repeating character in a string.
name = "Yashwanth"
for i in name:
    if name.count(i) == 1:
        print(i)
        break




# Replace all occurrences of a substring.
name = "Yashwanth kasula is kasula cause he's kasula yashwanth "
new_name = name.replace('kasula' , 'goud')
print(new_name)



# Find all substrings of a given string. no of substring = n(n+1)/2
name = 'yashwanth'
for i in range(len(name)): #len = 9 so from 0 to 8
    for j in range(i + 1, len(name) + 1): #here from 1 to 9 after 2 - 9 .. 3 - 9....9 - 9
        print(name[i:j]) #slicing will happend according to range
    



# Print all permutations of a string.
from itertools import permutations

string = "abc"

perms = permutations(string)

for p in perms:
    print("".join(p))


# Longest word in a sentence.
name = 'yashwanth goud kasula'
new = name.split()
print(max(new , key = len))



# Compress a string (e.g., "aaabbccc" → "a3b2c3").
name = "aaabbcccd"
compressed = ""
count = 1

for i in range(len(name) - 1):
    if name[i] == name[i + 1]:
        count += 1
    else:
        compressed += name[i] + str(count)
        count = 1

# Add the last character and its count
compressed += name[-1] + str(count)

print(compressed)



# Implement your own version of .find() and .replace().
name = "Yashwanth kasula is kasula cause he's kasula yashwanth "
find = name.find('kasula')
replace = name.replace('kasula' , 'goud')
print(find)
print(replace)



# Find the longest common prefix among a list of strings.
def longest_common_prefix(strings):
    if not strings:
        return ""
    
    prefix = strings[0]  # assume the first string is the prefix
    for s in strings[1:]:
        # shorten prefix until it matches the beginning of s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix


words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))




# Check if a string is a valid Python identifier.
import keyword

def is_valid_identifier(s):
    return s.isidentifier() and not keyword.iskeyword(s)

print(is_valid_identifier("name"))      # True
print(is_valid_identifier("2name"))     # False
print(is_valid_identifier("for"))       # False (keyword)
print(is_valid_identifier("_value"))    # True



# Decode a string like "3[a2[b]]" → "abbabbabb" (nested repeat pattern).
def decode_string(s):
    stack = []
    current_str = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            # Push current state
            stack.append((current_str, current_num))
            current_str, current_num = "", 0
        elif char == "]":
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str


print(decode_string("3[a2[b]]"))