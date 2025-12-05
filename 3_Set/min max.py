# Maximum and Minimum element in a Set 

s1={3,4,1,5,100,990,500}

# Method 1(min() & max())
print("using min max functions:")
print("min element:",min(s1))
print("max element:",max(s1))

# Method 2(sorted())
sorted_s=sorted(s1)
print("using sorted():")
print("min element:",sorted_s[0])
print("max element:",sorted_s[-1])

# Method 3(loops)
min_val=float('inf')
max_val=float('-inf')
for i in s1:
    if i<min_val:
        min_val=i
    if i>max_val:
        max_val=i
print("using loops:")
print("Minimum element:", min_val)
print("Maximum element:", max_val)