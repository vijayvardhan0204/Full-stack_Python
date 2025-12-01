str="interview"
vowels="AEIOUaeiou"
a=[]
for i in str:
    if i not in vowels:
        a.append(i)

print(a)