# for Loop with else in Python
for i in range(5):
  print(i)

else:
  print("Out of for loop")

print("\n")
for i in []:
  print(i)

else:
  print("Out of for loop")

print("\n")
for i in range(6):
  print(i)
  if(i==4):
    break #End of for loop

else:
  print("else has been executed.")

print("\n")
j = 0
while (j<7):
  print(j)
  j = j + 1
  if (j==4):
    break #End of for loop

else:
  print("else has been executed.")

print("\n")
for i in range(5):
  print("iteration no {} in for loop".format(i+1))
else:
  print("else block in loop")
print("Out of loop")