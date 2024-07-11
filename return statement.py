def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        return sum/len(numbers)

c=average(5,3,6,5,4,32,4)
print(c)
