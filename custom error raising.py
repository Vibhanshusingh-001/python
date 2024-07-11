# salary=int(input("enter your salary:"))
# if not 2000<salary<5000:
#     raise ValueError("not a valid salary")

# a = int(input("Enter any value between 5 and 9:"))
# if (a < 5 or a > 9):
#     raise ValueError("Value should be between 5 and 9")
# error raise karne ka sabse accha use hai ki agr koi error aaye to program wahi ruk jaaye aur kuch unexpected n ho jaaye

a=int(input("enter your input:"))
if(a>9 or a<2):
    raise ValueError("value should be between 2 and 9")
else:
    print("you make right entry")