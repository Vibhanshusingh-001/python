# def percentilecalculator(n,N):
#     parcentile=(n/N*100)
#     print(parcentile)
# N=int(input("enter the value of N:"))
# n=int(input(("enter the value of n:")))
# print(percentilecalculator,(n, N))
# def calculategmean(a,b):
#     mean=a*b/a+b
#     print(mean)
# a=45

# b=36
# print(calculategmean(a,b))
# def greaterlesser(a,b):
#     if(a>b):
#         print("first number is greater")
#     else:
#         print("first number is lesser")
#
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# print(greaterlesser(a,b))



def parecentilecalculator(n,N):
    parcentile=(n*N/100)
    print(parcentile)
n=int(input("enter the value of n"))
N=int(input("enter the value of N"))
print(parecentilecalculator(n,N))