

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  # finally:
  #   print("I am always executed")
  print("I am always executed")


x = func1()
print(x)




      


#what is the difference betwwen finaaly keyword and print statement---->
# jab ham cheejo ko function me wrap karte h aur tab agar error aata h to print statement
# nhi excute hoga magr ham agr finally keyword ka use karenge to function me error aane ke baad bhi finaaly wala statement
# print hoga