# no of words
# Method 1
sentence=input("enter sentence:")
words=sentence.split()
print("no of words:",len(words))

# Method 2
# Count words in a string (without using .split()).
sentence=input("enter sentence:")
count = 0
in_word = False   # flag to track when we’re inside a word
for char in sentence:
    if char!=' ':
        if not in_word:
            count+=1
            in_word=True
        else:
            in_word=False
print("Number of words:", count)        