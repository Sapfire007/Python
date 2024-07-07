s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
print(s1, s2)
s1.update(s2)   #Values of s2 get in s1
print(s1, s2)
colors1 = {"Red","Blue","Green"}
colors2 = {"Yellow","Cyan","Purple","Blue","Pink","Grey","Red"}
colors3 = colors1.union(colors2)
print(colors3)
colors4 = colors1.intersection(colors2)
print(colors4)
colors5 = colors1.copy() 
colors5.intersection_update(colors2)
print(colors5)
animals1 = {"Dog","Cat","Horse","Cow","Goat"}
animals2 = {"Squirrel","Cat","Horse","Cow","Sheep"}
animals3 = animals1.symmetric_difference(animals2)
print(animals3)   #Unique ones among both the sets
animals4 = animals1.copy()
animals4.symmetric_difference_update(animals2)
print(animals4)
fruits1 = {"Apple","Cherry","Guava","Papaya","Watermelon"}
fruits2 = {"Strawberry","Plum","Cherry","Grapes","Papaya"}
fruits3 = fruits1.difference(fruits2) #fruits1 - fruits2
print(fruits3)
fruits4 = fruits2.difference(fruits1) #fruits2 - fruits1
print(fruits4)
elements1 = {"Fire","Water"}
elements2 = {"Wind","Earth"}
print(elements1.isdisjoint(elements2))
elements3 = elements1.copy()
elements3.add("Wind")
# print(elements3)
print(elements3.isdisjoint(elements2))
animals5 = {"Tiger","Giraffe","Gorilla","Lion","Bear","Kangaroo","Panda"}
animals6 = {"Gorilla","Lion","Tiger"}
print(animals5.issuperset(animals6))
print(animals6.issubset(animals5))
animals7 = {"Gorilla","Lion","Tiger","Elephant","Sloth"}
print(animals5.issuperset(animals7)) #All elements of animals7 must be present in animals5 to have animals5 as a superset
print(animals7.issubset(animals5))
a1 = {"Hello","Hi","Wassup"}
a2 = {"Hey","Sup"}
a1.update(a2)
print(a1, a2)
Countries1 = {"India","Japan","Bhutan","USA","Canada"}
Countries2 = Countries1.copy()
Countries1.remove("Bhutan")
print(Countries1)
#Countries2.remove("Chile")  This will display an error in the output
Countries2.discard("Chile")
print(Countries2)
electronics1 = {"Fan","Television","Laptop","LEDs","Tablets"}
item = electronics1.pop()
print(electronics1)
print(item)
house = {"Windows","Doors","Rooms","Ceilings"}
house2 = house.copy()
del house
# print(house) #This will show an error cuz set:house has been deleted and doesnt exist
house2.clear()
print(house2) #Output: set()
#To check if element is present in a set :
set1 = {"Saptarshi",17,7.5,True}
if False in set1:
  print("False is present in set1")
else:
  print("False is not present in set1")