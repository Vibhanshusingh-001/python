def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print("average is",sum/len(numbers))
average(5,3,6,5,4,32,4)

#Sometimes we may need to pass more arguments than those defined in the actual function.
# This can be done using variable-length arguments.
