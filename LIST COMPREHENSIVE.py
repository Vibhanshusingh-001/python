# List comprehensions are used for creating new lists from other
# iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.
# list are mutable

#Expression: It is the item which is being iterated.
#Iterable: It can be list, tuples, dictionaries, sets, and even in arrays and strings.
#Condition: Condition checks if the item should be added to the new list or not.
#Accepts items with the small letter “o” in the new list

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
