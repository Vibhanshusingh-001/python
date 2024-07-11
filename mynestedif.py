num=int(input("enter your number:"))
print(num)
if(num<0):
    print("your number is negative")
    if(num>0):
        print("your number is positive")
    elif(num<10):
        print("your number is less than 10")
    elif(num<20):
        print("your number is less than 20")
    else:
        print("your number is grater than 20")
else:
    print("your number is positive ")



