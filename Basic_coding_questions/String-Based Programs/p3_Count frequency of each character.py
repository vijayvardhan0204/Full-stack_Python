s = input("Enter string: ")
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

print(freq)
