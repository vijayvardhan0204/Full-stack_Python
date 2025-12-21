# First Repeating Character


s = "programming"

for ch in s:
    if s.count(ch) > 1:
        print(ch)
        break
