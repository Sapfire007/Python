for i in range (15):
  if(i==10):
    break
  print("5 x",i+1,"=",5*(i+1))
print("Break statement has been executed")  
print("\n")
for i in range (15):
  if(i==10):
    print("Iteration has been skipped for 11th")
    continue
  print("5 x",i+1,"=",5*(i+1))