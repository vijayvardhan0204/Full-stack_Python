'''A Harshad number = number divisible by sum of its digits
Example: 18 → 1 + 8 = 9, 18 % 9 = 0
'''

num = int(input("Enter number: "))
temp = num
s = 0

while temp > 0:
    s += temp % 10
    temp //= 10

if num % s == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")
