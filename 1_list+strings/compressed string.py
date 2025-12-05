# Compress a string (e.g., "aaabbccc" → "a3b2c3").

name='aaabbcccdddd'
compressed=''
count=1
for i in range(len(name)-1):
    if name[i]==name[i+1]:
        count+=1
    else:
        compressed+=name[i]+str(count)
        count=1
compressed+=name[-1]+str(count) # Add the last character and its count
print(compressed)