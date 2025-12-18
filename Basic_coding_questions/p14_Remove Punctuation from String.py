import string

s="Hello!!! How are you??"
res=''
for ch in s:
    if ch not in string.punctuation:
        res+=ch
print(res)