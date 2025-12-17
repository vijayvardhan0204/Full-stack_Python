# GCD

a, b = 12, 18

while b:
    a, b = b, a % b

print(a)
