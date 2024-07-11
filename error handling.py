
# a=input("entr your entry:")
# print(f"enter your entry{a}")
# try:
#    for i in range(1,11):
#     print(f"{int(a)}x{i}={int(a)*i}")
# except ValueError:
#     print("your entry is wrong")


try:
    num = int(input("Enter an integer: "))
    a = [6, 3,5]
    print(a[num])
except ValueError:# to handle value error
    print("Number entered is not an integer.")

except IndexError:
    print("index error")




# error handling --->esaka matlab hai error aaye to aur kuch ho jaaye
# aur specific tarah ka error bhi ham handle kar sakte h

# a=input("enter your entry:")
# print(f"Multiplication table of number {a}")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}x{i},={int(a)*i}")
# except Exception as e:
# # agar program acche se nhi run ho rha to aapko ek exception dekhane ko milega
#     print(e)
#valueerror ---->to handle value error
#Indexerror ----->to handle Index error