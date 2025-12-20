# Reverse List Without reverse()

lst = [1, 2, 3, 4]
rev = []

for i in lst:
    rev = [i] + rev

print(rev)
