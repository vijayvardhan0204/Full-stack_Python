s = input("enter string:")
print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))


''''Explanation:

any() → returns True if at least one element in the iterable is True.
The expression (c.isalnum() for c in s) is a generator that checks each character one by one.
So:
any(c.isalnum() for c in s) → True if any character is alphanumeric.
any(c.isalpha() for c in s) → True if any character is alphabetic.
any(c.isdigit() for c in s) → True if any character is a digit.
any(c.islower() for c in s) → True if any character is lowercase.
any(c.isupper() for c in s) → True if any character is uppercase.'''