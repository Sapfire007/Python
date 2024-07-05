#Tuples are immutable
tup = (4,7,17,"Yellow",True)
# tup[0]=75            This cant be done because tuple values remain unchanged
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print(type(tup[4]))
print(tup[-1])
tup1 = (4,7)
print(type(tup1),tup1)
tup2 = (4)
print(type(tup2),tup2)
if "Yellow" in tup:
  print("Yes, ",tup[3]," is present")
else:
  print("Not present")
newTup = tup[2:-1]
print(newTup)