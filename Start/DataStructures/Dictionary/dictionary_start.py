# Example file for Programming Foundations: Algorithms by Joe Marini
# demonstrate dictionary usage


# TODO: create a dictionary all at once
dictionary = {"one" : 1, "two" : 2, "three" : 3}
dictionary3 = dict({"oneone" : 11, "twotwo" : 22, "threethree" : 33})
print(dictionary)
# TODO: dictionary a dictionary progressively
dictionary2 = {}
dictionary2["four"] = 4
dictionary2["five"] = 5
dictionary2["six"] = 6

# TODO: replace an item

dictionary2["four"] = 44

# TODO: try to access a nonexistent key
#print(dictionary["four"])

# TODO: iterate the keys and values in the dictionary
print(dictionary.keys())
print(dictionary.values())
print(dictionary2.keys())
print(dictionary2.values())
print(dictionary3.keys())
print(dictionary3.values())