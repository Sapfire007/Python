a = int(input("Enter your age : "))
votercard = input("Do you have a voter card ? (Answer in yes/no) : ")
print("Your age is : ",a)
if (a>18):
  if((votercard.lower())=="yes"):
    print("You can vote")
  elif((votercard.lower())=="no"):
    print("You cannot vote")
  else:
    print("Invalid input in voter card confirmation")
elif (a>0 and a<=18):
  print("Sorry you are underage.") #The gap before print statement is called indentation
else:
  print("Invalid input")
b = 7
print(b==7)
print(b!=7)
print(b<=7)
print(b>=7)
print(b>7)
print(b<7)