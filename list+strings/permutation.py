# Print all permutations of a string.

from itertools import permutations
string = "abc"
perms = permutations(string)

for p in perms:
    print(" ".join(p))
    

''''itertools.permutations(string) → generates all possible orderings of the characters in the string.

Each permutation is returned as a tuple of characters (e.g., ('a', 'b', 'c')).

"".join(p) → joins the tuple into a string.'''
