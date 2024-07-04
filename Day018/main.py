l1 = [70,100,1,2,3,4,5,6]
print(l1)
l1.append(7)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l2 = [4,7,17,35,42,47,7,54,75,7]
print(l2)
print(l2.index(17))
print(l2.count(7))
l3 = [45,64,53,21,67]
newlist = l3
newlist[0] = 0
print(l3)   #l3 also changes because newlist is a reference of l3
l4 = [45,64,53,21,67]
newlist2 = l4.copy()
newlist2[0] = 0
print(l4)  #l4.copy() fixes the issue mentioned above
fruits = ["Mango","Cherry","Apple","Strawberry"]
fruits.insert(2,"Grapes")     #.insert(index,item) inserts your added item in the index pushing the rest elements
print(fruits)
living_things = ["Mammals","Reptiles","Insects","Birds","Fishes","Micro organisms"]
print(living_things)
flora = ["Plants","Shrubs","Trees","Creepers"]
print(flora)
living_things.extend(flora) #living_things=living_things+flora could also be done
print(living_things)
living_things.sort()
print(living_things)