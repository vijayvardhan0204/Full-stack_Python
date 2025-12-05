# # Replace 
name = "budhuu is tooooooooo budhuuuuuuu"
new_name = name.replace('budhuuuuuuu' , 'cuteeeee')
print(new_name)

# You can limit replacements using a third parameter:
text = "apple apple apple"
print(text.replace("apple", "orange", 1))

# Method 2
name = "budhuu is tooooooooo budhuuuuuuu"
parts = name.split("budhuuuuuuu")   # split by the word to remove
new_name = "cuteeeee".join(parts)   # join with new word
print(new_name)


''''join() is a string method that takes all the elements of an 
iterable (like a list or tuple of strings) and joins them into one string, 
using the string before .join() as a separator.

✅ Syntax:
separator.join(iterable)

separator → the string you want to insert between each element.
iterable → the collection (like a list or tuple) containing strings.'''