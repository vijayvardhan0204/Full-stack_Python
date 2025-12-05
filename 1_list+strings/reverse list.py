# Reverse
# Method 1(Reverse method)
a = [1, 2, 3, 4, 5]
# Reverse the list in-place
a.reverse()
print(a)

# Method 2 (Using a Loop)
a = [1, 2, 3, 4, 5]
# Initialize an empty list to store reversed element
res = []
# Loop through each item and insert
# it at the beginning of new list
for val in a:
    res.insert(0, val)
print(res)

# Method 3 (Slicing)
a = [1, 2, 3, 4, 5]
# Create a new list that is a reversed list
# of 'a' using slicing
rev = a[::-1]
print(rev)

# Method 4(List Comprehension)
a=[1,2,3,4,5]
rev=[a[i] for i in range(len(a)-1,-1,-1)]
print(rev)

a = [1, 2, 3, 4, 5]
# Use reversed() to create an iterator
# and convert it back to a list
rev = list(reversed(a))
print(rev)