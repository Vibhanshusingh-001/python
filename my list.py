marks=[25,36,65,59,8,5,"harry",True,25,47,"7",3]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[len(marks)-3])# for positive index



if "7" in marks:
  print("Yes")
else:
  print("No")

animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes'                      # YE SAMJH ME NHI AAYA

# Same thing applies for strings as well!
# if "Ha" in "Harry":
#   print("Yes")
#listName[start : end : jumpIndex]
print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])                                                      # YE SAMJH ME NHI AAYA

# lst = [i*i for i in range(10)]
# print(lst)
# lst = [i*i for i in range(10) if i%2==0]
# print(lst)