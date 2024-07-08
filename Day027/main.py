#Dictionaries in python
dct = {
  "Saptarshi" : "Human Being",
  "Laptop" : "Electronic gadget"
}
print(dct["Saptarshi"])
empID = {
  7 : "Saptarshi",          #7 is a key and Saptarshi is its value
  127 : "Sam",
  675 : "Ash",
  750 : "Rohan"  
}
print(empID[7])
print(empID.get(7))
#Both of the above statements work the same
#print(empID[75])    This will show an error because empID 75 does not exist
print(empID.get(75))    #This will display output as none
print(empID)
print(empID.keys())
print(empID.values())
for key in empID.keys():
  print(f"The value corresponding to the key {key} is : {empID[key]}")
print(type(empID.items()))
print(empID.items())
for key, value in empID.items():
  print(f"The value corresponding to the key {key} is : {value}")