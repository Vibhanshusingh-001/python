#DEFAULT ARGUMENTS


# def average(a=45,b=35):
#     my=(a+b)/2
#     print(my)
# average()
#
# #
# def average(a=45,b=35):
#     my=(a+b)/2
#     print(my)
# average(a=85,b=65)


#We can provide a default value while creating a function.
# This way the function assumes a default value even if a value is not provided in the function call for that argument.

def myaverage(a=45,b=36):
    sum=a+b/2
    print(sum)
myaverage()


def myaverage(a=45,b=36):
    sum=a+b/2
    print(sum)
myaverage(a=58,b=96)