# Dictionary Methods in Python
employidandperf = {
  7: 95,
  45 : 84,
  75 : 90,
  745 : 78,
  932 : 78
}
employidandperf2 = {
  777 : 88,
  888 : 41  
}
employidandperf3 = employidandperf.copy()
employidandperf.update(employidandperf2)
print(employidandperf) #Thus dictionaries are ordered
print("employidandperf3 is : ",employidandperf3)
employidandperf3.clear()
print(employidandperf3, type(employidandperf3)) #Will print an empty dictionary
empidndprf = {}
print(empidndprf, type(empidndprf))
employidandperf4 = {
  "Name" : "Karan",
  "Age" : 20,
  "Application" : "Hold"
}
print(employidandperf4)
employidandperf4.pop("Application")
print(employidandperf4)
employidandperf5 = {
  "Name" : "David",
  "Age" : 25,
  "Application" : "Hold",
  "Year of joining" : 2019,
  "On leave" : False,
  "Designation" : "Manager"
}
print(employidandperf5)
for i,j in employidandperf5.items():
  print(i,":",j)
employidandperf5.popitem() #Deletes the last key-value pair
print(employidandperf5)
employidandperf6 = {
  "Name" : "Rohit",
  "Age" : 20,
  "Application" : "Hold"
}
print(employidandperf6)
# del employidandperf6   #Deletes the dictionary
del employidandperf6["Age"]
print(employidandperf6)