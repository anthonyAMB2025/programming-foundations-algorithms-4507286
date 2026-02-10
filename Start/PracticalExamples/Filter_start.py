# Example file for Programming Foundations: Algorithms by Joe Marini
# use a set to count unique items


# define a set of items that we want to reduce duplicates
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a set to perform a filter
itemSet = set(items)
print(itemSet)
# TODO: loop over each item and add to the set


# TODO: Count the unique letters in a sentence
sentence = "The quick brown fox jumps over the lazy dog."
print((set(sentence))) #good but inlcludes " " and "."

uniqueLetters = { c for c in sentence.lower() if c.isalnum()}
print((uniqueLetters))