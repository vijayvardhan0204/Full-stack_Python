# factors of num
n=int(input("enter number:"))
print(f"factors of {n} are :")
for i in range(1,abs(n)+1):
    if n%i==0:
        print(i)

# prime factors
n=int(input("enter number:"))
n=abs(n)
prime_fact=[]
for i in range(2,n+1):
    if n%i==0:
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            prime_fact.append(i)
print(prime_fact)