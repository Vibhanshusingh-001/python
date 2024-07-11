#matchcase statement ---> for variable matching
# y=int(input("enter value of x:"))
# y is variable to match
# match y:
#     case 0:
#         print("value of y is zero",y)
#     case 5:
#         print("the value of y is 5",y)
#     case _ if y>25:
#         print("value of y is grater then 25",y)
#     case _ if y<25:
#         print("value of y is less than 25",y)
#     case _:
#         print(y)

y=int(input("enter the value of y:"))
match y :
    case 0:
        print("the value of y is 0",y)
    case 5:
        print("value of y is 5",y)
    case _ if y>20:
        print("value of y is greater than 20",y)
    case _ if y<20:
        print("value of y is less than 20",y)
    case _ :
        print("that is ",y)





