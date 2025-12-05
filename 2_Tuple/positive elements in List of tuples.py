# find Tuples with positive elements in List of tuples

# method 1(Using list comprehension + all())
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
res=[sub for sub in test_list if all(i>0 for i in sub)]
print(res)

# Method 2(Using filter() + lambda + all())
rest=list(filter(lambda sub :all(i>0 for i in sub),test_list))
print(rest)
''''filter() returns a filter object, not a list.
This filter object is an iterator — meaning it produces values one by one when you loop over it.
That’s why we usually convert it to a list:

res = list(filter(...))'''

# Method 3(using loops)
resto=[]
for i in test_list:
    c=0
    for j in i:
         if (j>0):
                c+=1
    if(c==len(i)):
        resto.append(i)
print(resto)