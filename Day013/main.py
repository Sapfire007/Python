for i in range(3):
  print(i)

print("\n")
j = 0
while(j<=3):
  print(j)
  j = j+1

s = 0
while(s<17):        #Wont exit the loop until the satement becomes false, i.e., 17 or higher 
  s=int(input("Enter a number : "))
  print(s,", well well let's see.")
print("You cracked the code!")
print("\n")

#Decrementing while loop
a = 7
while(a>0):
  print(a)
  a = a-1
else:
  print("The while condition stopped meeting so else has been executed.")