def reverse(s):
    if s == "":
        return s
    return reverse(s[1:]) + s[0]

print(reverse("python"))
