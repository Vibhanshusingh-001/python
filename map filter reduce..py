#map ko dedo aap pahle function ka naam phir dedo list jisame aap har element par ye function apply karna chahte ho
# map ,filter ,reduce ---> higher order function---->function ko jab function as a argumnent le leta hai tab use higher order function kahate h
# filter--> 1 function aur 1 iterable leta h
# jin jin value ke liye ye function true return karega wo wo values aapke output me hongi otherwise nahi
# reduce hame import karna hota h





# # MAP
# # def cube(x):
# #   return x * x * x


# # print(cube(2))

# l = [1, 2, 4, 6, 4, 3]
# # newl = []
# # for item in l:
# #   newl.append(cube(item))

# newl = list(map(lambda x: x*x*x, l))
# print(newl)




# # FILTER

# def filter_function(a):
#   return a>2

# newnewl = list(filter(filter_function, l))
# print(newnewl)


#REDUCE


from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]


# Calculate the sum of the numbers using the reduce function
def mysum(x, y):
    return x + y


sum = reduce(mysum, numbers)

# Print the sum
print(sum)