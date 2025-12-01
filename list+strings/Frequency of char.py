# Frequency of char
# Method 1
name = input("enter word:")
for i in set(name):
    print(i , name.count(i))
#as sets are unorderd they print unordered output
#to preserve the output use method 2

# Method 2
# To preserve order and remove dulpicates
name = input("enter word:")
for i in dict.fromkeys(name):
    print(i, name.count(i))

'''dict.fromkeys(name)
This creates a dictionary where each unique character in name becomes a key.
print(i, name.count(i))
You are looping through only the keys — meaning each character appears once, in the order it first appeared in the original string.'''