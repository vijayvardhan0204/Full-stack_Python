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
        if not in_word:         # we just entered a new word
            count+=1
            in_word=True
    else:
        in_word=False           # space means we’re outside a word
print("Number of words:", count)        

''''| Char    | Is Space? | in_word Before | in_word After | count | Why                          |
| ------- | --------- | -------------- | ------------- | ----- | ---------------------------- |
| I       | No        | False          | True          | 1     | Start of word → count++      |
| (space) | Yes       | True           | False         | 1     | End of word                  |
| l       | No        | False          | True          | 2     | Start of next word → count++ |
| o       | No        | True           | True          | 2     | Still in same word           |
| v       | No        | True           | True          | 2     | Still in same word           |
| e       | No        | True           | True          | 2     | Still in same word           |
'''