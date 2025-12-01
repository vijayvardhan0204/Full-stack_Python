# Find all substrings of a given string. no of substring = n(n+1)/2

name = "vijayvardhan"
substrings = []  # empty list to store substrings

for i in range(len(name)):  # start index len = 13 so from 0 to 12
    for j in range(i + 1, len(name) + 1):  # end index here from 1 to 13 after 2 - 13 .. 3 - 13....13 - 13
        substrings.append(name[i:j])  # add substring to list

print(substrings)
print("Total substrings:", len(substrings))
