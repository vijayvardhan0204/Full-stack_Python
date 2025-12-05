import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input("enter string:"), int(input("enter width:"))
    result = wrap(string, max_width)
    print(result)

'''abcdefghijklmnopqrstuvwxvyz
4

output:
abcd
efgh
ijkl
mnop
qrst
uvwx
vyz'''