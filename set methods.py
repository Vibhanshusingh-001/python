s={"vibhu",45,58,123,True,False}
if 45 in s:
    print("45 is present")
else:
    print("45 is not present")

# UNION ------> to unite sets
city={"sidhi","indore","mirzapur","meerut","pondicherry"}
city2= {"matiyari","dhanha"}
city3=city.union(city2)
print(city3)

#UPDATE------->
city={"sidhi","indore","mirzapur","meerut","pondicherry"}
city2= {"matiyari","dhanha"}
City3=city.update(city2)
print(city3)
#intersection and intersection update----->(matlab jo common hai)

# The intersection() and intersection_update() methods prints only items that are similar to both the sets.
# The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.
city={"sidhi","indore","mirzapur","dhanha","meerut","pondicherry"}
city2= {"matiyari","dhanha"}
city3=city.intersection(city2)
print(city3)

#intersection update----->
city={"sidhi","indore","mirzapur","dhanha","meerut","pondicherry"}
city2= {"matiyari","dhanha"}
city.intersection_update(city2)
print(city)
#symmetric_difference and symmetric_difference_update():---->(jo common nhi h)

#The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets.
#The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set

#symmetric_difference :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
#symmetric_difference_update()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
# difference() and difference_update():------>

# The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets.
# The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

# difference()---->
cities = {"sidhi","indore","mirzapur","meerut","pondicherry"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

# difference_update()------>
cities = {"sidhi","indore","mirzapur","meerut","pondicherry"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities.difference_update(cities2)
print(cities)

