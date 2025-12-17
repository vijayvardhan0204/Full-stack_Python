# Count Vowels in a String

s = "python"
count = 0
for ch in s:
    if ch in "aeiouAEIOU":
        count += 1
print(count)
