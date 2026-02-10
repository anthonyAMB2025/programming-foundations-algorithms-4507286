# Example file for Programming Foundations: Algorithms by Joe Marini
# using a hashtable to count individual items
from collections import defaultdict

# define a set of items that we want to count
items = ["apple", "pear", "orange", "banana", "apple",
         "orange", "apple", "pear", "banana", "orange",
         "apple", "kiwi", "pear", "apple", "orange"]

# TODO: create a hashtable object to hold the items and counts
counter = defaultdict(int)

# TODO: iterate over each item and increment the count for each one
for i in items:
  counter[i] += 1



# print the results
print(counter)
