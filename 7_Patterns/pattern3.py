n=int(input("enter value:"))
for i in range(1,n+1):
    for j in range(i):
        print(i,end=' ')
    print()

y=int(input("enter value:"))
for i in range(1,n+1):
    for j in range(1,i+1):
         print(j,end=' ')
    print()