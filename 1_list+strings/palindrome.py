#Palindrome
# Method 1
name = input("enter a word:")
if name == name[::-1]:
    print('palindrome')
else :
    print("not palindrome")


# Method 2
rev=''
for i in range(len(name)-1,-1,-1):
    rev+=name[i]
if rev==name:
     print('palindrome')
else :
    print("not palindrome")
