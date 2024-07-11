import math

result = math.sqrt(9)
print(result)  # Output: 3.0

#from keyword
from math import sqrt

result = sqrt(9)
print(result)  # Output: 3.0
#You can also import multiple functions or variables at once by separating them with a comma:
from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

#It's also possible to import all functions and variables from a module using the * wildcard
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793

#The "as" keyword

import math as m
result = m.sqrt(9)
print(result)  # Output: 3.0
print(m.pi)  # Output: 3.141592653589793
#dir that you can use to view the names of all the functions and variables defined in a module
