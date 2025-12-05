# Removing duplicates from tuple

# Method 1(Using set() + tuple())
# Input = [
#     ('hi', 'bye'),
#     ('Geeks', 'forGeeks'),
#     ('a', 'b'),
#     ('hi', 'bye'),
#     ('a', 'b')
# ]

test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
res=tuple(set(test_tup))
print(res)

# method 2
x=[]
for i in test_tup:
    if i not in x:
        x.append(i)
print(tuple(x))

# method 3(Using counter())
input = [
    ('hi', 'bye'),
    ('Geeks', 'forGeeks'),
    ('a', 'b'),
    ('hi', 'bye'),
    ('a', 'b')
]
from collections import Counter
rest=tuple(Counter(test_tup).keys())
print(rest)
''''Counter counts how many times each element appears.
It returns a dictionary-like object:
{1: 3, 3: 3, 5: 2, 2: 1}
Keys = unique elements
Values = their counts'''

# method 4(Using OrderedDict)

from collections import OrderedDict
resto=OrderedDict.fromkeys(input).keys()
print(resto)