# Sum of elements

# Method 1
tuple=(5,6,7,8,9,10)
count=0
for i in tuple:
    count+=i
print("sum of elements using loop:",count)

# method 2
test=[x for x in tuple]
# test=list(tuple)
s=sum(test)
print("sum of elements using list comprehension and sum():",s)

# method 3
import math
# calculating sum of tuple elements using math.fsum()
res = math.fsum(tuple)
# printing result
print("sum of elements using math: " ,res)