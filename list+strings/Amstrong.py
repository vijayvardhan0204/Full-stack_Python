#Armstrong number
""""153 = 1³ + 5³ + 3³ = 153 (Armstrong number)
120 ≠ 1³ + 2³ + 0³ = 9 (Not an Armstrong number)"""
# Method 1
n=int(input('enter a number:'))
num=n
power=len(str(n))
total=0
while n>0:
    t=n%10
    total+=t**power
    n//=10
if total==num:
    print("Armstrong Number")
else:
    print("not an armstrong number")
"""Explanation:
len(str(num)) gives the number of digits.
Each digit is extracted using % 10.
The digit is raised to the power of total digits.
The loop adds all powered digits and checks if the sum equals the original number."""


# Method 2
# String Conversion Method
n=int(input('enter a number:'))
n1=str(n)
power=len(n1)
sum=0
for i in n1:
    sum+=int(i)**power
if sum==n:
    print("Armstrong Number")
else:
    print("not an armstrong number")
""""Converts the number to a string to easily loop over each digit.
Converts each digit back to an integer for calculation.
Uses sum() for a concise and elegant approach."""



# Method 3
# Recursive Method 
n=int(input("enter a num:"))
num=n
power=len(str(n))
def recursive_fact(n):
    if n==0:
        return 0
    else:
        return (n%10)**power+recursive_fact(n//10)
if recursive_fact(n)==num:
    print("Arstrong num")
else:
    print("not armstrong")
""""The function repeatedly extracts digits and adds their powered values.
The recursion ends when n becomes 0."""