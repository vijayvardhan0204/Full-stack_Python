# Reverse of string

# Method 1(slicing)
s = "Vijay"
print(s[::-1])


#  Method 2(Using a loop)
rev=""
for i in s:
    rev=i+rev
print(rev)

# Method 3(Using reversed())
reve = "".join(reversed(s))
print(reve)

# Method 4(recurssive)
def reverse_string(sv):
    if len(sv) == 0:
        return sv
    return reverse_string(sv[1:]) + sv[0]

print(reverse_string("Vijay"))

# Method 5
s = "Vijay"
rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print(rev)
