import re

# match keyword matches the pattern only at the beginning of string
print(bool(re.match("Hello", "He hello")))# checks only 1st word
print(bool(re.match('vijay','vijay is cute' )))
print(bool(re.match(r'\d','1 23 abc')))#\d checks only 1st char if its number or not
print(re.match(r'.+', 'hi this is vijay'))
'''.+ means: “match any character at least once”
It will match:
letters → a, b, c …
numbers → 1, 2, 3 …
symbols → @,#,$
spaces → ' '''
print("---------------------------------------------------------------------------------------")

for m in re.finditer(r"\d", "a1b2c3"):
    print(m.group(), m.start())
# finditer Returns an iterator of match objects (useful when you want positions of matches).
print("---------------------------------------------------------------------------------------")

# Searches the entire string and returns the first match found.
print(re.search(r"\d+", "Room 45 is on floor 6"))
#\d+ → matches one or more digits (numbers)
print(re.search(r"\w","@ au is sona"))
print("---------------------------------------------------------------------------------------")

# \w finds numbers,letters,underscore(_)
# findall returns all matches in a list
print(re.findall(r"\w", "a$"))    # Example 1
print(re.findall(r"\w", "7%_"))    # Example 2
print(re.findall(r'.+',"hi this is vijay0024"))
# \s matches spaces
print(re.findall(r"\s", "Hello World"))   # Example 1
print(re.findall(r"\s", "A\tB"))          # Example 2
print("-------------------------------------------------------------------------------------")

# sub Replaces pattern matches with something else.
print(re.sub(r"\d", "*", "A1B2C3"))
print("--------------------------------------------------------------------------------------")

# Splits a string using regex (like str.split() but more powerful).
print(re.split(r"\d+", "abc123def45ghi"))
print("--------------------------------------------------------------------------------------")


# . matches any char except new line
print(re.findall(r".", "A1289g"))     # Example 1
print(re.findall(r".", "@"))     # Example 2
print("------------------------------------------------------------------------------------")
# ^pattern must start with pattern
print(re.findall(r"^Hello", "Hello world"))   # Example 1
print(re.findall(r"^abc", "abcdef"))          # Example 2
print(bool(re.findall(r"^123","23 456 123456 ")))
print("---------------------------------------------------------------------------------------")
# pattern$ must end with pattern
print(re.findall(r"world$", "Hello world"))   # Example 1
print(re.findall(r"123$", "abc123"))          # Example 2
print("------------------------------------------------------------------------------")

#[abc] matches a or b or c
print(re.findall(r"[abc]", "bat"))   # Example 1
print(re.findall(r"[abc]", "cat"))   # Example 2

# a{3} matches if aaa occurs
print(re.findall(r"a{3}", "aaabc"))    # Example 1
print(re.findall(r"a{3}", "bbaaa"))    # Example 2
print(re.match(r'\d{2,4}', '1a2b4c'))
print(re.match(r'\d{1,4}', '23234c'))#match 2 to 4 digits continuously
