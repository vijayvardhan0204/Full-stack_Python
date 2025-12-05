# Count tuples occurrence in list of tuples

# Method 1(List comprehension)
Input = [('hi', 'bye'),('Geeks', 'forGeeks'),('a', 'b'),('hi', 'bye'),('a', 'b')]
check_ele=('a', 'b') 
x=[i for i in Input if i==check_ele] 
print("tuple ('a', 'b') occurs",len(x),"times")

# Method 2(Using lambda function )
y=list(filter(lambda i:(i==check_ele),Input))
print(len(y))

# Method 3(using collections)
import collections
Output=collections.defaultdict(int)
'''defaultdict(int) creates a dictionary
When you access a new key, it automatically starts from 0
(instead of giving KeyError)'''
for i in Input:
    Output[i]+=1
print(Output)

# Method 4(Using only Counter function)
from collections import Counter
z=Counter(Input)
print(z)
print(z[check_ele])

# Method 5(Using countof function)
import operator as op
print(op.countOf(Input,check_ele))

# Method 6(Using set() and count())
unique=set(Input)
out={i:Input.count(i) for i in unique}
print(out)