# A pangram is a sentence that contains every letter of the English alphabet (A–Z) at least once.

s = "the quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for ch in alphabet:
    if ch not in s.lower():
        print("Not Pangram")
        break
else:
    print("Pangram")
