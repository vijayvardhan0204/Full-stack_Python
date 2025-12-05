'''Regular expressions (regex) in Python are patterns used to match, search, and manipulate text.
They help you check if a string follows a pattern (like email, phone number), extract specific parts, or replace text.

Python provides regex support through the re module.

🔹 Simple Definition

Regular expressions are special sequences of characters that describe a search pattern.

Example:

Pattern "abc" matches the exact string "abc".

Pattern \d+ matches one or more digits (0 to 9).

Pattern [A-Za-z]+ matches letters only.'''




'''✅ 1. re.match()

Matches the pattern only at the beginning of the string.

import re
re.match("Hello", "Hello world")

✔ Works
❌ "world Hello" won't match


✅ 2. re.search()

Searches the entire string and returns the first match found.

re.search(r"\d+", "Room 45 is on floor 6")


Output → first number "45"

✅ 3. re.findall()

Returns all matches in a list.

re.findall(r"\d", "a1b2c3")


Output → ['1', '2', '3']

✅ 4. re.finditer()

Returns an iterator of match objects (useful when you want positions of matches).

for m in re.finditer(r"\d", "a1b2"):
    print(m.group(), m.start())

✅ 5. re.sub()

Replaces pattern matches with something else.

re.sub(r"\d", "*", "A1B2C3")


Output → A*B*C*

✅ 6. re.split()

Splits a string using regex (like str.split() but more powerful).

re.split(r"\d+", "abc123def45ghi")


Output → ['abc', 'def', 'ghi']'''
