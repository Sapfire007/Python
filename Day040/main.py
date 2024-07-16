x = 7
print(x)
z = 4
print (z)
def Hello():
  # print(x) It would print 7 as x = 7 is global variable but latter x is assigned as 10
  x = 10     #local variable
  global z #accesses the global variable within a function
  z = 75
  print(x)
  print("End of fuction.")

Hello()
print(x)
print(z)   #Modified value of z within the function is printed