# Method 1(list)
arr = [1,2,3,4,5,5,4,2,2]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print(unique)

# Method 2(string)
word = "programming"
unique = ''.join(dict.fromkeys(word))
print(unique)

# Method 3(string)
name = "VijayVardhan"
result = ''
for i in name:
    if i not in result:
        result += i
print(result)

# Method 4(Using sets)
word=input("enter word:")
a=list(set(word))
print(a)



