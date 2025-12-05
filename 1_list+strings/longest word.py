# longest word

name = input("enter sentence:")
new = name.split()
longest = max(new, key=len)
print("Longest word:", longest)
print("Length:", len(longest))
