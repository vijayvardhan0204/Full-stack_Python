# Left Rotation

lst = list(map(int, input("Enter elements: ").split()))
n = int(input("Rotate by: "))

n = n % len(lst)
rotated = lst[n:] + lst[:n]

print("Left rotated list:", rotated)

# Right Rotation

lst = list(map(int, input("Enter elements: ").split()))
n = int(input("Rotate by: "))

n = n % len(lst)
rotated = lst[-n:] + lst[:-n]

print("Right rotated list:", rotated)
