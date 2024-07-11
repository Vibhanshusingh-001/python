


#dictionary datatype is mutable

name={1:"vibhu",2:"singh",3:"gaharwar"}
print(name)
print(name.values())
print(name.items())
print(name.keys())
for key in name:
    print(f"the value of {key} is {name[key]}")
for key ,value in name.items():
    print(f"the value corresponding to {key} is {value}")



# ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
# ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ek dictionary ke content ko update kar deta hai
# doosare dictinory me
# ep1.clear()
# ep1.pop(122)#us key aur value ko gayab kar dega jiski
# key mention h
# ep1.popitem()
# The popitem() method removes
# the last key-value pair from the dictionary
# del ep1[122]
# we can also use the del keyword to remove a dictionary item.
# print(ep1)

# cmp(dict1, dict2)
# Compares elements of both dict.

# len(dict)
# Gives the total length of the dictionary. This would be equal to the number of items in the dictionary.

# str(dict)
# Produces a printable string representation of a dictionary

# type(variable)
# Returns the type of the passed variable. If passed variable is dictionary, then it would return a dictionary type.