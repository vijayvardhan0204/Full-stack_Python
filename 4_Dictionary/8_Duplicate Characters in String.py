# Duplicate Characters in String

# Method 1(using collections.Counter)

from collections import Counter
s='vijayvardhan'
d=Counter(s)
res=[c for c,cnt in d.items() if cnt>1]
print(res)
