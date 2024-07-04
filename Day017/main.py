list1 = [4,7,17,70,75,"Saptarshi",True]
print(list1)
print(type(list1))
# print("Entity at list position 0 is : ",list1[0])
for i in range (0,len(list1)):
  print("Entity at list position ",i," is : ",list1[i])
print("Entity at list position -3 is : ",list1[-3])   #list1[4] : len(list1) - 3
colors = ["Yellow", "Red", "Blue", "Purple", "Cyan"]
if "Pink" in colors:
  print("Pink is present")
else:
  print("Pink is not present")
#Python strings are case sensitive  
if "red".capitalize() in colors:
    print("Happy outcome")
else:
    print("Unhappy outcome")

if "arsh" in "Saptarshi":
  print("Yes, present")
else:
  print("No, not present")
if "ash" in "Saptarshi":
  print("Yes, present")
else:
  print("No, not present")

list2 = list1+[1,57,65,77,"Added data",52,30]
print(list2[:])   #list2[0:len(list2)]
print("Length of list2 is : ",len(list2))
print(list2[1:10:2])     #list_name[start:end:jump_index]

#List comprehension
list3 = [i for i in range(10)]
print(list3)
list4 = [i**2 for i in range(10)]
print(list4)
#List = [Expression(item) for item in iterable if Condition]
list5 = [i**2 for i in range(10) if i%2==0]
print(list5)