a=2
b=10
for i in range(2,b+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)