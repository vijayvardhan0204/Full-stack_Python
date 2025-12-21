# Print Numbers from 1 to N

def print_num(n):
    if n == 0:
        return
    print_num(n-1)
    print(n)

print_num(5)
