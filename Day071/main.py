# Time Module in Python
import time
def usingWhile():
  i = 0
  while i<50000:
    print(i)
    i += 1
  pass

def usingFor():
  for i in range(50000):
    print(i)
  pass

init = time.time() #Calculates total seconds passed since year 1970
usingFor()
t1 = time.time() - init
print(f"Time taken by the for loop : {t1} sec") # (count of seconds passed since 1970 till this current line of code,i.e, after time taken by the for loop in the function usingFor()) - (seconds passed from 1970 till init is run in line 15)
init2 = time.time()
usingWhile()
print(f"Time taken by the for loop : {t1} sec") 
print(f"Time taken by the while loop : {time.time() - init2} sec")