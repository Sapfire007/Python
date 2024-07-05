"""
Tuples are immutable, hence if we want to add, remove or change tuple items, then
first we must convert the tuple to a list. Then perform operation on that list and
convert it back to tuple
"""
colors = ("Yellow","Red","Blue","Purple","Cyan")
temp = list(colors)
temp.append("Pink")          #add item
temp.pop(3)                  #remove item
temp[0] = "Black"            #change item
colors = tuple(temp)
print(colors)
fruits1 = ("Mango","Apple","Papaya")
fruits2 = ("Grapes","Cherry","Starfruit")
fruits = fruits1+fruits2
print(fruits)
tup1 = (1,2,5,7,1,2,5,3,4,1,9,5,1,1,2)
print("Count of 1 in tup1 is : ",tup1.count(1))
print("First index of 5 in tup1 is : ",tup1.index(5))
print("First index of 5 in tup1 is : ",tup1.index(5,4,-3)) #Index of 5 within index range 4 to -3
print("Length of tup1 is : ",len(tup1))