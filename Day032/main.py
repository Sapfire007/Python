# Raising custom errors in Python
a = int(input("Enter any value between 5 and 9 : "))
if (a<5 or a>9) :
  raise ValueError("Value out of specified range ~Sap")

#Take an input from the user 0 to 9 or "quit":
b = input("Enter any value between 0 to 9 : ")
if (b.isdecimal()) is True:
  if (int(b)<0 or int(b)>9):
    raise ValueError("Value out of specified range ~Sap")
elif(b!="quit"):
  raise ValueError("Invalid input ~Sap")